from app.services.workflow_state_service import (
    WorkflowStateService
)

from app.repositories.conversation_repository import (
    ConversationRepository
)

from app.services.workflow_memory_service import (
    WorkflowMemoryService
)

from app.workflow.workflow_guidance import (
    WORKFLOW_GUIDANCE
)

from app.workflow.troubleshooting_engine import (
    TroubleshootingEngine
)


class WorkflowContextBuilder:

    @staticmethod
    def build_context(
        db,
        ticket_id: int,
        question: str
    ):

        workflow_state = (
            WorkflowStateService
            .get_workflow_state(
                db,
                ticket_id
            )
        )

        if not workflow_state:

            return {

                "conversation_memory": "",
                "workflow_context": "",
                "workflow_guidance": "",
                "workflow_actions": "",
                "workflow_lifecycle_context": "",
                "historical_memory": "",
                "next_troubleshooting_action": "",
                "response_rules": ""
            }

        # =================================================
        # CONVERSATION MEMORY
        # =================================================

        messages = (
            ConversationRepository
            .get_ticket_messages(
                db,
                ticket_id
            )
        )

        memory_lines = []

        for message in messages[-6:]:

            memory_lines.append(
                f"{message.sender}: "
                f"{message.message}"
            )

        conversation_memory = "\n".join(
            memory_lines
        )

        # =================================================
        # GUIDANCE
        # =================================================

        workflow_guidance = (
            WORKFLOW_GUIDANCE
            .get(
                workflow_state.workflow_type,
                {}
            )
            .get(
                workflow_state.current_step,
                ""
            )
        )

        # =================================================
        # EXECUTION DATA
        # =================================================

        execution_data = (
            TroubleshootingEngine
            .determine_next_action(
                workflow_state
            )
        )

        workflow_actions = "\n".join(

            execution_data.get(
                "instructions",
                []
            )
        )

        response_rules = "\n".join(

            execution_data.get(
                "response_rules",
                []
            )
        )

        # =================================================
        # MEMORY
        # =================================================

        historical_memory = (
            WorkflowMemoryService
            .get_historical_memories(
                db,
                workflow_state.workflow_type,
                workflow_state.current_issue
            )
        )

        workflow_context = f"""
Workflow Type:
{workflow_state.workflow_type}

Current Step:
{workflow_state.current_step}

Workflow Status:
{workflow_state.status}

Current Issue:
{workflow_state.current_issue}
"""

        return {

            "conversation_memory":
            conversation_memory,

            "workflow_context":
            workflow_context,

            "workflow_guidance":
            workflow_guidance,

            "workflow_actions":
            workflow_actions,

            "workflow_lifecycle_context":
            workflow_state.status,

            "historical_memory":
            historical_memory,

            "next_troubleshooting_action":
            execution_data.get(
                "objective",
                ""
            ),

            "response_rules":
            response_rules
        }