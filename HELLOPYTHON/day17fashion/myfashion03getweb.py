# original 
import urllib.request
from cv2 import cv2

################
print("웹에서 이미지 가져와서 확인하기 -- 시작")
# 이미지 주소
url = 'https://cdn.imweb.me/thumbnail/20200924/e1f059d0cb20b.jpg'

# 이미지 요청 및 다운로드
urllib.request.urlretrieve(url, 'testget.jpg')

img = cv2.imread('testget.jpg', cv2.IMREAD_GRAYSCALE)
# 이미지 크기 조절
img2 = cv2.resize(img, (28, 28))
# 이미지 보이기
cv2.imshow('Test Image', img2)
# 흰배경 검은 글씨/물건 상태/ 배열 차원 재 구조화 
img3 = 1 - (img2.reshape((1, 28 * 28)) / 255)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 구조 확인
# print("정확도 판단 : ", model.predict(img3))
# print('The Answer is ', model.predict_classes(img3))
