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
