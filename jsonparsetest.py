import json

with open("awsjsontest.json", "r") as read_file:
    data = json.load(read_file)
    json_string = json.dumps(data)
    print(json_string + "\n")
    json_details = json.loads(json_string)
    print(json_details)
    word_count = 0
    word_list = []
    word_str = ""
    while True:
        try:
            if json_details["TextDetections"][word_count]["Type"] == "LINE":
                word_list.append(json_details["TextDetections"][word_count]["DetectedText"])
            word_count += 1
        except:
            break
    print(word_list)
    for word in word_list:
        word_str += word + " "
    print(word_str)
