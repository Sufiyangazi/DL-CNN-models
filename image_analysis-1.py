# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %%
# method-1
# using opencv method when you read the image it will open in a new window
# And image will disply on the window if you want to close the window press : 0
import os
os.getcwd()
# %%
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
image.shape

# %%
# use the below steps to read the image using opencv
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
cv2.imshow('ozge',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
# Method-3 - Using pillow package
from PIL import Image
image = Image.open('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
image.show()
# %%
# Above code is for opening the image in the another window
# Use this code open the image below the code
from PIL import Image
image = Image.open('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
image
# %%
# Method - 4 - Using Matplotlib
import matplotlib.pyplot as plt
from PIL import Image
# Opening the image using pillow package
image = Image.open('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
# show the image using matplotlib.pyplot
plt.imshow(image)
# %%
import matplotlib.pyplot as plt
import cv2
# Read the image using opencv or pillow
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
# open the image using matplotlib
plt.imshow(image)
# %%
from PIL import Image
image = Image.open('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
plt.imshow(image)
# %%
import cv2
