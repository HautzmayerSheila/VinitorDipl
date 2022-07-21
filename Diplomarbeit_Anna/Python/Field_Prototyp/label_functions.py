import pandas as pd
import numpy as np
import cv2
import os


def label_images(label_path):
    label_df = pd.DataFrame()
    for labeled_image in os.listdir(label_path):
        print(labeled_image)

        df2 = pd.DataFrame()
        label = cv2.imread(label_path + labeled_image)
        label: np.ndarray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)

        label_values = label.reshape(-1)
        df2['Label_Value'] = label_values
        df2['Label_Name'] = labeled_image

        label_df = pd.concat([label_df, df2])
    return label_df
