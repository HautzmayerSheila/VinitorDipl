import cv2
from skimage import io, img_as_float
from skimage.filters import median
from matplotlib import pyplot as plt
from skimage.morphology import disk
import skimage as sk

img_gaussian_noise = img_as_float(io.imread('images/Osteosarcoma_01_25Sigma_noise.tif', as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread('images/Osteosarcoma_01_8bit_salt_pepper.tif', as_gray=True))

img = img_salt_pepper_noise


#Disk creates a circular structuring element, similar to a mask with specific radius
median_using_skimage = median(img, disk(2), mode='constant', cval=0.0)

plt.imshow(median_using_skimage, cmap="gray")
plt.show()