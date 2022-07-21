import pandas as pd
import numpy as np
from skimage.filters import roberts, sobel, scharr, prewitt
from scipy import ndimage as nd
import cv2
from skimage import feature as skf


def filter(img_path, img_name):
    img_df: pd.DataFrame = pd.DataFrame()

    img: np.ndarray = cv2.imread(img_path)
    img: np.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_flat: np.ndarray = img.reshape(-1)
    img_df['Image_Name'] = img_name
    img_df['Pixel_Value'] = img_flat

    num = 1
    kernels = []
    for theta in range(2):
        theta = theta / 4 * np.pi
        for sigma in (1, 3):
            for lamda in np.arange(0, np.pi, np.pi / 4):
                for gamma in (0.005, 0.5):
                    gabor_label = "Gabor: " + str(num)
                    ksize = 15
                    phi = 1
                    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
                    kernels.append(kernel)

                    fimg: np.ndarray = cv2.filter2D(img, cv2.CV_8UC3, kernel)
                    fimg_flat: np.ndarray = fimg.reshape(-1)

                    # io.imsave(f"filter/{gabor_label}.jpg", fimg_flat.reshape(img.shape))
                    #cv2.imwrite(f"filter/{gabor_label}.jpg", fimg_flat.reshape(img.shape))
                    img_df[gabor_label] = fimg_flat
                    # print(f"{gabor_label}: theta={theta} sigma={sigma} lamda={lamda} gamma={gamma}")
                    num += 1

    # NOTE Apply other filter

    # CANNY EDGE
    edges = skf.canny(img)  # Image, min and max values
    edges1 = edges.reshape(-1)
    img_df['Canny Edge'] = edges1
    #cv2.imwrite(f"filter/canny.jpg", edges1.reshape(img.shape))

    # ROBERTS EDGE
    edge_roberts = roberts(img)
    edge_roberts1 = edge_roberts.reshape(-1)
    img_df['Roberts'] = edge_roberts1
   # cv2.imwrite(f"filter/roberts.jpg", edge_roberts1.reshape(img.shape))

    # SOBEL
    edge_sobel = sobel(img)
    edge_sobel1 = edge_sobel.reshape(-1)
    img_df['Sobel'] = edge_sobel1
   # cv2.imwrite(f"filter/sobel.jpg", edge_sobel1.reshape(img.shape))

    # SCHARR
    edge_scharr = scharr(img)
    edge_scharr1 = edge_scharr.reshape(-1)
    img_df['Scharr'] = edge_scharr1
    #cv2.imwrite(f"filter/scharr.jpg", edge_scharr1.reshape(img.shape))

    # PREWITT
    edge_prewitt = prewitt(img)
    edge_prewitt1 = edge_prewitt.reshape(-1)
    img_df['Prewitt'] = edge_prewitt1
    #cv2.imwrite(f"filter/prewitt.jpg", edge_prewitt1.reshape(img.shape))

    # GAUSSIAN with sigma=3
    gaussian_img = nd.gaussian_filter(img, sigma=3)
    gaussian_img1 = gaussian_img.reshape(-1)
    img_df['Gaussian s3'] = gaussian_img1
    #cv2.imwrite(f"filter/gaussian3.jpg", gaussian_img1.reshape(img.shape))

    # GAUSSIAN with sigma=7
    gaussian_img2 = nd.gaussian_filter(img, sigma=7)
    gaussian_img3 = gaussian_img2.reshape(-1)
    img_df['Gaussian s7'] = gaussian_img3
    #cv2.imwrite(f"filter/gaussian7.jpg", gaussian_img3.reshape(img.shape))

    # MEDIAN with sigma=3
    median_img = nd.median_filter(img, size=3)
    median_img1 = median_img.reshape(-1)
    img_df['Median s3'] = median_img1
    #cv2.imwrite(f"filter/median.jpg", median_img1.reshape(img.shape))
    return img_df
