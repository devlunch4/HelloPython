import logging
from flask import Flask, render_template
import pymysql

import numpy as np


complex_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(complex_formatter)
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("my.log", mode='a', encoding='utf-8')
file_handler.setFormatter(complex_formatter)
file_handler.setLevel(logging.DEBUG)

this_logger = logging.getLogger("parent.child")
this_logger.addHandler(console_handler)
this_logger.addHandler(file_handler)
this_logger.setLevel(logging.DEBUG)

app = Flask(__name__)


class MyManager:

    def __init__(self):
        self.conn = pymysql.connect(user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def getAllScode(self):
        print("getAllScode 진입")
        sql = "SELECT s_code FROM stock GROUP BY s_code"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        codes = []
        for i in result:
            codes.append(i[0])
        return codes
    
    def getPricesPerNumpyFromCode(self, s_code):
        sql = "SELECT s_price, in_time FROM stock WHERE s_code = %s ORDER BY in_time"
        self.cursor.execute(sql, (s_code,))
        result = self.cursor.fetchall()
        prices = []
        for row in result:
            prices.append((row[2]))
        return prices


@app.route("/chart.do")
def chart():
    this_logger.debug("chart 진입")
            
    mm = MyManager()
    codes = mm.getAllScode()
    
    zs = []
    cnt = 0
    for code in codes:
        cnt += 1
        print(cnt)
        zs.append(mm.getPricesPerNumpyFromCode(code))
        print(zs[0][0])

    print(zs[0][0])
    
    title = "dbtest"
    return render_template('chart.html', db_list=zs)


if __name__ == "__main__":
    app.run()

