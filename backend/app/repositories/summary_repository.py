from sqlalchemy.orm import Session

from app.models.conversation_summary import (
    ConversationSummary
)


class SummaryRepository:

    # ==========================================
    # CREATE SUMMARY
    # ==========================================

    @staticmethod
    def create_summary(
        db: Session,
        summary_data: dict
    ):

        summary = ConversationSummary(
            **summary_data
        )

        db.add(summary)

        db.commit()

        db.refresh(summary)

        return summary

    # ==========================================
    # GET TICKET SUMMARIES
    # ==========================================

    @staticmethod
    def get_ticket_summaries(
        db: Session,
        ticket_id: int
    ):

        return (
            db.query(ConversationSummary)
            .filter(
                ConversationSummary.ticket_id
                == ticket_id
            )
            .all()
        )