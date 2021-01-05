import numpy as np
import matplotlib.pyplot as plt
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    user='root',
    passwd='java',
    host='127.0.0.1',
    db='python',
    charset='utf8'
)
cursor = conn.cursor()

sql = "SELECT s_code, s_name, s_price, in_time FROM stock ORDER BY `s_code` ASC LIMIT 10;"
cursor.execute(sql)
row = cursor.fetchall()
print()
print("!!!!!!!!!!!!!!!!!!!!!!!!", len(row))

# # make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test data / x 코드 / y 시간 / z 는 가격
# x = np.arange(0., 1, .1)
# y = np.arange(-1., 1., .1)
# z = np.arange(-1., 1., .1)

count = 0

for i in range(len(row)):
    prtout = [ row[i][0], row[i][1], row[i][2], row[i][3]]
    count += 1
    print("실행중 :", count)
    print(prtout)
    x =  row[i][1]
    x = [row[i][0], row[i][2], row[i][3]]
    print(x)
    
    

    
    

conn.close()
print("연결해제완료")

# plot test data
# 
# make labels
ax.set_xlabel('s_code')
ax.set_ylabel('in_time')
ax.set_zlabel('s_price')

# 
plt.show()
