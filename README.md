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
<h2> Workflow</h2>

```mermaid
flowchart TD
    A[User Logs In] --> B{Identify Role}
    B --> C[Check Role Permissions]
    C --> D[User Submits Query]
    D --> E[Retrieve Role-Based Document]
    E --> F[Generate Answer with LLM]
    F --> G[Return Context-Aware, Secure Response]
    %% Define node styles
    style A fill:#D0E6FF,stroke:#0066CC,stroke-width:2px
    style B fill:#FFEDD5,stroke:#F97316,stroke-width:2px
    style C fill:#FEF9C3,stroke:#CA8A04,stroke-width:2px
    style D fill:#DCFCE7,stroke:#22C55E,stroke-width:2px
    style E fill:#E0E7FF,stroke:#6366F1,stroke-width:2px
    style F fill:#FCE7F3,stroke:#EC4899,stroke-width:2px
    style G fill:#FFE4E6,stroke:#EF4444,stroke-width:2px
