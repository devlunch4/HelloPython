import numpy as np
import matplotlib.pyplot as plt
import pymysql


# 함수화를 위한 클래스 설정
class MyManager:

    def __init__(self):
        self.conn = pymysql.connect(user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    def getPrices(self, s_name):
        print("getPrices 진입")
                # SQL문 실행 SELECT
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = %s ORDER BY in_time DESC;"
        self.cursor.execute(sql, (s_name,))
        rows = self.cursor.fetchall()
        prices = []
        for row in rows:
            prices.append(row[2])
        return prices
    
    def setlinexy(self):
        print("setline 진입")
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = '삼성전자' ORDER BY in_time DESC;"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return len(rows)
    
    def getName(self):
        print("getName 진입")
        sql = "SELECT DISTINCT(s_name) FROM stock;"
        self.cursor.execute(sql)
        namerows = self.cursor.fetchall()
        return namerows
    
    def getPricesPer(self, s_name):
        # 초기값 가져오기
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = %s ORDER BY in_time"
        self.cursor.execute(sql, (s_name,))
        rows = self.cursor.fetchall()
        self.fvalue = (str(rows[0][2]))
        print("self.fvalue 시작가 :", self.fvalue)
        # 최종값 설정
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = %s ORDER BY in_time"
        self.cursor.execute(sql, (s_name,))
        rows = self.cursor.fetchall()
        prices = []

        for row in rows:
            # print("getPricesPer변화율:",row[1], "변화율 :", (row[2] - rows[0][2]) / rows[0][2] * 100, "시간 :", row[3])
            zerobreak = rows[0][2]
            pvalue = row[2]
            if zerobreak == 0:
                zerobreak = 1
                pvalue = 1
            prices.append((pvalue - zerobreak) / zerobreak * 100)
        return prices


# MyManager CALL
mm = MyManager()

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# x, y 배열 설정
lenonecode = int(mm.setlinexy())
xarray = []
yarray = []         
zarray = []
for i in range(lenonecode):
            xarray.append(0)
            yarray.append(0 + i)
print("xarray", xarray, "yarray", yarray)
x = np.array(xarray)
y = np.array(yarray)

# 이름 배열 설정
namelist = mm.getName()

# xyz 설정 
zarray = []
xplus = 0
for i in namelist:
    zarray = mm.getPricesPer(i)
    z = zarray
    xplus += 1
    ax.plot(x + xplus, y, z)
    
print ("마지막 x 배열", x, "마지막 z 배열", z)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
print ("출력완료!!!")
