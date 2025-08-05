
```mermaid
flowchart TD
    A[🔐 User Logs In] --> B{🎭 Identify Role}
    B --> C[📄 Check Role Permissions]
    C --> D[💬 User Submits Query]
    D --> E[📂 Retrieve Role-Based Documents (RAG)]
    E --> F[🤖 Generate Answer with LLM]
    F --> G[📤 Return Context-Rich, Secure Response]

