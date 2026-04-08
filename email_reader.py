import imaplib
import email
import os


EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")


def fetch_unread_emails():
    emails = []

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")

        if status != "OK":
            return []

        for num in messages[0].split():
            status, msg_data = mail.fetch(num, "(RFC822)")

            if status != "OK":
                continue

            msg = email.message_from_bytes(msg_data[0][1])

            subject = msg["subject"]

            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            emails.append({
                "subject": subject,
                "body": body
            })

        mail.logout()

    except Exception as e:
        print("Email fetch error:", e)
        return []

    return emails