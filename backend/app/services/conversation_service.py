from sqlalchemy.orm import Session

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.repositories.conversation_repository import (
    ConversationRepository
)

from app.services.ollama_service import (
    OllamaService
)

from app.services.workflow_service import (
    WorkflowService
)

from app.services.workflow_service import WorkflowService


class ConversationService:

    @staticmethod
    def add_message(
        db: Session,
        ticket_id: int,
        payload
    ):

        ticket = TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )
        
        if not ticket:
            return None

        message_data = {
            "ticket_id": ticket_id,
            "sender": payload.sender,
            "message": payload.message
        }

        message = ConversationRepository.create_message(
            db,
            message_data
        )

        WorkflowService.log_action(
            db=db,
            ticket_id=ticket_id,
            action="MESSAGE_ADDED",
            details=f"{payload.sender} added a message"
        )
        return message

    @staticmethod
    def get_messages(
        db: Session,
        ticket_id: int
    ):

        ticket = TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )

        if not ticket:
            return None

        return ConversationRepository.get_ticket_messages(
            db,
            ticket_id
        )
    
    @staticmethod
    def generate_ai_response(
        db: Session,
        ticket_id: int
    ):
        ticket = TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )
        
        if not ticket:
            return None

        messages = ConversationRepository.get_ticket_messages(
            db,
            ticket_id
        )
        
        conversation_text = ""
        
        recent_messages = messages[-5:]

        for msg in recent_messages:
            conversation_text += (
                f"{msg.sender}: {msg.message}\n"
            )

        prompt = f"""
        You are an internal IT support assistant chatting with an employee.

        Rules:
        - Respond naturally like chat
        - Never use email formatting
        - Never use placeholders
        - Never say "Dear User"
        - Never mention ticket IDs
        - Keep responses concise
        - Use simple technical troubleshooting
        - Avoid repeating previous responses
        - Focus mainly on the latest message
        - If user says goodbye, reply briefly

        Ticket Title:
        {ticket.title}

        Ticket Description:
        {ticket.description}

        Conversation History:
        {conversation_text}

        Generate the next assistant response.
        """

        ai_response = OllamaService.generate_response(
            prompt
        )
        
        ai_message_data = {
            "ticket_id": ticket_id,
            "sender": "ai",
            "message": ai_response
        }

        saved_message = (
            ConversationRepository.create_message(
                db,
                ai_message_data
            )
        )

        WorkflowService.log_action(
            db=db,
            ticket_id=ticket_id,
            action="AI_RESPONSE_GENERATED",
            details="AI generated a response"
        )

        return saved_message