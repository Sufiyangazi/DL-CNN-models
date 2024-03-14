# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2
# %%
dir(cv2)
# %%
# Read the image using opencv command
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
cv2.imshow('ozge',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
# Convert color image to Gray
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
image
# %%
# Read the image
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
# Gray scale conversion
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# %%
gray_image
# %%
plt.imshow(gray_image)
# %%
# import the all packages used
import cv2
from matplotlib import pyplot as plt
import numpy as np
# %%
cv2.__version__
# %%
# read the image
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\bala.jpg')
cv2.imshow('bala',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
(height,width,channels) = image.shape
# %%
print('image height',height)
print('image width',width)
print('image chaanels',channels)
# %%
type(image)
# %%
# Cropping the image
# For bala eyes
# first give y_axis[start:stop] then x-axis[start:stop]
# then plot the image and get balas eyes
cropped_image = image[500:650,400:800]
# %%
plt.imshow(cropped_image)
# %%
image[500:650,400:800]
# %%
# changing the color of the cropped area
image[500:650,400:800]=(0,0,0)
plt.imshow(image)
# %%
image[500:650,400:800] = [34,143,195]
plt.imshow(image)
# %%
image[500:650,400:800] = (255,255,255)
plt.imshow(image)
# %%
# Translation matrix the first row moves pixels horizentally
# second row moves vertically
M = np.float32([[1,0,250],[0,2,500]])
M
# %%
shifted = cv2.warpAffine(image,
                         M,
                         (image.shape[1],
                          image.shape[0]))
plt.imshow(shifted)
# %%
m = np.float32([[65,43,65],
                [2,2,2]])
shift = cv2.warpAffine(image,
                       m,
                       (image.shape[1],
                        image.shape[0]))
plt.imshow(shift)
# %%
m = np.float32([[4,0,4],
                [2,0,2]])
shift1 = cv2.warpAffine(image,
                        m,
                        (image.shape[1],
                         image.shape[0]))
plt.imshow(shift1)
# %%
m = np.float32([[1,43,-110],
                [0,2,-98]])
sf = cv2.warpAffine(image,
                    m,
                    (image.shape[1],
                     image.shape[0]))
plt.imshow(sf)
# %%
(height,width,channels) = image.shape
center = (width //2,height // 2)
center
# %%
m = cv2.getRotationMatrix2D(center,45,1.0)
rotate = cv2.warpAffine(image,m,(width,height))
plt.imshow(rotate)
# %%
m = cv2.getRotationMatrix2D(center,90,1.0)
df = cv2.warpAffine(image,m,
                    (width,height))
plt.imshow(df)
# %%
