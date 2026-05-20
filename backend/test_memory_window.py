from app.memory.memory_window import (
    get_recent_messages,
    format_memory_context
)

messages = [
    {"sender": "user", "message": "VPN issue"},
    {"sender": "ai", "message": "Check token"},
    {"sender": "user", "message": "Token expired"},
    {"sender": "ai", "message": "Regenerate token"},
    {"sender": "user", "message": "Still failing"},
    {"sender": "ai", "message": "Check network"},
    {"sender": "user", "message": "Network works"},
]

recent = get_recent_messages(messages)

formatted = format_memory_context(recent)

print(formatted)