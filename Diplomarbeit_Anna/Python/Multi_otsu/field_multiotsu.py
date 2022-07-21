import matplotlib.pyplot as plt
import numpy as np

from skimage import io, img_as_ubyte
from skimage.filters import threshold_multiotsu
import os


def show_otsu_image_segmented(image_name, classes):
    image: np.ndarray = io.imread("images/"+image_name, as_gray=True)
    print(image.shape)

    thresholds = threshold_multiotsu(image, classes=classes)
    print(thresholds)

    regions = np.digitize(image, bins=thresholds)

    plt.imshow(regions, cmap='Accent')
    plt.title(f'Multi-Otsu - Classes: {classes} - {image_name}')
    plt.axis('off')
    plt.show()


def show_histogram(thresholds, image):
    plt.hist(image.ravel(), bins=255)
    plt.title('Histogram')
    for thresh in thresholds:
        plt.axvline(thresh, color='r')
    plt.show()

img_path = "images/"

for img_name in os.listdir(img_path):
    print(img_name)
    for otsu_class in (2,3,4):
        show_otsu_image_segmented(img_name, otsu_class)