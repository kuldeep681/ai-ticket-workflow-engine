from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database.session import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text, nullable=False)

    status = Column(String, default="OPEN")

    priority = Column(String, default="MEDIUM")

    category = Column(String, nullable=True)

    department = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    conversations = relationship(
    "Conversation",
    back_populates="ticket",
    cascade="all, delete"
    )

    workflow_logs = relationship(
    "WorkflowLog",
    back_populates="ticket",
    cascade="all, delete"
    )