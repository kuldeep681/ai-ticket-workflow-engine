from sqlalchemy.orm import Session

from app.repositories.conversation_repository import (
    ConversationRepository
)

from app.repositories.summary_repository import (
    SummaryRepository
)

from app.memory.memory_window import (
    get_recent_messages,
    format_memory_context
)


class MemoryManager:

    @staticmethod
    def build_conversation_memory(
        db: Session,
        ticket_id: int
    ):

        # ======================================
        # GET RECENT RAW MESSAGES
        # ======================================

        messages = (
            ConversationRepository.get_ticket_messages(
                db=db,
                ticket_id=ticket_id
            )
        )

        formatted_messages = []

        for message in messages:

            formatted_messages.append({
                "sender": message.sender,
                "message": message.message
            })

        # ======================================
        # APPLY MEMORY WINDOW
        # ======================================

        recent_messages = get_recent_messages(
            formatted_messages
        )

        recent_memory_context = (
            format_memory_context(
                recent_messages
            )
        )

        # ======================================
        # GET HISTORICAL SUMMARIES
        # ======================================

        summaries = (
            SummaryRepository.get_ticket_summaries(
                db=db,
                ticket_id=ticket_id
            )
        )

        summary_context = ""

        if summaries:

            summary_lines = []

            for summary in summaries:

                summary_lines.append(
                    f"- {summary.summary}"
                )

            summary_context = "\n".join(
                summary_lines
            )

        # ======================================
        # BUILD HYBRID MEMORY
        # ======================================

        memory_context = f"""
================ RECENT CONVERSATION ================

{recent_memory_context}

================ HISTORICAL SUMMARIES ================

{summary_context}
"""

        return memory_context