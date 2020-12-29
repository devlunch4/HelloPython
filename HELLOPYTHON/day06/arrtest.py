
arr = []

# 자바의 배열과 다른점은 자바는 변하지 않으나 파이썬은 변한다
arr.append("1,2")
arr.append("3,4")

for i in range(2):
    line = []
    line.append(5)
    line.append(6)
    arr.append(line)
# 

print ("arr : ", ":", arr)
print ("line : ", ":", arr)
