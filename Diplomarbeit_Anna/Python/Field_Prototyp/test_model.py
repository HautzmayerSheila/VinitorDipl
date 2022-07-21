import matplotlib.pyplot as plt
from skimage import io
import numpy as np
import pickle
import cv2

import extractFeatures

filename = "field_model"
loaded_model = pickle.load(open(filename, 'rb'))

img: np.ndarray = cv2.imread("Fields/test/field_6.png")
img: np.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
X = extractFeatures.filter("Fields/test/field_6.png", "field_6.png")
X = X.drop(["Image_Name"], axis=1)
X["Image_Name"] = 0
X["index"] = 0
result = loaded_model.predict(X)
segmented = result.reshape(img.shape)
segmented = segmented.astype(np.int8)
plt.imshow(segmented)
plt.show()
#io.imsave('images/segmented_image_trained_test.png', segmented)
# plt.imsave('images/sandstone/Segmanted_images/'+ image, segmented, cmap ='jet')
