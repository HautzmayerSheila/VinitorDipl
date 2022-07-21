from skimage import io, filters, feature
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np


img = io.imread('images/field_1.png', 0)

#Canny
canny_edge = cv2.Canny(img, 100, 140)  #Supply Thresholds 1 and 2

#Autocanny
# sigma = 0.3
# median = np.median(img)
#
# # apply automatic Canny edge detection using the computed median
# lower = int(max(0, (1.0 - sigma) * median))
# #Lower threshold is sigma % lower than median
#
# upper = int(min(255, (1.0 + sigma) * median))
# #Upper threshold is sigma% higher than median
# #If the value is below 0 then take 0 as the value
#
# auto_canny = cv2.Canny(img, lower, upper)
#
# plt.imshow(canny_edge, cmap="gray")
# plt.show()

plt.imshow(canny_edge, cmap="gray")
plt.show()

plt.imshow(img, cmap="gray")
plt.show()
