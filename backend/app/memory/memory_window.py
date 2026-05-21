# =========================================================
# ENTERPRISE MEMORY WINDOW CONFIGURATION
# =========================================================

LAST_N_MESSAGES = 4

MAX_MESSAGE_LENGTH = 300

IGNORED_AI_PATTERNS = [

    "please ensure",
    "verify your internet connection",
    "restart your device",
    "contact your it department",
    "active directory synchronization",
    "vpn gateway status",
    "security monitoring portal",
    "internal outage notifications",
    "if the issue persists",
    "feel free to reach out"
]

# =========================================================
# FILTER LOW-VALUE MEMORY
# =========================================================

def is_low_value_message(
    sender: str,
    content: str
):

    content_lower = content.lower()

    # ==============================================
    # FILTER REPETITIVE AI TROUBLESHOOTING
    # ==============================================

    if sender.lower() == "ai":

        for pattern in IGNORED_AI_PATTERNS:

            if pattern in content_lower:

                return True

    # ==============================================
    # FILTER VERY SHORT MESSAGES
    # ==============================================

    if len(content.strip()) < 3:

        return True

    return False

# =========================================================
# CLEAN MESSAGE CONTENT
# =========================================================

def clean_message_content(
    content: str
):

    # ==============================================
    # REMOVE EXCESSIVE WHITESPACE
    # ==============================================

    cleaned = " ".join(
        content.split()
    )

    # ==============================================
    # TRIM VERY LONG RESPONSES
    # ==============================================

    if len(cleaned) > MAX_MESSAGE_LENGTH:

        cleaned = (
            cleaned[:MAX_MESSAGE_LENGTH]
            + "..."
        )

    return cleaned

# =========================================================
# GET RECENT FILTERED MESSAGES
# =========================================================

def get_recent_messages(
    messages,
    limit=LAST_N_MESSAGES
):

    """
    Return recent high-value conversational memory.
    """

    if not messages:

        return []

    filtered_messages = []

    # ==============================================
    # FILTER LOW-VALUE MEMORY
    # ==============================================

    for message in messages:

        sender = (
            message.get(
                "sender",
                "unknown"
            )
        )

        content = (
            message.get(
                "message",
                ""
            )
        )

        if is_low_value_message(
            sender,
            content
        ):

            continue

        cleaned_content = (
            clean_message_content(
                content
            )
        )

        filtered_messages.append({

            "sender":
            sender,

            "message":
            cleaned_content
        })

    # ==============================================
    # RETURN RECENT FILTERED MEMORY
    # ==============================================

    return filtered_messages[-limit:]

# =========================================================
# FORMAT MEMORY CONTEXT
# =========================================================

def format_memory_context(
    messages
):

    """
    Convert conversational memory into
    compact prompt-ready context.
    """

    formatted_lines = []

    for message in messages:

        sender = (
            message.get(
                "sender",
                "unknown"
            ).upper()
        )

        content = (
            message.get(
                "message",
                ""
            )
        )

        formatted_lines.append(
            f"{sender}: {content}"
        )

    return "\n".join(
        formatted_lines
    )