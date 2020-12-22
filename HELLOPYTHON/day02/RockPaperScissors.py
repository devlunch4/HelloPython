import random

mine = input("가위1바위2보3 선택하시오...")
minex = ""

if mine == "1":
    minex = "가위"
elif mine == "2":
    minex = "바위"
elif mine == "3":
    minex = "보"

com = ""
rnd = random.random()

if rnd < 0.3:
    com = "가위"
elif rnd < 0.6: 
    com = "바위"
else:
    com = "보"
    
result = ""
if minex == com:
    result = "비겼습니다."
elif (minex == "가위" and com == "보") or (minex == "바위" and com == "가위") or (minex == "보" and com == "바위"):
    result = "이겼습니다."
else:
    result = "졌습니다."
    
print("mine", ":", mine)    
print("minex", ":", minex)
print("com", ":", com)
print("result", ":", result)
