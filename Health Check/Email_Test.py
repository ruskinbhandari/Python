import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, receiver_emails):
    try:
        # Email configuration
        sender_email = "ruskin.bhandari.wlink@gmail.com"
        smtp_server = "smtp.wlink.com.np"
        smtp_port = 25  # Change port if required

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject

        # Construct the email body
        msg.attach(MIMEText(body, 'plain'))

        # Setup SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Send email to each receiver
        for receiver_email in receiver_emails:
            msg['To'] = receiver_email
            server.sendmail(sender_email, receiver_email, msg.as_string())

        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", e)

# Define the receiver email addresses outside the function
receiver_emails = ["ruskin.bhandari@worldlink.com.np"]

# Get the current timestamp for Email
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject = "Test Email"
body = (f"[{timestamp}] Test mail. \n "
        f"Please Ignore test mail.")
send_email(subject, body, receiver_emails)
