from pydantic import BaseModel
from typing import List

# =========================================================
# REQUEST
# =========================================================

class RAGQueryRequest(BaseModel):

    ticket_id: int

    question: str


# =========================================================
# RESPONSE
# =========================================================

class RAGQueryResponse(BaseModel):

    question: str

    answer: str

    sources: List[str]