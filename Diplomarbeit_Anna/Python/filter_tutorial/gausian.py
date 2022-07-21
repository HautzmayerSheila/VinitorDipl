import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian
from matplotlib import pyplot as plt

img_gaussian_noise = img_as_float(io.imread('images/Osteosarcoma_01_25Sigma_noise.tif', as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread('images/Osteosarcoma_01_8bit_salt_pepper.tif', as_gray=True))

plt.imshow(img_salt_pepper_noise, cmap='gray')
plt.show()

img = img_gaussian_noise

gaussian_using_cv2 = cv2.GaussianBlur(img, (3,3), 0, borderType=cv2.BORDER_CONSTANT)

gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval= 0.0)
#sigma defines the std dev of the gaussian kernel.

plt.imshow(gaussian_using_skimage, cmap='gray')
plt.show()