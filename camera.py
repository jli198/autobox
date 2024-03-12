#!/usr/bin/python
from gpiozero import MotionSensor

import datetime as dt
import sys
import subprocess
import os
from rekognition_detect import *
from json_parse import *
from image_rectangle import *

pir = MotionSensor(4)

IMAGE_NAME = dt.datetime.now().strftime('%m%d%Y%H%M%S')+ '.jpg'
BUCKET = "s3://autoboximages/"
SRC_DIR = '/home/admin/' + IMAGE_NAME # path may be wrong now
DEST = BUCKET + "images/" # need to remake images folder in bucket
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

while True:
	pir.wait_for_motion()
	print("You moved")
	
	camera(IMAGE_NAME)
	CMD = "s3cmd put --acl-public %s %s" % (SRC_DIR, BUCKET)
	print(CMD)
	subprocess.call(CMD, shell=True)
	time.sleep(5)
	detect_text(BUCKET[5:-1], IMAGE_NAME, IMAGE_NAME[:-4])
	time.sleep(1)
	detect_labels(BUCKET[5:-1], IMAGE_NAME, IMAGE_NAME[:-4])
	parsed_text = json_parse_text_bounding_box(IMAGE_NAME[:-4] + "_Text.json")
	print(parsed_text(0))
	parsed_labels = json_parse_labels(IMAGE_NAME[:-4] + "_Labels.json")
	print(parsed_labels)
	time.sleep(1)
	word_location(IMAGE_NAME[:-4], parsed_text[1])
	os.remove('/home/admin/'+IMAGE_NAME)
	# os.remove('/home/admin/'+IMAGE_NAME[:-4]+'_Text.json')
	# os.remove('/home/admin/'+IMAGE_NAME[:-4]+'_Labels.json')
	pir.wait_for_no_motion()
