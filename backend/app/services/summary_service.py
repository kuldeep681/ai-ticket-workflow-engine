from sqlalchemy.orm import Session

from app.repositories.conversation_repository import (
    ConversationRepository
)

from app.repositories.summary_repository import (
    SummaryRepository
)

from app.memory.conversation_summarizer import (
    ConversationSummarizer
)


class SummaryService:

    # ==========================================
    # GENERATE SUMMARY FOR TICKET
    # ==========================================

    @staticmethod
    def generate_ticket_summary(
        db: Session,
        ticket_id: int
    ):

        messages = (
            ConversationRepository.get_ticket_messages(
                db,
                ticket_id
            )
        )

        if not messages:
            return None

        # ======================================
        # BUILD CONVERSATION TEXT
        # ======================================

        conversation_text = ""

        for msg in messages:

            conversation_text += (
                f"{msg.sender}: "
                f"{msg.message}\n"
            )

        # ======================================
        # GENERATE SUMMARY
        # ======================================

        summary = (
            ConversationSummarizer
            .summarize_conversation(
                conversation_text
            )
        )

        # ======================================
        # SAVE SUMMARY
        # ======================================

        return (
            SummaryRepository.create_summary(
                db,
                {
                    "ticket_id": ticket_id,
                    "summary": summary
                }
            )
        )

    # ==========================================
    # GET TICKET SUMMARIES
    # ==========================================

    @staticmethod
    def get_ticket_summaries(
        db: Session,
        ticket_id: int
    ):

        return (
            SummaryRepository.get_ticket_summaries(
                db,
                ticket_id
            )
        )