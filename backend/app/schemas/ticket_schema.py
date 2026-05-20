from pydantic import BaseModel
from datetime import datetime


class TicketCreate(BaseModel):
    title: str
    description: str


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    category: str | None = None
    department: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TicketStatusUpdate(BaseModel):
    status: str