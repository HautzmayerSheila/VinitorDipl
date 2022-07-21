import matplotlib.pyplot as plt
import numpy as np

from skimage import data, io, img_as_ubyte
from skimage.filters import threshold_multiotsu

image: np.ndarray = io.imread("images/BSE.jpg", as_gray=True)
print(image.shape)

thresholds = threshold_multiotsu(image, classes=5)
print(thresholds)

regions = np.digitize(image, bins=thresholds)

output = img_as_ubyte(regions)

#plt.imsave("images/Otsu_Segmented.jpg", output)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))


# Plotting the histogram and the two thresholds obtained from
# multi-Otsu.
ax[0].hist(image.ravel(), bins=255)
ax[0].set_title('Histogram')
for thresh in thresholds:
    ax[0].axvline(thresh, color='r')

# Plotting the Multi Otsu result.
ax[1].imshow(regions, cmap='Accent')
ax[1].set_title('Multi-Otsu result')
ax[1].axis('off')

plt.subplots_adjust()

plt.show()