
import cv2

# 버전확인
# print(cv2.__version__)

# 원본
img = cv2.imread('nikereact2.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Test Image', img)
cv2.waitKey(1)

print(img)
print("shape :", img.shape)

# 흑백
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_img", gray_img)
cv2.waitKey(0)

print(gray_img)
print("BL-WT shape :", gray_img.shape)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()

