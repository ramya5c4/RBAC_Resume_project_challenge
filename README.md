<h1> Role-Based Access Control Chatbot with RAG </h1>

<div>   
  <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp A secure and intelligent chatbot that delivers role-specific, context-aware responses by combining Role-Based Access Control (RBAC) with Retrieval-Augmented Generation (RAG). This system ensures only authorized users can access specific data, improving communication and decision-making across departments.</p>

<h2>Features</h2>
<ul>
  <li><b>RBAC:</b> Role-based data access for HR, Finance, Engineering, C-Level, etc.</li>
  <li><b>RAG: </b> Uses embedded documents + LLM to generate smart responses.</li>
  <li><b>Document Store:</b>ChromaDB for vector search.</li>
  <li><b> Embeddings: </b> Uses Hugging Face’s intfloat/e5-large-v2 model.</li>
  <li><b>Natural Language Queries: </b> Supports queries like “Show my reimbursements” or “List marketing campaign results”.</li>
</ul>
<h2> Technologies Used</h2>
<ul>
<li><b>Backend API : </b> FastAPI</li>
<li><b>	RAG Pipeline : </b> LangChain</li>
<li><b>Embedding Model:</b> intfloat/e5-large-v2</li>
<li><b>Vector DB  :</b> ChromaDB </li>
<li><b>LLM	:</b> LLaMA</li>
<li><b>UI  :</b> Streamlit</li>                                   
</ul>
<h2>How it works</h2>
<ul>
1.The user logs in securely.
2.System identified role (e.g., HR, Finance, Engineering).
3.The user submits a natural language question.
4.The system applies RBAC rules to determine which documents the user can access.
5.Only the authorized documents are retrieved from the vector database (ChromaDB).
6.A language model (e.g.,LLaMA) reads the retrieved content.
7.It generates a context-rich and secure response based on the user's role.
8.The chatbot displays the answer in a user-friendly interface. </ul>
