# 100포함~200포함까지 합.

sum = 0
for i in range(101):
     sum = sum + i + 100
print("sum",sum)


sum = 0
for i in range(101):
     sum += (i + 100)
print("sum",sum)
print("sum : " + str(sum))
