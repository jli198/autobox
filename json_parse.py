import json

def json_parse(file):
    #ADD CODE FOR PARSING LABELS AS WELL AND RETURN AS A LIST OR STRING
    with open(file, "r") as read_file:
        data = json.load(read_file)
        json_string = json.dumps(data)
        #print(json_string + "\n")
        json_details = json.loads(json_string)
        #print(json_details)
        word_count = 0
        word_list = []
        word_str = ""
        bounding_box_list = []
        while True:
            try:
                if json_details["TextDetections"][word_count]["Type"] == "WORD":
                    word_list.append(json_details["TextDetections"][word_count]["DetectedText"])
                    bounding_box_list.append(json_details["TextDetections"][word_count]["Geometry"]["BoundingBox"])
                word_count += 1
            except:
                break
        #print(word_list)
        for word in word_list:
            word_str += word + " "
        #print(word_str)
        return word_str, bounding_box_list
