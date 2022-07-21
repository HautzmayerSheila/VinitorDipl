from skimage import io, filters, feature
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np
from skimage.filters import roberts, sobel, scharr, prewitt, farid


img = io.imread('images/synthetic.jpg', 1)

print(img.shape)

#Edge detection

roberts_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)
farid_img = farid(img)

plt.imshow(img, cmap="gray")
plt.show()
plt.imshow(roberts_img, cmap="gray")
plt.show()
plt.imshow(roberts_img, cmap="gray")
plt.show()
plt.imshow(scharr_img, cmap="gray")
plt.show()
plt.imshow(prewitt_img, cmap="gray")
plt.show()
plt.imshow(farid_img, cmap="gray")
plt.show()