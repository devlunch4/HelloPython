import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

score = model.evaluate(x_test, y_test)

############ 추가 소스 ##################
print("score :", score)
print("추가소스 진입")
img = Image.open("image/0_95.jpg")
plt.imshow(img)
plt.show()
##
test_num = plt.imread('num7.jpg')
plt.imshow(test_num, cmap='Greys', interpolation='nearest');
test_num = test_num.reshape((1, 28, 28, 1))
print('The Answer is ', model.predict_classes(test_num))
plt.show() 
