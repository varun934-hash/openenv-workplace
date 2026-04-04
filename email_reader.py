<<<<<<< HEAD
import imaplib
import email

EMAIL = "scalerhackathon@gmail.com"
PASSWORD = "xhxwllfrzmcikfzp"


def fetch_unread_emails():
    try:
        print("Connecting to Gmail...")

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)

        print("Login successful ✅")

        # Select inbox
        mail.select("INBOX")

        # 🔥 FETCH ALL EMAILS (NOT UNSEEN)
        status, messages = mail.search(None, "ALL")

        print("Search status:", status)
        print("Raw message IDs:", messages)

        email_list = []

        if status != "OK":
            print("Search failed ❌")
            return []

        mail_ids = messages[0].split()

        print("Total emails found:", len(mail_ids))

        # 🔥 GET LAST 5 EMAILS (IMPORTANT)
        for num in mail_ids[-5:]:
            status, data = mail.fetch(num, "(RFC822)")

            if status != "OK":
                continue

            msg = email.message_from_bytes(data[0][1])

            subject = str(msg["subject"])

            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
            else:
                try:
                    body = msg.get_payload(decode=True).decode()
                except:
                    pass

            email_list.append({
                "subject": subject,
                "body": body
            })

        mail.logout()

        print("Emails extracted:", email_list)

        return email_list

    except Exception as e:
        print("Email fetch error:", e)
=======
import imaplib
import email

EMAIL = "scalerhackathon@gmail.com"
PASSWORD = "xhxwllfrzmcikfzp"


def fetch_unread_emails():
    try:
        print("Connecting to Gmail...")

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)

        print("Login successful ✅")

        # Select inbox
        mail.select("INBOX")

        # 🔥 FETCH ALL EMAILS (NOT UNSEEN)
        status, messages = mail.search(None, "ALL")

        print("Search status:", status)
        print("Raw message IDs:", messages)

        email_list = []

        if status != "OK":
            print("Search failed ❌")
            return []

        mail_ids = messages[0].split()

        print("Total emails found:", len(mail_ids))

        # 🔥 GET LAST 5 EMAILS (IMPORTANT)
        for num in mail_ids[-5:]:
            status, data = mail.fetch(num, "(RFC822)")

            if status != "OK":
                continue

            msg = email.message_from_bytes(data[0][1])

            subject = str(msg["subject"])

            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
            else:
                try:
                    body = msg.get_payload(decode=True).decode()
                except:
                    pass

            email_list.append({
                "subject": subject,
                "body": body
            })

        mail.logout()

        print("Emails extracted:", email_list)

        return email_list

    except Exception as e:
        print("Email fetch error:", e)
>>>>>>> 0c94d1aa3ad327c92e2fbd0af7b279095d94b96a
        return []