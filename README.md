<h1> Role-Based Access Control Chatbot with RAG </h1>

<div>
  <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp A secure and intelligent chatbot that delivers role-specific, context-aware responses by combining Role-Based Access Control (RBAC) with Retrieval-Augmented Generation (RAG). This system ensures only authorized users can access specific data, improving communication and decision-making across departments.</p></div>

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

<pre>```mermaid
flowchart TD
    A[🔐 User Logs In] --> B{🎭 Identify Role}
    B --> C[📄 Check Role Permissions]
    C --> D[💬 User Submits Query]
    D --> E[📂 Retrieve Role-Based Documents (RAG)]
    E --> F[🤖 Generate Answer with LLM]
    F --> G[📤 Return Context-Rich, Secure Response]</pre>

