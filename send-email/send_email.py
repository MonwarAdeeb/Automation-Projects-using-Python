import smtplib
import ssl
from email.message import EmailMessage

subject = "Test Email From Python"
body = "This is a test email form Automation Python Project!"
sender_email = "monwar.adeeb@gmail.com"
receiver_email = "monwar.adeeb@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Automated Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Successfully Sent!")