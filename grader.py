def grade(task, action):
    desc = task.description.lower()

    if "refund" in desc and action.action_type == "complete":
        return 0.8
    elif "meeting" in desc and action.action_type == "schedule":
        return 0.7
    elif "email" in desc and action.action_type == "respond":
        return 0.6
    elif "complaint" in desc and action.action_type == "complete":
        return 0.9

    # wrong action
    return 0.3