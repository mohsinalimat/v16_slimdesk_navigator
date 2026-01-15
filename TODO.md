# SlimDesk Navigator TODO

## Backlog
- [ ] 

## In Progress
- [ ] **Feature: Restore Defaults Button**
    - **Goal:** Allow users to reset sidebar to original state (all auto-discovered workspaces).
    - **Use Case:** User accidentally removes all items or wants to start fresh.
    - **Implementation:** Add button to "Customize" dialog that clears user config and re-fetches defaults.

## Completed
- [x] **Bug: Icons Unresponsive after System Reload** (v3.41) **Bug: Icons Stop Working after System Reload**
    - **Scenario:** Changing system settings triggers a Frappe "Reload" modal. After this reload, SlimDesk icons become unresponsive or disappear.
    - **Workaround:** Navigating to Desk URL + Hard Refresh restores functionality.
    - **Suspect:** Initialization logic doesn't re-trigger correctly after a soft `frappe.ui.reload` or DOM replacement. 

## Completed
- [x] v3.40 Public Release
