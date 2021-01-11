import logging

from flask import Flask, render_template
import pymysql

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


@app.route("/chart.do")
def chart():
    this_logger.debug("db 진입")
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    curs.execute("select s_code,s_name,s_price, in_time from stock GROUP BY s_code ORDER BY in_time LIMIT 200")
    rows = curs.fetchall()
    conn.close()
    this_logger.debug(rows)
    return render_template('chart.html', db_list=rows)


if __name__ == "__main__":
    app.run()
