from app.ml.inference.priority_inference import (
    predict_ticket_priority
)

class PriorityService:

    @staticmethod
    def predict_priority(ticket_text: str) -> dict:
        """
        Predict ticket priority using ML model.
        """

        predicted_priority = predict_ticket_priority(
            ticket_text
        )

        return {
            "success": True,
            "priority": predicted_priority
        }