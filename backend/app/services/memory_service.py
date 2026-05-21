from sqlalchemy.orm import Session

from app.memory.memory_manager import (
    MemoryManager
)


class MemoryService:

    @staticmethod
    def get_conversation_memory(
        db: Session,
        ticket_id: int
    ):

        memory_context = (
            MemoryManager.build_conversation_memory(
                db=db,
                ticket_id=ticket_id
            )
        )

        return memory_context