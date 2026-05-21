# =========================================================
# WORKFLOW ACTION RULES
# =========================================================

WORKFLOW_ACTIONS = {

    # =====================================================
    # VPN SUPPORT
    # =====================================================

    "vpn_support": {

        "authentication_check": {

            "allowed_actions": [
                "verify vpn credentials",
                "check token validity",
                "validate vpn connectivity",
                "confirm authentication status",
                "verify vpn client configuration"
            ],

            "forbidden_topics": [
                "password reset",
                "credential recovery",
                "email troubleshooting",
                "unrelated account changes"
            ],

            "expected_goal":
            "Validate VPN authentication and connectivity state."
        },

        "token_regeneration": {

            "allowed_actions": [
                "generate new vpn token",
                "request replacement token",
                "replace expired token",
                "reconnect vpn client",
                "validate regenerated token"
            ],

            "forbidden_topics": [
                "password reset",
                "credential recovery",
                "account recovery",
                "mailbox troubleshooting"
            ],

            "expected_goal":
            "Successfully regenerate and validate VPN token."
        },

        "connection_test": {

            "allowed_actions": [
                "test vpn connection",
                "verify internal access",
                "confirm successful authentication",
                "validate internal resource access"
            ],

            "forbidden_topics": [
                "password reset",
                "credential recovery"
            ],

            "expected_goal":
            "Verify VPN functionality after troubleshooting."
        }
    },

    # =====================================================
    # PASSWORD SUPPORT
    # =====================================================

    "password_support": {

        "identity_verification": {

            "allowed_actions": [
                "verify user identity",
                "validate otp",
                "confirm account ownership",
                "validate security verification"
            ],

            "forbidden_topics": [
                "vpn troubleshooting",
                "network diagnostics"
            ],

            "expected_goal":
            "Verify user identity securely."
        },

        "password_reset": {

            "allowed_actions": [
                "reset account password",
                "update credentials",
                "verify new password",
                "unlock user account"
            ],

            "forbidden_topics": [
                "vpn token regeneration",
                "network troubleshooting"
            ],

            "expected_goal":
            "Restore account login access."
        },

        "login_validation": {

            "allowed_actions": [
                "test login",
                "validate authentication",
                "verify account access",
                "confirm successful sign in"
            ],

            "forbidden_topics": [
                "vpn troubleshooting"
            ],

            "expected_goal":
            "Validate successful authentication."
        }
    },

    # =====================================================
    # MFA SUPPORT
    # =====================================================

    "mfa_support": {

        "mfa_validation": {

            "allowed_actions": [
                "validate otp",
                "verify authenticator app",
                "check time synchronization",
                "validate backup codes",
                "confirm device registration"
            ],

            "forbidden_topics": [
                "password reset",
                "hardware diagnostics"
            ],

            "expected_goal":
            "Validate MFA authentication functionality."
        },

        "mfa_reset": {

            "allowed_actions": [
                "reset mfa enrollment",
                "re-register authenticator",
                "remove old device",
                "validate new mfa setup"
            ],

            "forbidden_topics": [
                "password recovery",
                "vpn troubleshooting"
            ],

            "expected_goal":
            "Restore MFA authentication access."
        }
    },

    # =====================================================
    # EMAIL SUPPORT
    # =====================================================

    "email_support": {

        "mailbox_diagnostics": {

            "allowed_actions": [
                "test send receive",
                "validate mailbox connectivity",
                "check mailbox quota",
                "verify outlook connectivity",
                "validate exchange access"
            ],

            "forbidden_topics": [
                "vpn token regeneration",
                "security policy modification"
            ],

            "expected_goal":
            "Identify mailbox or email delivery issue."
        },

        "sync_diagnostics": {

            "allowed_actions": [
                "refresh mailbox",
                "validate outlook sync",
                "check exchange synchronization",
                "restart sync services"
            ],

            "forbidden_topics": [
                "password recovery"
            ],

            "expected_goal":
            "Restore mailbox synchronization."
        },

        "mailbox_recovery": {

            "allowed_actions": [
                "repair outlook profile",
                "restart outlook",
                "rebuild mailbox cache",
                "restore mailbox connectivity"
            ],

            "forbidden_topics": [
                "vpn troubleshooting"
            ],

            "expected_goal":
            "Recover mailbox functionality."
        }
    },

    # =====================================================
    # NETWORK SUPPORT
    # =====================================================

    "network_support": {

        "network_diagnostics": {

            "allowed_actions": [
                "check internet connectivity",
                "validate dns resolution",
                "test network latency",
                "verify gateway access",
                "test wifi stability"
            ],

            "forbidden_topics": [
                "password reset",
                "account recovery"
            ],

            "expected_goal":
            "Diagnose network connectivity issue."
        },

        "router_validation": {

            "allowed_actions": [
                "restart router",
                "check cabling",
                "validate wifi signal",
                "verify access point connectivity"
            ],

            "forbidden_topics": [
                "credential reset"
            ],

            "expected_goal":
            "Validate local network infrastructure."
        },

        "connectivity_test": {

            "allowed_actions": [
                "ping external resources",
                "validate dns responses",
                "test internet access",
                "validate stable connectivity"
            ],

            "forbidden_topics": [
                "password recovery"
            ],

            "expected_goal":
            "Confirm restored network connectivity."
        }
    },

    # =====================================================
    # ACCESS SUPPORT
    # =====================================================

    "access_support": {

        "permission_validation": {

            "allowed_actions": [
                "validate permissions",
                "check role assignments",
                "verify access groups",
                "validate authorization policies"
            ],

            "forbidden_topics": [
                "security bypass",
                "unauthorized privilege escalation"
            ],

            "expected_goal":
            "Validate user access permissions."
        },

        "access_request_review": {

            "allowed_actions": [
                "review access request",
                "validate approval",
                "confirm business justification"
            ],

            "forbidden_topics": [
                "policy bypass"
            ],

            "expected_goal":
            "Review and validate access request."
        }
    },

    # =====================================================
    # SOFTWARE SUPPORT
    # =====================================================

    "software_support": {

        "application_diagnostics": {

            "allowed_actions": [
                "check application logs",
                "verify software version",
                "validate dependencies",
                "test application startup"
            ],

            "forbidden_topics": [
                "security bypass",
                "unauthorized installations"
            ],

            "expected_goal":
            "Diagnose application failure."
        },

        "installation_validation": {

            "allowed_actions": [
                "validate installer",
                "check permissions",
                "verify compatibility",
                "review installation logs"
            ],

            "forbidden_topics": [
                "unsupported software installation"
            ],

            "expected_goal":
            "Validate software installation process."
        },

        "application_recovery": {

            "allowed_actions": [
                "reinstall application",
                "clear cache",
                "reset configuration",
                "validate software updates"
            ],

            "forbidden_topics": [
                "credential recovery"
            ],

            "expected_goal":
            "Restore software functionality."
        }
    },

    # =====================================================
    # HARDWARE SUPPORT
    # =====================================================

    "hardware_support": {

        "hardware_diagnostics": {

            "allowed_actions": [
                "check power status",
                "validate peripherals",
                "review hardware symptoms",
                "check overheating indicators"
            ],

            "forbidden_topics": [
                "firmware modification",
                "unauthorized hardware replacement"
            ],

            "expected_goal":
            "Diagnose hardware issue."
        },

        "device_validation": {

            "allowed_actions": [
                "test keyboard",
                "test monitor",
                "verify docking station",
                "check battery health"
            ],

            "forbidden_topics": [
                "credential reset"
            ],

            "expected_goal":
            "Validate device functionality."
        },

        "hardware_recovery": {

            "allowed_actions": [
                "restart device",
                "reconnect peripherals",
                "perform hardware checks",
                "prepare escalation if necessary"
            ],

            "forbidden_topics": [
                "security bypass"
            ],

            "expected_goal":
            "Recover hardware operation."
        }
    },

    # =====================================================
    # PRINTER SUPPORT
    # =====================================================

    "printer_support": {

        "printer_diagnostics": {

            "allowed_actions": [
                "check printer connectivity",
                "validate print queue",
                "review printer status",
                "check toner and paper"
            ],

            "forbidden_topics": [
                "credential recovery"
            ],

            "expected_goal":
            "Diagnose printer issue."
        },

        "printer_recovery": {

            "allowed_actions": [
                "restart printer",
                "clear print queue",
                "reconnect printer",
                "validate printer network access"
            ],

            "forbidden_topics": [
                "network policy modification"
            ],

            "expected_goal":
            "Restore printer functionality."
        }
    },

    # =====================================================
    # SECURITY SUPPORT
    # =====================================================

    "security_support": {

        "security_validation": {

            "allowed_actions": [
                "validate security alert",
                "review suspicious activity",
                "identify phishing indicators",
                "review endpoint alerts"
            ],

            "forbidden_topics": [
                "disable antivirus",
                "ignore security controls",
                "bypass enterprise policies"
            ],

            "expected_goal":
            "Validate security incident safely."
        },

        "incident_containment": {

            "allowed_actions": [
                "disconnect affected system",
                "preserve evidence",
                "notify security team",
                "limit system exposure"
            ],

            "forbidden_topics": [
                "delete evidence",
                "disable monitoring systems"
            ],

            "expected_goal":
            "Contain potential security incident."
        }
    }

}