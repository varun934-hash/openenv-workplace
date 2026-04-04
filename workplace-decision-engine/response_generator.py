def generate_response(task):
    desc = task.description.lower()

    if "login" in desc:
        return "Your issue has been escalated. Our support team will contact you shortly."

    elif "refund" in desc:
        return "Your refund has been successfully processed."

    elif "meeting" in desc:
        return "Your meeting has been scheduled successfully."

    else:
        return "Your request has been received and is being processed."