from skimage import io
from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.keras import layers as l
import tensorflow.python.keras as kr

image_data = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = image_data.load_data()

# NOTE Plot
# ind = 0
# plt.imshow(train_images[ind], cmap="gray")
# plt.xlabel(f"Label: {train_labels[ind]}")
# plt.show()

train_images = train_images/255.0
test_images = test_images / 255.0

model: kr.Sequential = tf.keras.Sequential([
    l.Flatten(
        input_shape=(28,28)
    ),
    l.Dense(128, activation="relu"),
    l.Dense(10)     #Output
])

model.compile(optimizer="adam",
              loss=kr.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy"]
              )

model.fit(x=train_images, y=train_labels, epochs=10)

predicted = model.predict(x=test_images)

for i in range(20):
    print(f"{i}. Predicted: {np.argmax(predicted[i])}  Actual: {test_labels[i]}")

