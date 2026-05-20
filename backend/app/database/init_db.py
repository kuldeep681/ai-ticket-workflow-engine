from app.database.connection import engine
from app.database.session import Base

from app.models.ticket import Ticket
from app.models.conversation import Conversation
from app.models.workflow_log import WorkflowLog
from app.models.document import Document


def init_db():
    Base.metadata.create_all(bind=engine)