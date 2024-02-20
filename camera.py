#!/usr/bin/python
import datetime as dt
import sys
import subprocess
import os

IMAGE_NAME = dt.datetime.now().strftime('%m%d%Y%H%M%S')+ '.jpg'
BUCKET = "s3://autoboximages/"
SRC_DIR = '/home/admin/Documents/' + IMAGE_NAME
DEST = BUCKET + "images/"
CURRENT_DATE = dt.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

def camera(file):
  cmd = 'rpicam-jpeg'
  args = '-o'
  temp = subprocess.Popen([cmd, args, file], stdout = subprocess.PIPE)
  output = str(temp.communicate())
  output = output.split("\n")
  output = output[0].split('\\')

  res = []
  for line in output:
    res.append(line)
  print('camera results')
  print('\n'.join(res[len(res) - 3:len(res) - 1]))
  return res

camera(IMAGE_NAME)

CMD = "s3cmd put --acl-public %s %s" % (SRC_DIR, BUCKET)
print(CMD)
subprocess.call(CMD, shell=True)
os.remove('/home/admin/Documents/'+IMAGE_NAME)
