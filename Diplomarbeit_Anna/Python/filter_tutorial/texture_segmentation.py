
import matplotlib.pyplot as plt
from skimage import io

import numpy as np
from skimage.filters import threshold_otsu
import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import io, img_as_float


from scipy import ndimage


img = img_as_float(io.imread("images/field_2.png", 1))
#
# #Variance - not a great way to quantify texture
# k=7
# img_mean = ndimage.uniform_filter(img, (k, k))
# img_sqr_mean = ndimage.uniform_filter(img**2, (k, k))
# img_var = img_sqr_mean - img_mean**2
# plt.imshow(img_var, cmap='gray')
# plt.show()
# #GABOR - A great filter for texture but usually efficient
# #if we know exact parameters. Good choice for generating features
# #for machine learning
#
ksize=45
theta=np.pi/4
kernel = cv2.getGaborKernel((ksize, ksize), 5.0, theta, 10.0, 0.9, 0, ktype=cv2.CV_32F)
filtered_image = cv2.filter2D(img, cv2.CV_8UC3, kernel)
plt.imshow(filtered_image, cmap='gray')
plt.show()

#Entropy
#Entropy quantifies disorder.
#Since cell region has high variation in pixel values the entropy would be
#higher compared to scratch region

entropy_img = entropy(img, disk(13))

plt.hist(entropy_img.flat, bins=100, range=(0,5))  #.flat returns the flattened numpy array (1D)
#plt.show()
thresh = threshold_otsu(entropy_img)

binary = entropy_img <= thresh
plt.imshow(binary)
plt.show()
