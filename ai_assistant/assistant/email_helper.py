def handle_email():
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")
    print(f"📧 Sending email to {recipient}...\nSubject: {subject}\nBody: {body}")
