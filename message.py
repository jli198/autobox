import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
#    "sprint": "@messaging.sprintpcs.com"
}

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
 
def send_message(phone_number, carrier, message, IMAGE_NAME):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    msg = MIMEMultipart()
    msg.attach(MIMEText(message, "plain")
    msg.attach(MIMEImage(file(IMAGE_NAME).read()))
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, msg.as_string())
    server.close()

