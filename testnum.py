import streamlit as st
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time
import os

os.system("pip install apscheduler")

# Email sending function
def send_email(recipient, subject, body):
    sender_email = "ftpb2024.1776@gmail.com"
    sender_password = "oyls tmvu cpko kyqc"
    
    # Create MIME message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient

    # Turn the body into a MIMEText object
    part = MIMEText(body, "plain")
    message.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, message.as_string())
        server.quit()
        print(f"Email sent to {recipient}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to be scheduled - sends an email at random intervals
def scheduled_email_job():
    # Here, you'd fetch your email details (recipient, subject, body) probably stored from the Streamlit inputs
    recipient = "ftb2024.1776@gmail.com"  # Placeholder values
    subject = "Your Subject Here"
    body = "Your email body here."
    send_email(recipient, subject, body)
    print("Email scheduled job executed.")

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_email_job, 'interval', seconds=random.randint(10, 100))
scheduler.start()

# Prevent the scheduler from shutting down immediately
try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

# Streamlit UI
st.title("Email Automation App")

recipient = st.text_input("Recipient Email")
subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

if st.button("Schedule Email"):
    # Here, instead of sending directly, store these details and let the scheduled job use them
    st.write("Email scheduled!")

