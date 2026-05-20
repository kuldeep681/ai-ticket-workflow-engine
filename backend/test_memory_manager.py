import app.models

from app.database.session import SessionLocal

from app.memory.memory_manager import (
    MemoryManager
)

db = SessionLocal()

ticket_id = 1

memory = MemoryManager.build_conversation_memory(
    db=db,
    ticket_id=ticket_id
)

print(memory)