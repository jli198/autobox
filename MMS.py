"""
Thank you to https://www.alfredosequeida.com/blog/how-to-send-text-messages-for-free-using-python-use-python-to-send-text-messages-via-email/
"""
import email, smtplib, ssl
from providers import PROVIDERS

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from os.path import basename

def send_mms(
    number: str,
    message: str,
    file_path: str,
    mime_maintype: str,
    mime_subtype: str,
    provider: str,
    sender_credentials: tuple = ("autoboxproject@gmail.com", "{ADD PASSWORD}"),
    subject: str = "Autobox Alert",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):

    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("mms")}'

    email_message=MIMEMultipart()
    email_message["Subject"] = subject
    email_message["From"] = sender_email
    email_message["To"] = receiver_email

    email_message.attach(MIMEText(message, "plain"))

    with open(file_path, "rb") as attachment:
        part = MIMEBase(mime_maintype, mime_subtype)
        part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={basename(file_path)}",
        )

        email_message.attach(part)

    text = email_message.as_string()

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, text)

number = "{Chris Phone Number or Jason for that matter}"
message = "Autobox Alert"
provider = "{Chris mobile carrier}"

sender_credentials = ("autoboxproject@gmail.com", "{ADD PASSWORD HERE}")


file_path = "{ADD FILEPATH}" 

mime_maintype = "image"
mime_subtype = "jpeg"

send_mms(
    number,
    message,
    file_path,
    mime_maintype,
    mime_subtype,
    provider,
    sender_credentials,
    )
