from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime

from sqlalchemy.orm import relationship

from app.database.session import Base


class WorkflowState(Base):

    __tablename__ = "workflow_states"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticket_id = Column(
        Integer,
        ForeignKey("tickets.id"),
        nullable=False,
        unique=True
    )

    workflow_type = Column(
        String,
        nullable=False
    )

    current_issue = Column(
        String,
        nullable=False
    )

    current_step = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="in_progress"
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    ticket = relationship(
        "Ticket"
    )