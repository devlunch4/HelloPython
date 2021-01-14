# original 
from cv2 import cv2
from tensorflow.python.keras.models import load_model
import numpy as np
import urllib

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

#모델 로드#######
print("훈련 모델 로딩")
model = load_model("mymodel")

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

########
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