from langchain_community.document_loaders import DirectoryLoader, TextLoader, CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from functools import partial
api_key="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"
#print(api_key)
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", api_key=api_key,temperature=0.7)

embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-large-v2")
def load_data(role):
    #print(role)
    if role.lower() == "c-level":
        try:
            loader = DirectoryLoader(
                path="data/",
                glob="**/*.md",
                loader_cls=partial(TextLoader, encoding="utf-8"),
                recursive=True  # ✅ Required for "**/*.md"
            )
            md_docs = loader.load()
        except Exception as e:
            print(f"Error loading markdown files: {e}")
            md_docs = []
        csv_loader = CSVLoader(file_path=f"data/hr/hr_data.csv", source_column="employee_id")
        csv_docs = csv_loader.load()
        docs=md_docs + csv_docs
    elif role.lower() == "employee":

       loader = DirectoryLoader(path=f"data/general", glob="*.md", loader_cls=TextLoader)
       docs = loader.load()
    elif role.lower() == "hr":
        csv_loader = CSVLoader(file_path=f"data/hr/hr_data.csv", source_column="employee_id")
        docs = csv_loader.load()
    else:
        loader = DirectoryLoader(path=f"data/{role}", glob="*.md", loader_cls=TextLoader)
        docs = loader.load()

    vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory="chroma")


def retrieval_chain():

    vectordb = Chroma(persist_directory="chroma",embedding_function=embeddings)
    retriever = vectordb.as_retriever()
    prompt_template = """
    {context}

    {question}

    If the answer is not in the context, respond with:
    "I’m sorry, I couldn’t find the answer to that question in the provided information."
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain





 





