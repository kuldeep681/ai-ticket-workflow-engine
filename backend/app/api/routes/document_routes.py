from typing import List, Annotated

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.document_service import (
    DocumentService
)

from app.schemas.document_schema import (
    DocumentResponse,
    BulkDocumentResponse
)

# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

# =========================================================
# BULK DOCUMENT UPLOAD
# =========================================================

@router.post("/upload")
async def upload_multiple_documents(
    file1: UploadFile = File(...),
    file2: UploadFile = File(None),
    file3: UploadFile = File(None),
    file4: UploadFile = File(None),
    file5: UploadFile = File(None),
    db: Session = Depends(get_db)
):

    uploaded_files = [
        file
        for file in [
            file1,
            file2,
            file3,
            file4,
            file5
        ]
        if file is not None
    ]

    documents = (
        DocumentService.save_documents(
            db,
            uploaded_files
        )
    )

    return {
        "success": True,
        "documents": documents
    }