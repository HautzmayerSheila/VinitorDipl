import pandas as pd
import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from skimage.filters import roberts, sobel, scharr, prewitt
from scipy import ndimage as nd
import cv2
from skimage import feature as skf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import os
import pickle


import extractFeatures
import label_functions

img_data: pd.DataFrame = pd.DataFrame()
img_path = "Fields/train/"
for image_name in os.listdir(img_path):
    df = extractFeatures.filter(img_path+""+image_name, image_name)
    img_data = pd.concat([img_data, df])
    print(f"Bild {image_name} wurde gefiltert")

print(img_data.shape)

label_path = "Fields/labels/"
label_data = label_functions.label_images(label_path)

print(label_data.shape)

label_data = label_data.reset_index()
img_data = img_data.reset_index()
dataset = pd.concat([img_data, label_data], axis=1)

dataset = dataset[dataset.Label_Value != 0]

print(dataset.shape)

X = dataset.drop(labels=["Image_Name", "Label_Name", "Label_Value"], axis=1)

Y = dataset["Label_Value"].values

Y = LabelEncoder().fit_transform(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=20)

model = RandomForestClassifier(n_estimators=50, random_state=42)

model.fit(X_train, y_train)
#
# prediction_test = model.predict(X_test)
# print("Accuracy = ", metrics.accuracy_score(y_test, prediction_test))


model_name = "field_model"
pickle.dump(model, open(model_name, 'wb'))


#
# img: np.ndarray = cv2.imread("Fields/train/field_2.png")
# img: np.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# img_flat: np.ndarray = img.reshape(-1)
#
# print(img_flat.__class__)
#
# img_df["Original Image"] = img_flat
#
# num = 1
# kernels = []
# for theta in range(2):
#     theta = theta / 4 * np.pi
#     for sigma in (1, 3):
#         for lamda in np.arange(0, np.pi, np.pi / 4):
#             for gamma in (0.005, 0.5):
#                 gabor_label = "Gabor: " + str(num)
#                 ksize = 15
#                 phi = 1
#                 kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
#                 kernels.append(kernel)
#
#                 fimg: np.ndarray = cv2.filter2D(img, cv2.CV_8UC3, kernel)
#                 fimg_flat: np.ndarray = fimg.reshape(-1)
#
#                 #io.imsave(f"filter/{gabor_label}.jpg", fimg_flat.reshape(img.shape))
#                 #cv2.imwrite(f"filter/{gabor_label}.jpg", fimg_flat.reshape(img.shape))
#                 img_df[gabor_label] = fimg_flat
#                 #print(f"{gabor_label}: theta={theta} sigma={sigma} lamda={lamda} gamma={gamma}")
#                 num += 1
#
# #NOTE Apply other filter
#
# # CANNY EDGE
# edges = skf.canny(img)  # Image, min and max values
# edges1 = edges.reshape(-1)
# img_df['Canny Edge'] = edges1
#
# # ROBERTS EDGE
# edge_roberts = roberts(img)
# edge_roberts1 = edge_roberts.reshape(-1)
# img_df['Roberts'] = edge_roberts1
#
# # SOBEL
# edge_sobel = sobel(img)
# edge_sobel1 = edge_sobel.reshape(-1)
# img_df['Sobel'] = edge_sobel1
#
# # SCHARR
# edge_scharr = scharr(img)
# edge_scharr1 = edge_scharr.reshape(-1)
# img_df['Scharr'] = edge_scharr1
#
# # PREWITT
# edge_prewitt = prewitt(img)
# edge_prewitt1 = edge_prewitt.reshape(-1)
# img_df['Prewitt'] = edge_prewitt1
#
# # GAUSSIAN with sigma=3
# gaussian_img = nd.gaussian_filter(img, sigma=3)
# gaussian_img1 = gaussian_img.reshape(-1)
# img_df['Gaussian s3'] = gaussian_img1
#
# # GAUSSIAN with sigma=7
# gaussian_img2 = nd.gaussian_filter(img, sigma=7)
# gaussian_img3 = gaussian_img2.reshape(-1)
# img_df['Gaussian s7'] = gaussian_img3
#
# # MEDIAN with sigma=3
# median_img = nd.median_filter(img, size=3)
# median_img1 = median_img.reshape(-1)
# img_df['Median s3'] = median_img1
#
# print(img_df.shape)
#
# labeled_img = cv2.imread("Fields/labels/field_2_label.tiff")
# labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_BGR2GRAY)
# labeled_img1 = labeled_img.reshape(-1)
# img_df['Labels'] = labeled_img1
#
# original_img_data = img_df.drop(labels=["Labels"], axis=1)  # Use for prediction
# img_df = img_df[img_df.Labels != 0]
#
# Y = img_df["Labels"].values
# Y = LabelEncoder().fit_transform(Y)
# X = img_df.drop(labels=["Labels"], axis=1)
#
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=20)
#
# model = RandomForestClassifier(n_estimators=20, random_state=42)
# model.fit(X_train, y_train)
#
# prediction_RF = model.predict(X_test)
# print ("Accuracy using Random Forest = ", metrics.accuracy_score(y_test, prediction_RF))
#
# feature_list = list(X.columns)
# feature_imp = pd.Series(model.feature_importances_, index=feature_list).sort_values(ascending=False)
# print(feature_imp)
#
#
# result = model.predict(original_img_data)
# segmented = result.reshape((img.shape))
# plt.imshow(segmented, cmap='gray')
# plt.show()
