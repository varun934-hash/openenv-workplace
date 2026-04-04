<<<<<<< HEAD
def generate_response(task):
    desc = task.description.lower()

    if "login" in desc:
        return "Your issue has been escalated. Our support team will contact you shortly."

    elif "refund" in desc:
        return "Your refund has been successfully processed."

    elif "meeting" in desc:
        return "Your meeting has been scheduled successfully."

    else:
=======
def generate_response(task):
    desc = task.description.lower()

    if "login" in desc:
        return "Your issue has been escalated. Our support team will contact you shortly."

    elif "refund" in desc:
        return "Your refund has been successfully processed."

    elif "meeting" in desc:
        return "Your meeting has been scheduled successfully."

    else:
>>>>>>> 0c94d1aa3ad327c92e2fbd0af7b279095d94b96a
        return "Your request has been received and is being processed."