def grade(task, action):
    desc = task.description.lower()

    # correct actions
    if "refund" in desc and action.action_type == "complete":
        return 0.8
    elif "meeting" in desc and action.action_type == "schedule":
        return 0.7
    elif "complaint" in desc and action.action_type == "complete":
        return 0.9
    elif "email" in desc and action.action_type == "respond":
        return 0.6

    # wrong actions → small score (NOT 0)
    return 0.2