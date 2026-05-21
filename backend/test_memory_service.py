import app.models

from app.database.session import SessionLocal

from app.services.memory_service import (
    MemoryService
)

db = SessionLocal()

ticket_id = 1

memory = MemoryService.get_conversation_memory(
    db=db,
    ticket_id=ticket_id
)

print(memory)