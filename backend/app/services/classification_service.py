from app.ml.inference.classifier_inference import (
    predict_ticket_category
)

class ClassificationService:

    @staticmethod
    def classify_ticket(ticket_text: str) -> dict:
        """
        Classify ticket using ML model.
        """

        predicted_category = predict_ticket_category(ticket_text)

        return {
            "success": True,
            "category": predicted_category
        }