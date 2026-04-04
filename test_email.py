<<<<<<< HEAD
from email_reader import fetch_unread_emails

emails = fetch_unread_emails()

print("\n=== EMAILS FETCHED ===")
for mail in emails:
    print("Subject:", mail["subject"])
    print("Body:", mail["body"])
=======
from email_reader import fetch_unread_emails

emails = fetch_unread_emails()

print("\n=== EMAILS FETCHED ===")
for mail in emails:
    print("Subject:", mail["subject"])
    print("Body:", mail["body"])
>>>>>>> 0c94d1aa3ad327c92e2fbd0af7b279095d94b96a
    print("------")