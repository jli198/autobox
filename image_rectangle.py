import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image



#im = Image.open('Head Moderator.jpeg')
def word_location(image, bounding_boxes):

    im = Image.open(image)
    
    width, height = im.size

    # Create figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(im)

    for i in range(len(bounding_boxes)):
        # Create a Rectangle patch
        #rect = patches.Rectangle((0.10800746083259583*width, 0.11229314655065536*height), 0.6294227242469788*width, 0.05673758685588837*height, linewidth=1, edgecolor='lime', facecolor='none')
        rect = patches.Rectangle((bounding_boxes[i]["Left"]*width, bounding_boxes[i]["Top"]*height), bounding_boxes[i]["Width"]*width, bounding_boxes[i]["Height"]*height, linewidth=1, edgecolor='lime', facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)
        
    plt.show()
    return


#bounding_box_list = [{'Width': 0.5977653861045837, 'Height': 0.07328605651855469, 'Left': 0.23649908602237701, 'Top': 0.030732858926057816}, {'Width': 0.6294227242469788, 'Height': 0.05673758685588837, 'Left': 0.10800746083259583, 'Top': 0.11229314655065536}, {'Width': 0.540037214756012, 'Height': 0.11347518861293793, 'Left': 0.23649908602237701, 'Top': 0.16903074085712433}, {'Width': 0.11701598763465881, 'Height': 0.07760198414325714, 'Left': 0.8123537302017212, 'Top': 0.18682079017162323}, {'Width': 0.4450652003288269, 'Height': 0.047281306236982346, 'Left': 0.10614524781703949, 'Top': 0.8877068161964417}, {'Width': 0.29236504435539246, 'Height': 0.042553190141916275, 'Left': 0.5921787619590759, 'Top': 0.890070915222168}, {'Width': 0.44134077429771423, 'Height': 0.04373515397310257, 'Left': 0.2793295979499817, 'Top': 0.9361703395843506}, {'Width': 0.25325891375541687, 'Height': 0.03546099364757538, 'Left': 0.7169459462165833, 'Top': 0.9479905962944031}]

#word_location("Head Moderator.jpeg", bounding_box_list)
