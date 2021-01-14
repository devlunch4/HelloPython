# original 
# https://webnautes.tistory.com/1282
import tensorflow as tf
from cv2 import cv2
import urllib.request
import numpy as np

################
print("웹에서 이미지 가져와서 확인하기 -- 시작")
# 이미지 주소
url = 'https://static-breeze.nike.co.kr/kr/ko_kr/cmsstatic/product/CT2815-200/49d08e22-33ef-4358-ab25-96abfd72a48e_primary.jpg?zoom'
# 이미지 요청 및 다운로드
urllib.request.urlretrieve(url, 'testget.jpg')
# #수정
img = cv2.imread('testget.jpg', cv2.IMREAD_GRAYSCALE)
# 이미지 크기 조절
img2 = cv2.resize(img, (28, 28))
# 이미지 보이기
cv2.imshow('Test Image', img2)
# 흰배경 검은 글씨/물건 상태/ 배열 차원 재 구조화 
img3 = 1 - (img2.reshape((1, 28 * 28)) / 255)
cv2.waitKey(0)
cv2.destroyAllWindows()

########
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)
########
#모델 저장
print("모델저장")
model.save("mymodel")
########

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)


# 구조 확인
print("구조 확인 출력")
print("정확도 판단 : ", model.predict(img3))
# 예측하기
predictions = model.predict(img3)
print("predictions[0] 값 :", predictions[0])
print("np.argmax(predictions[0]) 값 :", np.argmax(predictions[0]))
x = np.argmax(predictions[0])
y = class_names[x]
print("예측 결과 :", y)