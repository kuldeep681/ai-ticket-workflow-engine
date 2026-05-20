from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    @staticmethod
    def create_document(
        db: Session,
        document_data: dict
    ):

        document = Document(**document_data)

        db.add(document)

        db.commit()

        db.refresh(document)

        return document