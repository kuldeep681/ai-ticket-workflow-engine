# =========================================================
# GENERIC ENTERPRISE WORKFLOW DETECTION RULES
# =========================================================

WORKFLOW_RULES = [

    # =====================================================
    # VPN SUPPORT
    # =====================================================

    {
        "workflow_type": "vpn_support",

        "keywords": [

            "vpn",
            "vpn issue",
            "vpn not working",
            "vpn disconnected",
            "cannot connect vpn",
            "vpn failed",
            "vpn timeout",
            "vpn token",
            "token expired",
            "invalid token",
            "vpn authentication",
            "vpn access denied",
            "vpn login failed",
            "vpn client",
            "vpn reconnect",
            "corporate vpn",
            "vpn gateway",
            "vpn server",
            "secure connection",
            "remote access"

        ],

        "current_issue":
        "vpn_connectivity_issue",

        "current_step":
        "authentication_check"
    },

    # =====================================================
    # PASSWORD SUPPORT
    # =====================================================

    {
        "workflow_type": "password_support",

        "keywords": [

            "forgot password",
            "password reset",
            "reset password",
            "password expired",
            "cannot login",
            "login failed",
            "account locked",
            "invalid password",
            "wrong password",
            "password not working",
            "signin failed",
            "credential issue",
            "credentials rejected",
            "unable to login",
            "login problem",
            "authentication failed",
            "password issue",
            "unlock account",
            "account disabled"

        ],

        "current_issue":
        "password_access_issue",

        "current_step":
        "identity_verification"
    },

    # =====================================================
    # MFA SUPPORT
    # =====================================================

    {
        "workflow_type": "mfa_support",

        "keywords": [

            "mfa failed",
            "otp not received",
            "otp expired",
            "2fa failed",
            "verification code invalid",
            "authenticator issue",
            "authenticator app",
            "mfa issue",
            "verification failed",
            "code not working",
            "multi factor authentication",
            "two factor authentication",
            "microsoft authenticator",
            "google authenticator",
            "otp issue",
            "security code",
            "verification code",
            "mfa reset",
            "authentication code"

        ],

        "current_issue":
        "mfa_authentication_issue",

        "current_step":
        "mfa_validation"
    },

    # =====================================================
    # EMAIL SUPPORT
    # =====================================================

    {
        "workflow_type": "email_support",

        "keywords": [

            "email",
            "mail",
            "outlook",
            "exchange",
            "mailbox",
            "inbox",
            "email sync",
            "syncing emails",
            "mail sync",
            "mailbox sync",
            "outlook sync",
            "exchange sync",
            "calendar sync",
            "contacts sync",
            "email not working",
            "mail not working",
            "cannot send email",
            "cannot receive email",
            "cannot send mail",
            "cannot receive mail",
            "email delayed",
            "mail delayed",
            "outlook issue",
            "outlook crashing",
            "outlook crashed",
            "outlook keeps crashing",
            "email login failed",
            "mailbox full",
            "exchange issue",
            "outlook disconnected",
            "mailbox unavailable",
            "outlook offline",
            "email connectivity"

        ],

        "current_issue":
        "email_service_issue",

        "current_step":
        "mailbox_diagnostics"
    },

    # =====================================================
    # NETWORK SUPPORT
    # =====================================================

    {
        "workflow_type": "network_support",

        "keywords": [

            "wifi not working",
            "internet down",
            "network unreachable",
            "dns issue",
            "slow network",
            "network disconnected",
            "packet loss",
            "high latency",
            "internet issue",
            "lan issue",
            "wifi disconnected",
            "internet not working",
            "connection timeout",
            "network issue",
            "router issue",
            "cannot access internet",
            "unstable connection",
            "weak wifi",
            "gateway unreachable",
            "dns failed"

        ],

        "current_issue":
        "network_connectivity_issue",

        "current_step":
        "network_diagnostics"
    },

    # =====================================================
    # ACCESS SUPPORT
    # =====================================================

    {
        "workflow_type": "access_support",

        "keywords": [

            "access denied",
            "permission denied",
            "cannot access",
            "unauthorized access",
            "missing permissions",
            "restricted access",
            "application access issue",
            "shared drive access",
            "folder access denied",
            "role issue",
            "permission issue",
            "authorization failed",
            "access request",
            "access problem",
            "access blocked",
            "group membership",
            "access rights",
            "authorization issue",
            "forbidden access"

        ],

        "current_issue":
        "access_control_issue",

        "current_step":
        "permission_validation"
    },

    # =====================================================
    # SOFTWARE SUPPORT
    # =====================================================

    {
        "workflow_type": "software_support",

        "keywords": [

            "application crashed",
            "software not opening",
            "app not responding",
            "installation failed",
            "software error",
            "update failed",
            "program crashed",
            "application error",
            "software issue",
            "application failed",
            "program not opening",
            "software crash",
            "app crash",
            "software update",
            "application freeze",
            "system error",
            "program error",
            "software installation",
            "compatibility issue"

        ],

        "current_issue":
        "software_application_issue",

        "current_step":
        "application_diagnostics"
    },

    # =====================================================
    # HARDWARE SUPPORT
    # =====================================================

    {
        "workflow_type": "hardware_support",

        "keywords": [

            "laptop not starting",
            "blue screen",
            "keyboard not working",
            "mouse not working",
            "monitor issue",
            "battery issue",
            "device overheating",
            "hardware failure",
            "screen flickering",
            "device issue",
            "pc not booting",
            "computer overheating",
            "hardware problem",
            "laptop issue",
            "display issue",
            "dock issue",
            "battery draining",
            "hardware crash",
            "device failure"

        ],

        "current_issue":
        "hardware_failure_issue",

        "current_step":
        "hardware_diagnostics"
    },

    # =====================================================
    # PRINTER SUPPORT
    # =====================================================

    {
        "workflow_type": "printer_support",

        "keywords": [

            "printer offline",
            "printer not printing",
            "paper jam",
            "printer error",
            "cannot print",
            "printer disconnected",
            "print queue stuck",
            "printer issue",
            "printing failed",
            "printer unavailable",
            "printer jam",
            "printer queue",
            "scanner issue",
            "print failed",
            "printer connectivity",
            "network printer",
            "printer problem"

        ],

        "current_issue":
        "printer_connectivity_issue",

        "current_step":
        "printer_diagnostics"
    },

    # =====================================================
    # SECURITY SUPPORT
    # =====================================================

    {
        "workflow_type": "security_support",

        "keywords": [

            "antivirus alert",
            "malware detected",
            "phishing email",
            "suspicious login",
            "security warning",
            "virus detected",
            "endpoint threat",
            "security issue",
            "ransomware",
            "infected device",
            "security breach",
            "unauthorized login",
            "malicious file",
            "threat detected",
            "security incident",
            "phishing attempt",
            "compromised account",
            "security alert"

        ],

        "current_issue":
        "security_incident_issue",

        "current_step":
        "security_validation"
    }

]