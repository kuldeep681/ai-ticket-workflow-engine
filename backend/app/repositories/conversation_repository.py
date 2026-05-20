from sqlalchemy.orm import Session

from app.models.conversation import Conversation


class ConversationRepository:

    @staticmethod
    def create_message(
        db: Session,
        message_data: dict
    ):

        message = Conversation(**message_data)

        db.add(message)

        db.commit()

        db.refresh(message)

        return message

    @staticmethod
    def get_ticket_messages(
        db: Session,
        ticket_id: int
    ):

        return db.query(Conversation).filter(
            Conversation.ticket_id == ticket_id
        ).all()