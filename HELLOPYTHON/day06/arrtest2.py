
arr = []

# 자바의 배열과 다른점은 자바는 변하지 않으나 파이썬은 변한다
arr.append("가")
arr.append("나")
# arr.insert(0, "다")
arr.insert(len(arr), "다")
arr.insert(len(arr), "라")

print (arr)
