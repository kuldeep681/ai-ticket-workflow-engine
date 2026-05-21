from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database.session import Base


class ConversationSummary(Base):

    __tablename__ = "conversation_summaries"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticket_id = Column(
        Integer,
        ForeignKey("tickets.id"),
        nullable=False
    )

    summary = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )