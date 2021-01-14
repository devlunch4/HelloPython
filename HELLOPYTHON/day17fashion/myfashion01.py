# 강사와 함꼐
import tensorflow as tf
from cv2 import cv2

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 몇개를 가져오는지 확인
# print("len(train_images):", len(train_images))
# print("len(train_labels):", len(train_labels))
# print("len(test_images):", len(test_images))
# print("len(test_labels):", len(test_labels))
# print("-test_images[0] 배열 출력")
# print(test_images[0])

print("-test_images[0] 배열 출력 시작------------------------------------------------------")
# test_images[0] 배열 출력
for i in test_images[0]:
    for j in i:
        if j > 0:
            print("1", end="")
        else:
            print("0", end="")
    print()
print("-test_images[0] 배열 출력 끝------------------------------------------------------")

# train 저장 fashion 폴더에 저장
for i in range(len(train_images)):
    label = str(train_labels[i])
    cv2.imwrite('fashion/' + label + "_" + str(i) + '.jpg', train_images[i])
print("train_images 저장 완료 생성 파일 수 :",len(train_images))

#클래스 명이 들어갈 배열 설정
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#이미지의 값을 축소화
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

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
