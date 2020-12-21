# IF 문을 활용하여 짝수만 더한다.

sum = 0
for i in range(11):
    if i % 2 == 0:
        sum = sum + i
print(sum)
