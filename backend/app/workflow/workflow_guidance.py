# =========================================================
# WORKFLOW STEP GUIDANCE
# =========================================================

WORKFLOW_GUIDANCE = {

    # =====================================================
    # VPN SUPPORT
    # =====================================================

    "vpn_support": {

        "authentication_check": """
Guide the user through VPN authentication troubleshooting.

Focus on:
- authentication failures
- invalid credentials
- expired VPN tokens
- VPN client validation
- connectivity verification

Ensure the user verifies:
- VPN username
- active VPN account
- correct VPN gateway/server
""",

        "token_regeneration": """
Guide the user through VPN token regeneration.

Focus on:
- generating a replacement token
- reconnecting VPN client
- validating token synchronization
- retrying authentication

Do NOT switch into password recovery workflows unless explicitly requested.
""",

        "connection_test": """
Guide the user through VPN connection validation.

Focus on:
- successful VPN reconnection
- internal resource access
- corporate portal accessibility
- DNS/internal routing validation

Ask the user to confirm whether internal systems are reachable.
"""
    },

    # =====================================================
    # PASSWORD SUPPORT
    # =====================================================

    "password_support": {

        "identity_verification": """
Guide the user through identity verification.

Focus on:
- employee identity confirmation
- verification codes
- account ownership validation
- MFA validation if required

Do NOT expose sensitive credential information.
""",

        "password_reset": """
Guide the user through secure password reset.

Focus on:
- password reset procedures
- password complexity requirements
- secure credential handling
- account unlock validation

Recommend testing login after password update.
""",

        "login_validation": """
Guide the user through login validation.

Focus on:
- successful authentication
- account access verification
- MFA confirmation
- session validation
"""
    },

    # =====================================================
    # MFA SUPPORT
    # =====================================================

    "mfa_support": {

        "mfa_validation": """
Guide the user through MFA troubleshooting.

Focus on:
- OTP validation
- authenticator synchronization
- time drift correction
- MFA device verification
- backup code validation
""",

        "mfa_reset": """
Guide the user through MFA reset procedures.

Focus on:
- resetting MFA enrollment
- re-registering authenticator devices
- validating new MFA configuration

Ensure identity verification is completed before MFA reset.
"""
    },

    # =====================================================
    # EMAIL SUPPORT
    # =====================================================

    "email_support": {

        "mailbox_diagnostics": """
Guide the user through mailbox diagnostics.

Focus on:
- send/receive validation
- mailbox accessibility
- Outlook client validation
- mailbox quota checks
- connectivity verification
""",

        "sync_diagnostics": """
Guide the user through email synchronization troubleshooting.

Focus on:
- Outlook synchronization
- delayed email delivery
- mailbox refresh
- cached mailbox issues
- Exchange connectivity
""",

        "mailbox_recovery": """
Guide the user through mailbox recovery.

Focus on:
- restoring mailbox connectivity
- repairing Outlook profile
- validating Exchange access
- restarting synchronization services
"""
    },

    # =====================================================
    # NETWORK SUPPORT
    # =====================================================

    "network_support": {

        "network_diagnostics": """
Guide the user through network diagnostics.

Focus on:
- internet connectivity
- WiFi status
- DNS resolution
- latency testing
- gateway reachability
- local network validation
""",

        "router_validation": """
Guide the user through router/network equipment validation.

Focus on:
- router restart
- cabling verification
- access point connectivity
- signal strength validation
""",

        "connectivity_test": """
Guide the user through connectivity testing.

Focus on:
- ping testing
- DNS testing
- website accessibility
- VPN coexistence validation
"""
    },

    # =====================================================
    # ACCESS SUPPORT
    # =====================================================

    "access_support": {

        "permission_validation": """
Guide the user through access validation.

Focus on:
- permission verification
- role-based access validation
- shared drive access
- application authorization
- account entitlement checks
""",

        "access_request_review": """
Guide the user through access request validation.

Focus on:
- manager approval validation
- role justification
- access policy compliance
- least privilege principles
"""
    },

    # =====================================================
    # SOFTWARE SUPPORT
    # =====================================================

    "software_support": {

        "application_diagnostics": """
Guide the user through software diagnostics.

Focus on:
- application startup failures
- crash diagnostics
- dependency validation
- update verification
- compatibility issues
""",

        "installation_validation": """
Guide the user through installation troubleshooting.

Focus on:
- installer validation
- administrative permissions
- missing dependencies
- installation logs
- software compatibility
""",

        "application_recovery": """
Guide the user through application recovery.

Focus on:
- reinstall procedures
- configuration reset
- cache cleanup
- update verification
"""
    },

    # =====================================================
    # HARDWARE SUPPORT
    # =====================================================

    "hardware_support": {

        "hardware_diagnostics": """
Guide the user through hardware diagnostics.

Focus on:
- device startup behavior
- peripheral connectivity
- overheating symptoms
- power validation
- hardware fault indicators
""",

        "device_validation": """
Guide the user through device validation.

Focus on:
- keyboard/mouse testing
- monitor connectivity
- docking station validation
- battery/power checks
""",

        "hardware_recovery": """
Guide the user through hardware recovery procedures.

Focus on:
- restart procedures
- BIOS/device checks
- reconnecting peripherals
- hardware escalation indicators
"""
    },

    # =====================================================
    # PRINTER SUPPORT
    # =====================================================

    "printer_support": {

        "printer_diagnostics": """
Guide the user through printer diagnostics.

Focus on:
- printer connectivity
- print queue status
- paper jams
- toner/ink validation
- printer availability
""",

        "printer_recovery": """
Guide the user through printer recovery.

Focus on:
- restarting printer services
- reconnecting printer
- clearing print queues
- validating network printer access
"""
    },

    # =====================================================
    # SECURITY SUPPORT
    # =====================================================

    "security_support": {

        "security_validation": """
Guide the user through security incident validation.

Focus on:
- suspicious activity verification
- phishing confirmation
- malware indicators
- endpoint security alerts
- unauthorized access attempts

Advise caution before interacting with suspicious content.
""",

        "incident_containment": """
Guide the user through basic containment procedures.

Focus on:
- disconnecting affected devices if necessary
- avoiding suspicious links/files
- notifying security teams
- preserving incident evidence
"""
    }

}