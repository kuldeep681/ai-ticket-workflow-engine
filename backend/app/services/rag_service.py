from app.rag.rag_pipeline import (
    generate_rag_response
)

# =========================================================
# RAG SERVICE
# =========================================================

class RAGService:

    @staticmethod
    def query_knowledge_base(
        question: str,
        conversation_memory: str = "",
        workflow_context: str = "",
        workflow_guidance: str = "",
        workflow_actions: str = "",
        workflow_lifecycle_context: str = "",
        historical_memory: str = "",
        next_troubleshooting_action: str = ""
    ):

        result = generate_rag_response(
            question=question,

            conversation_memory=
            conversation_memory,

            workflow_context=
            workflow_context,

            workflow_guidance=
            workflow_guidance,

            workflow_actions=
            workflow_actions,

            workflow_lifecycle_context=
            workflow_lifecycle_context,

            historical_memory=
            historical_memory,

            next_troubleshooting_action=
            next_troubleshooting_action
        )

        return result