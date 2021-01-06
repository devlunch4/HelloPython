import pymysql


# 함수화 
class MyManager:

    def __init__(self):
        self.conn = pymysql.connect(user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    def gePrices(self, s_name):
                # SQL문 실행 SELECT
        sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = %s ORDER BY in_time DESC;"
        self.cursor.execute(sql,(s_name,))
        rows = self.cursor.fetchall()
        prices = []
        for row in rows:
            prices.append(row[2])
        return prices

    
if __name__ == '__main__':
    mm = MyManager()
    prices = mm.gePrices('삼성전자')
    print(prices)
    prices = mm.gePrices('LG')
    print(prices)
