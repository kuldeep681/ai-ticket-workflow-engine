from app.ml.inference.routing_inference import (
    predict_ticket_department
)

class RoutingService:

    @staticmethod
    def predict_department(ticket_text: str) -> dict:
        """
        Predict support department using ML model.
        """

        predicted_department = (
            predict_ticket_department(ticket_text)
        )

        return {
            "success": True,
            "department": predicted_department
        }