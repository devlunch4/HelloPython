
import cv2

# 버전확인
# print(cv2.__version__)

# 이미지 읽기
img = cv2.imread('brgbw.png', 1)

img[0][0][0] = 255
img[0][0][1] = 255
img[0][0][2] = 0

img[0][1][0] = 255
img[0][1][1] = 255
img[0][1][2] = 0

img[0][2][0] = 255
img[0][2][1] = 255
img[0][2][2] = 0

img[0][3][0] = 255
img[0][3][1] = 0
img[0][3][2] = 0
        
print(img)
print("shape :", img.shape)

# 이미지 화면에 표시
cv2.imshow('Test Image', img)

cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()

