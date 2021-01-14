# tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras

# 헬퍼(helper) 라이브러리를 임포트합니다
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist


print("tensorflow VER check:", tf.__version__)

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
#전처리
train_images = train_images / 255.0

test_images = test_images / 255.0