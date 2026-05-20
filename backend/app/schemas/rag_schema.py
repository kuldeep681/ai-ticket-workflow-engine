from pydantic import BaseModel

# =========================================================
# REQUEST
# =========================================================

class RAGQueryRequest(BaseModel):

    question: str

# =========================================================
# RESPONSE
# =========================================================

class RAGQueryResponse(BaseModel):

    question: str

    answer: str

    sources: list[str]