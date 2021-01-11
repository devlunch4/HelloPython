import numpy as np
import matplotlib.pyplot as plt
import pymysql
import time


class MyManager:

    def __init__(self):
        self.conn = pymysql.connect(user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
    
    def setlinexy(self):
        print("setline 진입")
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = '삼성전자' ORDER BY in_time DESC;"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return len(rows)
    
    def getScode(self):
        print("getName 진입")
        sql = "SELECT DISTINCT(s_code) FROM stock;"
        self.cursor.execute(sql)
        namerows = self.cursor.fetchall()
        return namerows
    
    def getPricesPer(self, s_code):
        sql = "SELECT s_code, s_price in_time FROM stock WHERE s_code = %s ORDER BY in_time"
        self.cursor.execute(sql, (s_code,))
        rows = self.cursor.fetchall()
        prices = []

        for row in rows:
            zerobreak = rows[0][1]
            pvalue = row[1]
            if zerobreak == 0:
                zerobreak = 1
                pvalue = 1
            prices.append((pvalue - zerobreak) / zerobreak * 100)
        return prices


start = time.time()
print("시작시간 :", start)
mm = MyManager()

fig = plt.figure()
ax = fig.gca(projection='3d')

lenonecode = int(mm.setlinexy())
xarray = []
yarray = []         
zarray = []
for i in range(lenonecode):
            xarray.append(0)
            yarray.append(0 + i)
print("xarray", len(xarray), "yarray", len(yarray))
x = np.array(xarray)
y = np.array(yarray)

codelist = mm.getScode()

zarray = []
xplus = 0
for i in codelist:
    print(i)
    zarray = mm.getPricesPer(i)
    z = zarray
    xplus += 1
    ax.plot(x + xplus, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

end = time.time()
elapse = end - start
print("끝난시간 :", end)
print("걸린시간 :", elapse)
print ("출력완료!!!")
plt.show()
