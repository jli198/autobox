#!/usr/bin/python
import sys
import subprocess
import os
import time

# aws rekognition detect-text --image "S3Object={Bucket=autoboximages,Name=Head_Moderator.jpg}" --region us-east-1 > Head_Moderator_Text.txt


def detect_text(bucket, imagejpg, image):

	CMD = 'aws rekognition detect-text --image "S3Object={Bucket=%s,Name=%s}" --region us-east-1 > %s_Text.json' % (bucket, imagejpg, image)
	subprocess.call(CMD, shell=True)
	print(CMD)


def detect_labels(bucket, imagejpg, image):

	CMD = 'aws rekognition detect-labels --image "S3Object={Bucket=%s,Name=%s}" --region us-east-1 > %s_Labels.json' % (bucket, imagejpg, image)
	subprocess.call(CMD, shell=True)
	print(CMD)
