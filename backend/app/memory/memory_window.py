# backend/app/memory/memory_window.py

LAST_N_MESSAGES = 6


def get_recent_messages(messages, limit=LAST_N_MESSAGES):
    """
    Return only the most recent conversation messages.
    """

    if not messages:
        return []

    return messages[-limit:]


def format_memory_context(messages):
    """
    Convert messages into clean prompt-ready text.
    """

    formatted_lines = []

    for message in messages:

        sender = message.get("sender", "unknown").upper()
        content = message.get("message", "")

        formatted_lines.append(
            f"{sender}: {content}"
        )

    return "\n".join(formatted_lines)