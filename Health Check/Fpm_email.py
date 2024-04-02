import requests
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Assuming response is JSON data
        else:
            print("Failed to fetch data from the URL:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def save_to_log(data, log_file):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Log Taken Time:", timestamp)
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] {data}\n")  # Write timestamp and data
            f.write('\n')                        # Append an empty line
            print("Data saved to log successfully")
    except Exception as e:
        print("Error saving data to log:", e)

def send_email(subject, body, receiver_emails):
    try:
        # Email configuration
        sender_email = "fpm_alert@worldlink.com.np"
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

# Define the receiver email addresses
receiver_emails = ["ruskin.bhandari@worldlink.com.np"]

if __name__ == "__main__":
    url = "https://int-mobileapp.wlink.com.np/health.php"
    log_file = "Fpm_data_log.txt"

    while True:
        data = get_data(url)
        if data:
            save_to_log(data, log_file)
            # Check conditions for sending email
            try:
                fpm_value = int(data.get('fpm', 0))
                disk = data.get('disk', {})  # Retrieve the 'disk' dictionary from the data
                diskfree_value = int(disk.get('diskfree', 9999))  # Retrieve 'diskfree' from the 'disk' dictionary
                print("FPM Value:", fpm_value)
                print("Diskfree Value:", diskfree_value)

                if fpm_value > 150 or diskfree_value < 4:
                    print("Conditions met. Sending email...")
                    # Get the current timestamp for Email
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    subject = "Alert: High FPM or Low Diskfree"
                    body = (f"[{timestamp}] FPM is {fpm_value} and Diskfree is {diskfree_value}. \n "
                        f"Please check Int_mob_app_Health for details.")
                    send_email(subject, body, receiver_emails)
                else:
                    print("Conditions not met. Email not sent.")
            except ValueError:
                print("Error: Could not convert data to integer")

        # Wait for 30 minutes
        time.sleep(30 * 60)