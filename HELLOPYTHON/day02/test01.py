# 수학 점수를 입력하시오

ma = int(input("수학 점수를 입력하시오"))
ko = int(input("국어 점수를 입력하시오"))
en = int(input("영어 점수를 입력하시오"))

total = ma + ko + en
avg = total / 3

print("수학", ":", ma)
print("국어", ":", ko)
print("영어", ":", en)
print("평균", ":", avg)
print("총합", ":", total)