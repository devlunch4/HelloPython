# 필요한 라이브러리 불러오기
from cv2 import cv2
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# cv2.imshow('Test Image', train_images[0])
print("생성 저장중")
for i in range(len(train_images)):
    label = str(train_labels[i])
    cv2.imwrite('image/' + label + "_" + str(i) + '.jpg', train_images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
print("저장 완료, 생성된 파일수: ", len(train_images))
