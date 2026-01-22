import frappe
import json

@frappe.whitelist()
def save_config(workspaces):
    """
    Save the user's sidebar configuration.
    workspaces: List of strings (workspace names)
    """
    if isinstance(workspaces, str):
        try:
            workspaces = json.loads(workspaces)
        except:
            pass
    
    # If None, clear the default
    if workspaces is None:
        frappe.defaults.clear_user_default("slim_desk_config")
        return "cleared"

    # Ensure it's a list
    if not isinstance(workspaces, list):
        frappe.throw("Invalid workspace list")

    # Save as User Default
    frappe.defaults.set_user_default("slim_desk_config", json.dumps(workspaces))
    
    return "saved"

@frappe.whitelist()
def reset_config():
    """
    Resets the sidebar configuration to system defaults.
    """
    frappe.defaults.clear_user_default("slim_desk_config")
    return "reset"
