# =========================================================
# DETERMINISTIC WORKFLOW TRANSITION GRAPH
# =========================================================

WORKFLOW_TRANSITIONS = {

    # =====================================================
    # VPN SUPPORT
    # =====================================================

    "vpn_support": {

        "authentication_check": [
            "token_regeneration",
            "connection_test",
            "escalated"
        ],

        "token_regeneration": [
            "connection_test",
            "escalated"
        ],

        "connection_test": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # PASSWORD SUPPORT
    # =====================================================

    "password_support": {

        "identity_verification": [
            "password_reset",
            "escalated"
        ],

        "password_reset": [
            "login_validation",
            "escalated"
        ],

        "login_validation": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # MFA SUPPORT
    # =====================================================

    "mfa_support": {

        "mfa_validation": [
            "mfa_reset",
            "resolved",
            "escalated"
        ],

        "mfa_reset": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # EMAIL SUPPORT
    # =====================================================

    "email_support": {

        "mailbox_diagnostics": [
            "sync_diagnostics",
            "mailbox_recovery",
            "escalated"
        ],

        "sync_diagnostics": [
            "mailbox_recovery",
            "resolved",
            "escalated"
        ],

        "mailbox_recovery": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # NETWORK SUPPORT
    # =====================================================

    "network_support": {

        "network_diagnostics": [
            "router_validation",
            "connectivity_test",
            "escalated"
        ],

        "router_validation": [
            "connectivity_test",
            "escalated"
        ],

        "connectivity_test": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # ACCESS SUPPORT
    # =====================================================

    "access_support": {

        "permission_validation": [
            "access_request_review",
            "resolved",
            "escalated"
        ],

        "access_request_review": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # SOFTWARE SUPPORT
    # =====================================================

    "software_support": {

        "application_diagnostics": [
            "installation_validation",
            "application_recovery",
            "escalated"
        ],

        "installation_validation": [
            "application_recovery",
            "resolved",
            "escalated"
        ],

        "application_recovery": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # HARDWARE SUPPORT
    # =====================================================

    "hardware_support": {

        "hardware_diagnostics": [
            "device_validation",
            "hardware_recovery",
            "escalated"
        ],

        "device_validation": [
            "hardware_recovery",
            "resolved",
            "escalated"
        ],

        "hardware_recovery": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # PRINTER SUPPORT
    # =====================================================

    "printer_support": {

        "printer_diagnostics": [
            "printer_recovery",
            "escalated"
        ],

        "printer_recovery": [
            "resolved",
            "escalated"
        ]
    },

    # =====================================================
    # SECURITY SUPPORT
    # =====================================================

    "security_support": {

        "security_validation": [
            "incident_containment",
            "escalated"
        ],

        "incident_containment": [
            "resolved",
            "escalated"
        ]
    }
}

# =========================================================
# TERMINAL STATES
# =========================================================

TERMINAL_STATES = [

    "resolved",
    "escalated"
]