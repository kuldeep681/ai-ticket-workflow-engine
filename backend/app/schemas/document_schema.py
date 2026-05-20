from typing import List

from pydantic import BaseModel

from datetime import datetime


# =========================================================
# SINGLE DOCUMENT RESPONSE
# =========================================================

class DocumentResponse(BaseModel):

    id: int

    filename: str

    file_path: str

    uploaded_at: datetime

    class Config:
        from_attributes = True


# =========================================================
# BULK DOCUMENT RESPONSE
# =========================================================

class BulkDocumentResponse(BaseModel):

    success: bool

    documents: List[DocumentResponse]