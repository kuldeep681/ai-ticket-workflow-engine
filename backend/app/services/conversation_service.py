from sqlalchemy.orm import Session

from app.services.summary_service import (
    SummaryService
)

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.repositories.conversation_repository import (
    ConversationRepository
)

from app.services.workflow_service import (
    WorkflowService
)

from app.services.rag_service import (
    RAGService
)

from app.workflow.workflow_state_manager import (
    WorkflowStateManager
)

from app.workflow.workflow_context_builder import (
    WorkflowContextBuilder
)

from app.services.workflow_state_service import (
    WorkflowStateService
)


class ConversationService:

    SUMMARY_TRIGGER_COUNT = 12

    # =====================================================
    # ADD MESSAGE
    # =====================================================

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

        # =================================================
        # CREATE MESSAGE
        # =================================================

        message_data = {

            "ticket_id":
            ticket_id,

            "sender":
            payload.sender,

            "message":
            payload.message
        }

        message = (
            ConversationRepository.create_message(
                db,
                message_data
            )
        )

        # =================================================
        # PROCESS USER MESSAGE
        # =================================================

        if payload.sender.lower() == "user":
            print("\nUSER MESSAGE DETECTED")
            print("MESSAGE:", payload.message)
            print("SENDER:", payload.sender)

            WorkflowStateManager.process_message(
                db=db,
                ticket_id=ticket_id,
                user_message=payload.message
            )

            # =============================================
            # FORCE DATABASE SYNC
            # =============================================

            db.commit()

            db.refresh(ticket)

        # =================================================
        # GENERATE SUMMARY IF NEEDED
        # =================================================

        ConversationService.generate_summary_if_needed(
            db=db,
            ticket_id=ticket_id
        )

        # =================================================
        # WORKFLOW LOGGING
        # =================================================

        WorkflowService.log_action(
            db=db,
            ticket_id=ticket_id,
            action="MESSAGE_ADDED",
            details=(
                f"{payload.sender} added a message"
            )
        )

        return message

    # =====================================================
    # GET MESSAGES
    # =====================================================

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

        return (
            ConversationRepository.get_ticket_messages(
                db,
                ticket_id
            )
        )

    # =====================================================
    # GENERATE AI RESPONSE
    # =====================================================

    @staticmethod
    def generate_ai_response(
        db: Session,
        ticket_id: int
    ):

        ticket = (
            TicketRepository.get_ticket_by_id(
                db,
                ticket_id
            )
        )

        if not ticket:
            return None

        messages = (
            ConversationRepository.get_ticket_messages(
                db,
                ticket_id
            )
        )

        if not messages:
            return None

        latest_message = (
            messages[-1].message
        )

        # =================================================
        # BUILD WORKFLOW CONTEXT
        # =================================================

        context_data = (
            WorkflowContextBuilder.build_context(
                db=db,
                ticket_id=ticket_id,
                question=latest_message
            )
        )

        # =================================================
        # GENERATE RAG RESPONSE
        # =================================================

        rag_result = (
            RAGService.query_knowledge_base(

                question=latest_message,

                conversation_memory=(
                    context_data.get(
                        "conversation_memory",
                        ""
                    )
                ),

                workflow_context=(
                    context_data.get(
                        "workflow_context",
                        ""
                    )
                ),

                workflow_guidance=(
                    context_data.get(
                        "workflow_guidance",
                        ""
                    )
                ),

                workflow_actions=(
                    context_data.get(
                        "workflow_actions",
                        ""
                    )
                ),

                workflow_lifecycle_context=(
                    context_data.get(
                        "workflow_lifecycle_context",
                        ""
                    )
                ),

                historical_memory=(
                    context_data.get(
                        "historical_memory",
                        ""
                    )
                ),

                next_troubleshooting_action=(
                    context_data.get(
                        "next_troubleshooting_action",
                        ""
                    )
                ),

                response_rules=(
                    context_data.get(
                        "response_rules",
                        ""
                    )
                )
            )
        )

        ai_response = (
            rag_result["answer"]
        )

        # =================================================
        # STORE AI MESSAGE
        # =================================================

        ai_message_data = {

            "ticket_id":
            ticket_id,

            "sender":
            "ai",

            "message":
            ai_response
        }

        saved_message = (
            ConversationRepository.create_message(
                db,
                ai_message_data
            )
        )

        # =================================================
        # SUMMARY GENERATION
        # =================================================

        ConversationService.generate_summary_if_needed(
            db=db,
            ticket_id=ticket_id
        )

        # =================================================
        # WORKFLOW LOGGING
        # =================================================

        WorkflowService.log_action(
            db=db,
            ticket_id=ticket_id,
            action="AI_RESPONSE_GENERATED",
            details=(
                "AI generated workflow-aware response"
            )
        )

        return saved_message

    # =====================================================
    # AUTO SUMMARY GENERATION
    # =====================================================

    @staticmethod
    def generate_summary_if_needed(
        db: Session,
        ticket_id: int
    ):

        messages = (
            ConversationRepository.get_ticket_messages(
                db,
                ticket_id
            )
        )

        workflow_state = (
            WorkflowStateService.get_workflow_state(
                db,
                ticket_id
            )
        )

        should_summarize = (

            len(messages)
            >=
            ConversationService
            .SUMMARY_TRIGGER_COUNT
        )

        lifecycle_trigger = False

        if workflow_state:

            if workflow_state.status in [

                "resolved",
                "escalated"

            ]:

                lifecycle_trigger = True

        if (
            should_summarize
            or
            lifecycle_trigger
        ):

            SummaryService.generate_ticket_summary(
                db=db,
                ticket_id=ticket_id
            )