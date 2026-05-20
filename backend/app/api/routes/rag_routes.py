from fastapi import APIRouter

from app.schemas.rag_schema import (
    RAGQueryRequest,
    RAGQueryResponse
)

from app.services.rag_service import (
    RAGService
)

# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

# =========================================================
# RAG QUERY
# =========================================================

@router.post(
    "/query",
    response_model=RAGQueryResponse
)
def query_rag(
    request: RAGQueryRequest
):

    result = (
        RAGService.query_knowledge_base(
            request.question
        )
    )

    return result