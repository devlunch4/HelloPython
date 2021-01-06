import numpy as np
import matplotlib.pyplot as plt

import pymysql


# 함수화 
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

# MyManager CALL
mm = MyManager()

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')



lenonecode = int(mm.setlinexy())
xarray = []
yarray = []         
zarray = []
for i in range(lenonecode):
            xarray.append(0)
            yarray.append(0 + i)
            
print("xarray",xarray, "yarray", yarray)
x = np.array(xarray)
y = np.array(yarray)

z1 = np.array(mm.getPrices('삼성전자'))
z2 = np.array(mm.getPrices('LG'))
z3 = np.array(mm.getPrices('SK'))
print("z3 pirxe:",z3)

print("mm.getName()", mm.getName())
print("len mm.getName()", len(mm.getName()))

namelist = mm.getName()
zarray = []

xplus = 0
for i in namelist:
    zarray = mm.getPrices(i)
    z = zarray
    ax.plot(x+xplus, y, z)
    xplus +=1
print ("최종",z)
# plot test data




# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
