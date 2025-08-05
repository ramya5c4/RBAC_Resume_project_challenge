flowchart LR
    %% Define styles
    classDef start fill:#d1e7dd,stroke:#0f5132,color:#0f5132;
    classDef process fill:#cfe2ff,stroke:#084298,color:#084298;
    classDef decision fill:#fff3cd,stroke:#664d03,color:#664d03;
    classDef output fill:#f8d7da,stroke:#842029,color:#842029;

    A[User Logs In]:::start --> B{Identify Role}:::decision
    B --> C[Check Role Permissions]:::process
    C --> D[User Submits Query]:::process
    D --> E[Retrieve Role-Based Documents (RAG)]:::process
    E --> F[Generate Answer with LLM]:::process
    F --> G[Return Secure, Context-Aware Response]:::output
