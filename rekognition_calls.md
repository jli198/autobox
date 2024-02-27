
# LINUX

```
aws rekognition detect-text --image "S3Object={Bucket=autoboximages,Name=Head_Moderator.jpg}" --region us-east-1 > Head_Moderator_Text.txt

aws rekognition detect-labels --image "S3Object={Bucket=autoboximages,Name=Head_Moderator.jpg}" --region us-east-1 > Head_Moderator_labels.txt

```

# WINDOWS

```

aws rekognition detect-text --image "{\"S3Object\ {\"Bucket\":\"autoboximages\",\"Name\":\"Head_Moderator.jpg\"}}" --region us-east-1 > Head_Moderator_Text_Output.txt

aws rekognition detect-labels --image "{\"S3Object\":{\"Bucket\":\"autoboximages\",\"Name\":\"Head_Moderator.jpg\"}}" --region us-east-1 > Head_Moderator_Labels_Output.txt

```
