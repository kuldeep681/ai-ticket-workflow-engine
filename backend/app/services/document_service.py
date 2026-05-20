import shutil
from pathlib import Path

from sqlalchemy.orm import Session

from app.repositories.document_repository import (
    DocumentRepository
)

# =========================================================
# STORAGE DIRECTORY
# =========================================================

STORAGE_DIR = Path(
    "app/storage/documents"
)

STORAGE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# =========================================================
# DOCUMENT SERVICE
# =========================================================

class DocumentService:

    # =====================================================
    # MULTIPLE DOCUMENT UPLOAD
    # =====================================================

    @staticmethod
    def save_documents(
        db: Session,
        uploaded_files
    ):

        saved_documents = []

        for uploaded_file in uploaded_files:

            file_location = (
                STORAGE_DIR / uploaded_file.filename
            )

            # ==========================================
            # SAVE PHYSICAL FILE
            # ==========================================

            with open(file_location, "wb") as buffer:

                shutil.copyfileobj(
                    uploaded_file.file,
                    buffer
                )

            # ==========================================
            # SAVE DOCUMENT METADATA
            # ==========================================

            document = (
                DocumentRepository.create_document(
                    db,
                    {
                        "filename": uploaded_file.filename,
                        "file_path": str(file_location)
                    }
                )
            )

            saved_documents.append(document)

        return saved_documents