from app.rag.rag_pipeline import (
    generate_rag_response
)



# =========================================================
# RAG SERVICE
# =========================================================

class RAGService:

    @staticmethod
    def query_knowledge_base(
        question: str
    ):

        result = generate_rag_response(
            question
        )

        return result