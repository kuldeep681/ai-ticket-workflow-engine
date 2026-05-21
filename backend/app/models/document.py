from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.session import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    file_path = Column(
        String,
        nullable=False
    )

    # ==========================================
    # WORKFLOW DOMAIN
    # ==========================================

    workflow_domain = Column(
        String,
        nullable=False,
        default="general"
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )