from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):
    sender: str
    message: str


class MessageResponse(BaseModel):
    id: int
    ticket_id: int
    sender: str
    message: str
    timestamp: datetime

    class Config:
        from_attributes = True