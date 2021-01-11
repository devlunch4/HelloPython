
import cv2

# 버전확인
# print(cv2.__version__)

# 이미지 읽기
img = cv2.imread('nikereact2.jpg', 1)
        
print(img)
print("shape :", img.shape)

# 그림 회전하기
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 시계방향으로 90도 회전
img180 = cv2.rotate(img, cv2.ROTATE_180)  # 180도 회전
img270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 반시계방향으로 90도 회전 
# = 시계방향으로 270도 회전

# 이미지 화면에 표시
cv2.imshow('original', img)
cv2.imshow('rotate90', img90)
cv2.imshow('rotate180', img180)
cv2.imshow('rotate270', img270)

# 이미지 다른 파일로 저장
cv2.imwrite('nikereact2_rotate90.jpg', img90)
cv2.waitKey(0)
cv2.destroyAllWindows()

