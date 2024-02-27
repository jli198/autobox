from gpiozero import MotionSensor, Button, LED
from picamera2 import Picamera2
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import os
import email.mime.application
import datetime
import smtplib
import time
from time import sleep

from picamera2.encoders import H264Encoder
encoder = H264Encoder(bitrate=10000000)

pir = MotionSensor(20)
camera = Picamera2()
led = LED(17)
button = Button(16)

#replace the next three lines with your credentials
from_email_addr = 'autoboxcow@gmail.com'
from_email_password = 'aqqwvrvfajzoyunw'
to_email_addr = 'michaelabanks01@gmail.com'

#Create Alarm State by default it is off.
Alarm_state = True
Movement_state = True
while True:


    if button.is_pressed:
        Alarm_state = True
        print('Alarm ON')

    if Alarm_state == True:

        led.on()
        sleep(1)
        #if pir.motion_detected:
        if Movement_state == True:
            print("Motion Detected")
            led.off()
            #Video record
            camera.resolution = (640,480)
            camera.rotation = 180
            camera.start_recording(encoder,'alert_video.h264')
            time.sleep(2)
            camera.stop_recording()

            #coverting video from .h264 to .mp4
            command = "MP4Box -add alert_video.h264 alert_video.mp4"
            call([command], shell=True)
            print("video converted")


            #Create the Message
            msg = MIMEMultipart()
            msg[ 'Subject'] = 'INTRUDER ALERT..!!'
            msg['From'] = from_email_addr
            msg['To'] = to_email_addr


            #Video attachment
            Captured = '/home/admin/alert_video.h264'
            fp=open(Captured,'rb')
            att = email.mime.application.MIMEApplication(fp.read(),_subtype=".mp4")
            fp.close()
            att.add_header('Content-Disposition','attachment',filename='video' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.mp4')
            msg.attach(att)

            print("attach successful")

            #removing .h264 & .mp4 extra files
            os.remove("/home/admin/alert_video.h264")

            #renaming file
            #os.rename('alert_video.h264', datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.h264')

            #send Mail
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            #server.starttls()
            server.login(from_email_addr, from_email_password)
            server.sendmail(from_email_addr, to_email_addr, msg.as_string())
            server.quit()
            print('Email sent')
            Alarm_state = False
            Movement_state = False
