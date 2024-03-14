# %%
import cv2
# %%
image =cv2.imread('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
# %%
image
# %%
cv2.imshow('bala',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
from PIL import Image
image = Image.open('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
image.show()
# %%from PIL import Image
image = Image.open('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
# %%
image
# %%
import matplotlib.pyplot as plt
from PIL import Image
image = Image.open('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
plt.imshow(image)
# %%
import matplotlib.pyplot as plt
import cv2
image = cv2.imread('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
plt.imshow(image)
# %%
image=Image.open('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
plt.imshow(image)
# %%
image =cv2.imread('C:\\Users\\Admin\\Downloads\\sherry-christian-8Myh76_3M2U-unsplash.jpg')
cv2.imwrite('ouput.jpg',image)
cv2.imwrite('ouput.png',image)
# %%
image.shape
# %%
(height,width,channels) = image.shape
# %%
print('height ='height)
print('width = 'width)
print('Channels ='channels)
# %%
type(image)
# %%
cropped_image = image[1000:1250,2000:3000]
# %%
eye = plt.imshow(cropped_image)
# %%
image[1000:1250,2000:3000] = (0,0,0)
plt.imshow(image)
# %%
image[1000:1250,2000:3000] = (255,255,255)
plt.imshow(image)
# %%
def fixcolor(image):
    return(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
# %%
import numpy as np
# %%
M =np.float32([[1,0,-50],
            [0,1,-100]])
shifted = cv2.warpAffine(image,
                         M,
                         (image.shape[1],
                          image.shape[0]))
plt.imshow(shifted)
# %%
(height,width,channels) = image.shape
center = (width // 2, height // 2)
center
# %%
M = cv2.getRotationMatrix2D(center,45,1.0)
rotate