import mahotas as mh
from skimage import io
from matplotlib import pyplot as plt
import numpy as np

image = io.imread('SimpleImageDataset/building05.jpg')
#image = image - image.mean()

plt.imshow(image)
#plt.show()


image = mh.colors.rgb2gray(image, dtype=np.uint8)
plt.imshow(image) # Display the image
plt.gray()
#plt.show()

thresh = mh.thresholding.otsu(image)
#print(thresh)
plt.imshow(image > thresh)
#plt.show()

# Weiß als wohnblock und schwarzer himmel
# otsubin = (image <= thresh)
# otsubin = mh.close(otsubin, np.ones((15,15)))

otsubin = (image > thresh)
otsubin = mh.open(otsubin, np.ones((15,15)))
plt.imshow(otsubin)
#plt.show()

thresh = mh.thresholding.rc(image)
print(thresh)
