from app.workflow.workflow_actions import (
    WORKFLOW_ACTIONS
)

from app.workflow.workflow_transitions import (
    WORKFLOW_TRANSITIONS,
    TERMINAL_STATES
)


class TroubleshootingEngine:

    # =====================================================
    # BUILD EXECUTION POLICY
    # =====================================================

    @staticmethod
    def get_execution_data(
        workflow_type: str,
        current_step: str
    ):

        workflow_data = (
            WORKFLOW_ACTIONS.get(
                workflow_type,
                {}
            )
        )

        step_data = (
            workflow_data.get(
                current_step,
                {}
            )
        )

        transitions = (
            WORKFLOW_TRANSITIONS.get(
                workflow_type,
                {}
            )
        )

        available_transitions = (
            transitions.get(
                current_step,
                []
            )
        )

        next_step = None

        for step in available_transitions:

            if step not in TERMINAL_STATES:

                next_step = step
                break

        return {

            "objective":
            step_data.get(
                "expected_goal",
                ""
            ),

            "instructions":
            step_data.get(
                "allowed_actions",
                []
            ),

            "forbidden_topics":
            step_data.get(
                "forbidden_topics",
                []
            ),

            "next_step":
            next_step,

            "available_transitions":
            available_transitions
        }

    # =====================================================
    # DETERMINE EXECUTION MODE
    # =====================================================

    @staticmethod
    def determine_next_action(
        workflow_state
    ):

        # =================================================
        # RESOLVED
        # =================================================

        if workflow_state.status == "resolved":

            return {

                "mode": "resolved",

                "objective":
                "Confirm issue resolution briefly.",

                "response_rules": [

                    "confirm resolution briefly",
                    "do not continue troubleshooting",
                    "do not introduce new steps",
                    "offer additional help only"
                ]
            }

        # =================================================
        # ESCALATED
        # =================================================

        if workflow_state.status == "escalated":

            return {

                "mode": "escalated",

                "objective":
                "Recommend escalation.",

                "response_rules": [

                    "stop troubleshooting",
                    "recommend enterprise escalation",
                    "do not provide advanced remediation"
                ]
            }

        # =================================================
        # AWAITING USER
        # =================================================

        if workflow_state.status == "awaiting_user":

            return {

                "mode": "awaiting_user",

                "objective":
                "Wait for user validation.",

                "response_rules": [

                    "wait for user testing",
                    "do not continue troubleshooting"
                ]
            }

        # =================================================
        # ACTIVE EXECUTION
        # =================================================

        execution_data = (
            TroubleshootingEngine
            .get_execution_data(
                workflow_state.workflow_type,
                workflow_state.current_step
            )
        )

        return {

            "mode": "execution",

            "objective":
            execution_data["objective"],

            "instructions":
            execution_data["instructions"],

            "forbidden_topics":
            execution_data["forbidden_topics"],

            "next_step":
            execution_data["next_step"],

            "available_transitions":
            execution_data[
                "available_transitions"
            ],

            "response_rules": [

                "stay inside workflow",
                "be concise",
                "be operational",
                "avoid speculation",
                "avoid unrelated troubleshooting",
                "avoid generic explanations"
            ]
        }