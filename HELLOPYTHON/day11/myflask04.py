from flask import Flask
from flask import request
from flask.templating import render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/param', methods=['GET', 'POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name', 'POST기본값')
    # name = request.args.get('name', 'user01')
    if request.method == "GET":
        name = request.args.get('name', 'GET기본값')
    return "param = " + name


@app.route('/forward.do')
def forward():
    title = "Good Morning"
    return render_template('myflask03forward.html', title=title)


@app.route('/db.do')
def db():
    # _code_db select >> 화면에 뿌려주기
    return render_template("myflask04db.html", title="gogo", list={1, 2, 3})


@app.route('/selectdb.do')
def selectdb():
    # _code_db select >> 화면에 뿌려주기
    conn = pymysql.connect(user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8')
    cursor = conn.cursor()
    # cursorx = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT s_code, s_name, s_price, in_time FROM stock ORDER BY s_code, in_time"
    cursor.execute(sql)
    # cursorx.execute(sql)

    rows = cursor.fetchall()

    print(rows)
    # print(rowsx)
    conn.close()
    
    return render_template("myflask04selectdb.html", rows=rows)


if __name__ == '__main__':
    app.run()
