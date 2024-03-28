from randnum import generate_random_number
import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_addr, from_addr, password):
    """
    Send an email using Python.

    :param subject: Email subject as a string.
    :param message: Email message body as a string.
    :param to_addr: Recipient email address as a string.
    :param from_addr: Sender email address as a string.
    :param password: Password for the sender's email account.
    """
    # Create MIME message
    mime_message = MIMEMultipart()
    mime_message['From'] = from_addr
    mime_message['To'] = to_addr
    mime_message['Subject'] = subject
    mime_message.attach(MIMEText(message, 'plain'))
    
    try:
        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        server.login(from_addr, password)  # Login to the SMTP server
        server.send_message(mime_message)  # Send the email
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Your details
    FROM_EMAIL = "ftpb2024.1776@gmail.com"
    EMAIL_PASSWORD = "oyls tmvu cpko kyqc"
    TO_EMAIL = "ftpb2024.1776@gmail.com"
    SUBJECT = "Test Email from Python"
    MESSAGE = "This is a test email sent from a Python script."

    send_email(SUBJECT, MESSAGE, TO_EMAIL, FROM_EMAIL, EMAIL_PASSWORD)


def main():
    st.title("display")
    for number in generate_random_number():
        if number < 10:
            print("This works")

if __name__ == "__main__":
    main()
