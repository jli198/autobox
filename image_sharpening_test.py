import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Load the image 
image = cv2.imread('Head Moderator.jpeg')

scale_percent = 200 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# add rescaling
image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 
  
# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
  
# Sharpen the image 
sharpened_image = cv2.filter2D(image, -1, kernel) 
  
#Save the image 
cv2.imwrite('sharpened_image.jpg', sharpened_image) 
  
#Plot the sharpened image 
plt.subplot(1, 2, 2) 
plt.title("Sharpening") 
plt.imshow(sharpened_image) 
plt.show()


# Load the image 
image = cv2.imread('Head Moderator.jpeg')

scale_percent = 200 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# add rescaling
image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

# add rescaling
#image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)


#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((1, 1), np.uint8)
image = cv2.dilate(image, kernel, iterations=1)
image = cv2.erode(image, kernel, iterations=1)

# Remove noise using a median filter
#image = cv2.medianBlur(image, 11)

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
image = cv2.filter2D(image, -1, kernel) 
  
#Save the image 
cv2.imwrite('Modified_Image.jpg', image) 
  
#Plot the blured image 
plt.subplot(1, 2, 2) 
plt.title("Modified Image") 
plt.imshow(image) 
plt.show()
