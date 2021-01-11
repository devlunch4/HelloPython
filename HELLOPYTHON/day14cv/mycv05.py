
import cv2

# 버전확인
# print(cv2.__version__)

# 이미지 읽기
img = cv2.imread('nikereact2.jpg', 1)
        
print(img)
print("shape :", img.shape)

# 이미지 화면에 표시 >> 파란색만
for i in img:
    print(i)
    for j in i:
    #    j[0] = 0 #R
        j[1] = 0 #G
        j[2] = 0 #B
        
cv2.imshow('Test Image', img)
# 이미지 다른 파일로 저장
cv2.imwrite('nikereact2_filter.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


