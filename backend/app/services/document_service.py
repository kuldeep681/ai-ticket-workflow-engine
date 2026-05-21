import shutil
from pathlib import Path

from sqlalchemy.orm import Session

from app.repositories.document_repository import (
    DocumentRepository
)

from app.rag.text_extractor import (
    extract_document_text
)

from app.rag.chunker import (
    chunk_text
)

from app.rag.embedding_model import (
    generate_embeddings
)

from app.rag.vector_store import (
    store_embeddings
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
# DETECT WORKFLOW DOMAIN
# =========================================================

def detect_workflow_domain(
    filename: str
):

    filename = filename.lower()

    # ==============================================
    # VPN SUPPORT
    # ==============================================

    if (
        "vpn" in filename
        or "remote_access" in filename
    ):

        return "vpn_support"

    # ==============================================
    # PASSWORD SUPPORT
    # ==============================================

    elif (
        "password" in filename
        or "login" in filename
        or "credential" in filename
    ):

        return "password_support"

    # ==============================================
    # EMAIL SUPPORT
    # ==============================================

    elif (
        "email" in filename
        or "outlook" in filename
        or "mailbox" in filename
    ):

        return "email_support"

    # ==============================================
    # NETWORK SUPPORT
    # ==============================================

    elif (
        "wifi" in filename
        or "network" in filename
        or "internet" in filename
        or "dns" in filename
    ):

        return "network_support"

    # ==============================================
    # MFA SUPPORT
    # ==============================================

    elif (
        "mfa" in filename
        or "otp" in filename
        or "authenticator" in filename
        or "2fa" in filename
    ):

        return "mfa_support"

    # ==============================================
    # HARDWARE SUPPORT
    # ==============================================

    elif (
        "printer" in filename
        or "hardware" in filename
        or "device" in filename
    ):

        return "hardware_support"

    # ==============================================
    # SOFTWARE SUPPORT
    # ==============================================

    elif (
        "software" in filename
        or "application" in filename
        or "install" in filename
    ):

        return "software_support"

    # ==============================================
    # GENERAL
    # ==============================================

    return "general"

# =========================================================
# DOCUMENT SERVICE
# =========================================================

class DocumentService:

    # =====================================================
    # SAVE + INDEX DOCUMENTS
    # =====================================================

    @staticmethod
    def save_documents(
        db: Session,
        uploaded_files
    ):

        saved_documents = []

        for uploaded_file in uploaded_files:

            # ==========================================
            # FILE LOCATION
            # ==========================================

            file_location = (
                STORAGE_DIR / uploaded_file.filename
            )

            # ==========================================
            # SAVE PHYSICAL FILE
            # ==========================================

            with open(
                file_location,
                "wb"
            ) as buffer:

                shutil.copyfileobj(
                    uploaded_file.file,
                    buffer
                )

            # ==========================================
            # DETECT WORKFLOW DOMAIN
            # ==========================================

            workflow_domain = (
                detect_workflow_domain(
                    uploaded_file.filename
                )
            )

            # ==========================================
            # SAVE SQLITE METADATA
            # ==========================================

            document = (
                DocumentRepository.create_document(
                    db,
                    {
                        "filename":
                        uploaded_file.filename,

                        "file_path":
                        str(file_location),

                        "workflow_domain":
                        workflow_domain
                    }
                )
            )

            # ==========================================
            # EXTRACT TEXT
            # ==========================================

            extracted_text = (
                extract_document_text(
                    str(file_location)
                )
            )

            # ==========================================
            # SKIP EMPTY DOCUMENTS
            # ==========================================

            if not extracted_text.strip():

                print(
                    f"Skipped empty document: "
                    f"{uploaded_file.filename}"
                )

                continue

            # ==========================================
            # CREATE CHUNKS
            # ==========================================

            chunks = chunk_text(
                extracted_text
            )

            # ==========================================
            # SKIP EMPTY CHUNKS
            # ==========================================

            if not chunks:

                print(
                    f"No chunks generated for: "
                    f"{uploaded_file.filename}"
                )

                continue

            # ==========================================
            # GENERATE EMBEDDINGS
            # ==========================================

            embeddings = (
                generate_embeddings(
                    chunks
                )
            )

            # ==========================================
            # STORE EMBEDDINGS
            # ==========================================

            store_embeddings(
                chunks=chunks,

                embeddings=embeddings,

                document_name=(
                    uploaded_file.filename
                ),

                workflow_domain=(
                    workflow_domain
                )
            )

            print(
                f"Indexed document: "
                f"{uploaded_file.filename}"
            )

            saved_documents.append(
                document
            )

        return saved_documents