TICKET-AUTOMATION-SYSTEM/
│
├── .vscode/
│ └── settings.json
│
├── backend/
│ │
│ ├── app/
│ │ │
│ │ ├── **pycache**/
│ │ │
│ │ ├── api/
│ │ │ └── routes/
│ │ │ ├── **pycache**/
│ │ │ ├── ai_routes.py
│ │ │ ├── conversation_routes.py
│ │ │ ├── document_routes.py
│ │ │ ├── health_routes.py
│ │ │ ├── ml_routes.py
│ │ │ ├── rag_routes.py
│ │ │ ├── ticket_routes.py
│ │ │ └── workflow_routes.py
│ │ │
│ │ ├── chroma_db/
│ │ │ ├── a3d64237-4e53-4650-b4f6-6200cd8179c0/
│ │ │ └── chroma.sqlite3
│ │ │
│ │ ├── core/
│ │ │ ├── **pycache**/
│ │ │ └── config.py
│ │ │
│ │ ├── database/
│ │ │ ├── **pycache**/
│ │ │ ├── connection.py
│ │ │ ├── dependencies.py
│ │ │ ├── init_db.py
│ │ │ └── session.py
│ │ │
│ │ ├── memory/
│ │ │ ├── **pycache**/
│ │ │ ├── conversation_summarizer.py
│ │ │ ├── memory_manager.py
│ │ │ └── memory_window.py
│ │ │
│ │ ├── ml/
│ │ │ │
│ │ │ ├── datasets/
│ │ │ │ ├── cleaned/
│ │ │ │ │ ├── classification_dataset.csv
│ │ │ │ │ ├── priority_dataset.csv
│ │ │ │ │ └── routing_dataset.csv
│ │ │ │ │
│ │ │ │ ├── processed/
│ │ │ │ │
│ │ │ │ └── raw/
│ │ │ │ ├── dataset-tickets-multi-lang-4-20k.csv
│ │ │ │ └── IT Support Ticket Data.csv
│ │ │ │
│ │ │ ├── inference/
│ │ │ │ ├── **pycache**/
│ │ │ │ ├── classifier_inference.py
│ │ │ │ ├── priority_inference.py
│ │ │ │ └── routing_inference.py
│ │ │ │
│ │ │ ├── preprocessing/
│ │ │ │ └── clean_dataset.py
│ │ │ │
│ │ │ ├── saved_models/
│ │ │ │ ├── classifier_model.pkl
│ │ │ │ ├── priority_model.pkl
│ │ │ │ ├── priority_vectorizer.pkl
│ │ │ │ ├── routing_model.pkl
│ │ │ │ ├── routing_vectorizer.pkl
│ │ │ │ └── tfidf_vectorizer.pkl
│ │ │ │
│ │ │ └── training/
│ │ │ ├── debug_dataset.py
│ │ │ ├── debug_priority_dataset.py
│ │ │ ├── debug_routing_dataset.py
│ │ │ ├── train_classifier.py
│ │ │ ├── train_priority_model.py
│ │ │ └── train_routing_model.py
│ │ │
│ │ ├── models/
│ │ │ ├── **pycache**/
│ │ │ ├── **init**.py
│ │ │ ├── conversation_summary.py
│ │ │ ├── conversation.py
│ │ │ ├── document.py
│ │ │ ├── ticket.py
│ │ │ ├── workflow_log.py
│ │ │ ├── workflow_memory_profile.py
│ │ │ └── workflow_state.py
│ │ │
│ │ ├── rag/
│ │ │ ├── **pycache**/
│ │ │ ├── chunker.py
│ │ │ ├── embedding_model.py
│ │ │ ├── rag_pipeline.py
│ │ │ ├── retriever.py
│ │ │ ├── text_extractor.py
│ │ │ └── vector_store.py
│ │ │
│ │ ├── repositories/
│ │ │ ├── **pycache**/
│ │ │ ├── conversation_repository.py
│ │ │ ├── document_repository.py
│ │ │ ├── summary_repository.py
│ │ │ ├── ticket_repository.py
│ │ │ ├── workflow_memory_repository.py
│ │ │ ├── workflow_repository.py
│ │ │ └── workflow_state_repository.py
│ │ │
│ │ ├── schemas/
│ │ │ ├── **pycache**/
│ │ │ ├── ai_schema.py
│ │ │ ├── conversation_schema.py
│ │ │ ├── document_schema.py
│ │ │ ├── rag_schema.py
│ │ │ ├── ticket_schema.py
│ │ │ └── workflow_schema.py
│ │ │
│ │ ├── services/
│ │ │ ├── **pycache**/
│ │ │ ├── classification_service.py
│ │ │ ├── conversation_service.py
│ │ │ ├── document_service.py
│ │ │ ├── memory_service.py
│ │ │ ├── ollama_service.py
│ │ │ ├── priority_service.py
│ │ │ ├── rag_service.py
│ │ │ ├── routing_service.py
│ │ │ ├── summary_service.py
│ │ │ ├── ticket_service.py
│ │ │ ├── workflow_memory_service.py
│ │ │ ├── workflow_service.py
│ │ │ └── workflow_state_service.py
│ │ │
│ │ ├── storage/
│ │ │ └── documents/
│ │ │ ├── email_setup.txt
│ │ │ ├── employee_onboarding.txt
│ │ │ ├── incident_escalation_policy.txt
│ │ │ ├── laptop_hardware_guide.txt
│ │ │ ├── mfa_troubleshooting.txt
│ │ │ ├── password_reset.txt
│ │ │ ├── printer_troubleshooting.txt
│ │ │ ├── software_installation_sop.txt
│ │ │ ├── vpn_guide.txt
│ │ │ └── wifi_troubleshooting.txt
│ │ │
│ │ ├── utils/
│ │ │
│ │ ├── workflow/
│ │ │ ├── **pycache**/
│ │ │ ├── troubleshooting_engine.py
│ │ │ ├── workflow_actions.py
│ │ │ ├── workflow_context_builder.py
│ │ │ ├── workflow_guidance.py
│ │ │ ├── workflow_lifecycle.py
│ │ │ ├── workflow_rules.py
│ │ │ ├── workflow_state_manager.py
│ │ │ └── workflow_transitions.py
│ │ │
│ │ └── main.py
│ │
│ ├── .env
│ ├── requirements.txt
│ │
│ ├── test_chunking.py
│ ├── test_classification_service.py
│ ├── test_embeddings.py
│ ├── test_extraction.py
│ ├── test_memory_manager.py
│ ├── test_memory_service.py
│ ├── test_memory_window.py
│ ├── test_priority_service.py
│ ├── test_rag_pipeline.py
│ ├── test_retrieval.py
│ ├── test_routing_service.py
│ └── test_vector_store.py
│
├── database/
│ └── ticket_system.db
│
├── docs/
│
├── frontend/
│ │
│ ├── node_modules/
│ ├── public/
│ │ ├── favicon.ico
│ │ └── icons.svg
│ │
│ ├── src/
│ │ │
│ │ ├── api/
│ │ │ ├── chatApi.js
│ │ │ ├── client.js
│ │ │ └── ticketApi.js
│ │ │
│ │ ├── assets/
│ │ │ ├── hero.png
│ │ │ ├── react.svg
│ │ │ └── vite.svg
│ │ │
│ │ ├── components/
│ │ ├── hooks/
│ │ ├── layouts/
│ │ │
│ │ ├── pages/
│ │ │ ├── CreateTicket.jsx
│ │ │ ├── Dashboard.jsx
│ │ │ └── TicketDetails.jsx
│ │ │
│ │ ├── types/
│ │ ├── utils/
│ │ │
│ │ ├── App.css
│ │ ├── App.jsx
│ │ ├── index.css
│ │ └── main.jsx
│ │
│ ├── eslint.config.js
│ ├── index.html
│ ├── package-lock.json
│ ├── package.json
│ ├── README.md
│ └── vite.config.js
│
├── Folder_structure.md
├── Phase_1.md
├── Phase_2.md
├── Phase_3.md
├── Project_architecture.md
└── README.md
