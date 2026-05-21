from app.services.ollama_service import (
    OllamaService
)


class ConversationSummarizer:

    # ==========================================
    # GENERATE CONVERSATION SUMMARY
    # ==========================================

    @staticmethod
    def summarize_conversation(
        conversation_text: str
    ):

        prompt = f"""
You are an enterprise IT workflow summarizer.

Summarize the troubleshooting conversation clearly and concisely.

Focus on:
- issue reported
- troubleshooting steps performed
- workflow progress
- unresolved problems
- current status

Keep summary short but informative.

================ CONVERSATION ================

{conversation_text}

================ SUMMARY ================
"""

        summary = (
            OllamaService.generate_response(
                prompt
            )
        )

        return summary