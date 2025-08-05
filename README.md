```mermaid
flowchart TD
    A[User Logs In] --> B{Identify Role}
    B --> C[Check Role Permissions]
    C --> D[User Submits Query]
    D --> E[Retrieve Role-Based Document - RAG]
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
