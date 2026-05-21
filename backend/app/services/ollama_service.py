import re
import requests

from app.core.config import settings


class OllamaService:

    @staticmethod
    def clean_response(text: str):

        # Remove markdown stars
        text = text.replace("**", "")

        # Remove placeholder patterns
        text = re.sub(r"\[.*?\]", "", text)

        # Remove email-style greetings
        forbidden_phrases = [
            "Dear User",
            "Dear Customer",
            "Subject:",
            "Sincerely,",
            "Best regards,",
            "Thank you and have a great day!",
        ]

        for phrase in forbidden_phrases:
            text = text.replace(phrase, "")

        # Remove extra blank lines
        text = re.sub(r"\n\s*\n", "\n\n", text)

        return text.strip()

    @staticmethod
    def generate_response(prompt: str):

        payload = {
            "model": settings.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.4,
                "num_predict": 180,
                "repeat_penalty": 1.2
            }
        }

        response = requests.post(
            settings.OLLAMA_URL,
            json=payload
        )

        data = response.json()

        raw_response = data.get("response", "")

        cleaned_response = (
            OllamaService.clean_response(
                raw_response
            )
        )

        return cleaned_response