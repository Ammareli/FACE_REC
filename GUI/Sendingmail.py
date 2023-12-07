import smtplib
import random




def send_email(varification_code):
        # Email configuration
    sender_email = "ammarali.ak12@gmail.com"
    receiver_email = "ashfaqmehmood51@gmail.com"
    password = "jamk lczl txhe bshr"

    # Create a message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Verification Code (FACE_ATTENDANCE)"

    # Email content
    body = f"YOUR VARIFICATION CODE IS:  {varification_code} "
    message.attach(MIMEText(body, "plain"))

    # Establish a connection to the SMTP server
    smtp_server = "smtp.gmail.com"  # For Gmail
    smtp_port = 587  # For Gmail
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS

    # Log in to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit the server
    server.quit()   





from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email(0000)

