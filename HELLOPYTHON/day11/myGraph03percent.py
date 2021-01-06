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
        # SQL문 실행 SELECT
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = %s ORDER BY in_time"
        self.cursor.execute(sql, (s_name,))
        rows = self.cursor.fetchall()
        prices = []
        for row in rows:
            prices.append(row[2])
        return prices
    
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
        timex = []
        for row in rows:
            print("getPricesPer변화율:",row[1], "변화율 :", (row[2] - rows[0][2]) / rows[0][2] * 100, "시간 :", row[3])
            prices.append((row[2] - rows[0][2]) / rows[0][2] * 100)
        return prices
        
        for row in rows:
            timex.append(row[3])
        return timex
    
    def getPricesx(self, s_name):
    # SQL문 실행 SELECT
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = %s ORDER BY in_time"
        self.cursor.execute(sql, (s_name,))
        rows = self.cursor.fetchall()
        
        prices = []
        p_init = 0
        for idx, row in enumerate(rows):
            if idx == 0: 
                p_init = row[2]
            prices.append((row[2] - p_init) / p_init * 100)
            print("getPricesx변화율:",row[1], "변화율 :", (row[2] - p_init) / p_init * 100, "시간 :", row[3])
        return prices


# MyManager CALL
mm = MyManager()

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.array([0, 0, 0, 0, 0, 0])
y = np.array([0, 1, 2, 3, 4, 5])

z1 = np.array(mm.getPricesx('삼성전자'))
z2 = np.array(mm.getPricesx('LG'))
z3 = np.array(mm.getPricesx('SK'))

# plot test data
ax.plot(x, y, z1)
ax.plot(x + 1, y, z2)
ax.plot(x + 2, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
