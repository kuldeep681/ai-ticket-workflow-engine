from pydantic import BaseModel
from datetime import datetime


class WorkflowLogResponse(BaseModel):
    id: int
    ticket_id: int
    action: str
    details: str
    timestamp: datetime

    class Config:
        from_attributes = True