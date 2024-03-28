import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time

# Email sending function
def send_email(recipient, subject, body):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    # SMTP server configuration
    smtp_server = "smtp.example.com"
    smtp_port = 465  # For SSL
    
    # Create MIME message
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient
    part = MIMEText(body, "plain")
    message.attach(part)
    
    # Send the email
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, message.as_string())
        server.quit()
        st.success(f"Email sent to {recipient}!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# Function to wait for a random interval before sending an email
def wait_and_send_email(recipient, subject, body):
    random_interval = random.randint(10, 100)  # Random interval between 10 to 100 seconds
    st.write(f"Waiting for {random_interval} seconds to send the email...")
    time.sleep(random_interval)  # Wait for a random time
    send_email(recipient, subject, body)

# Streamlit UI
st.title("Email Automation App")

recipient = st.text_input("Recipient Email", value="")
subject = st.text_input("Email Subject", value="")
body = st.text_area("Email Body", value="")

if st.button("Send Email"):
    if recipient and subject and body:
        # Execute the wait and send email function without blocking the Streamlit app
        st.write("Scheduling email...")
        # Running the time delay in a separate thread if needed
        import threading
        threading.Thread(target=wait_and_send_email, args=(recipient, subject, body)).start()
    else:
        st.warning("Please fill out all fields.")


if st.button("Schedule Email"):
    # Here, instead of sending directly, store these details and let the scheduled job use them
    st.write("Email scheduled!")

