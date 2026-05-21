from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from datetime import datetime

from app.database.session import Base


class WorkflowMemoryProfile(Base):

    __tablename__ = "workflow_memory_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_type = Column(
        String,
        nullable=False
    )

    issue_type = Column(
        String,
        nullable=False
    )

    resolution_summary = Column(
        Text,
        nullable=False
    )

    successful_resolution = Column(
        String,
        default="yes"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )