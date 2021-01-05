import numpy as np

a = [ 1, 2, 3, 4, 5, 6, 7, 8]
print("a :",a)

b = np.reshape(a, [2, 4])
print("b :",b)


c = [
    [1,2,3,4],
    [5,6,7,8]
    ]
print("c :",c)
#7 추출하기
print(c[1][2])
print(b[1][2])