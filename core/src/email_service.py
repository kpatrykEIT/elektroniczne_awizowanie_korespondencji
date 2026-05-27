import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from config import config


def send_email(to_email, subject, body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = config["admin_email"]
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(attachment_path)}"
            )

            msg.attach(part)

        with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
            server.starttls()
            server.login(config["admin_email"], config["email_password"])
            server.send_message(msg)

        print("Email sent successfully")

    except Exception as e:
        print(f"Email error: {e}")