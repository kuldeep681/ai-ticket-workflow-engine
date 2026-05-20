from sqlalchemy.orm import Session

from app.repositories.conversation_repository import (
    ConversationRepository
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

        # Fetch all messages for ticket
        messages = ConversationRepository.get_ticket_messages(
            db=db,
            ticket_id=ticket_id
        )

        # Convert SQLAlchemy objects into dictionaries
        formatted_messages = []

        for message in messages:

            formatted_messages.append({
                "sender": message.sender,
                "message": message.message
            })

        # Apply memory window
        recent_messages = get_recent_messages(
            formatted_messages
        )

        # Format for prompt injection
        memory_context = format_memory_context(
            recent_messages
        )

        return memory_context