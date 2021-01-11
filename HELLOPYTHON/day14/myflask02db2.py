from flask import Flask, render_template, request, jsonify
import pymysql
import json
import logging

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


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/param", methods=['GET', 'POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name', "kimchulsu")
    if request.method == "GET":
        name = request.args.get('name', "kimchulsu")  
    return "param=" + name


@app.route("/forward.do")
def forward():
    title = "Good Morning"
    return render_template('forward.html', title=title)


@app.route("/db.do")
def db():
    this_logger.debug("db 진입")
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    curs.execute("select emp_id,emp_name,nickname from emp")
    rows = curs.fetchall()
    conn.close()
    this_logger.debug(rows)
    return render_template('db2.html', title="good", list=[1, 2, 3], db_list=rows)


@app.route("/upd.ajax")
def ajax_upd():
    this_logger.debug("ajax_upd 진입")
    emp_id = request.args.get('emp_id')
    emp_name = request.args.get('emp_name')
    nickname = request.args.get('nickname')
    this_logger.debug("수정 값 >> 기존emp_id : %s, emp_name : %s, nickname : %s", emp_id, emp_name, nickname)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("UPDATE emp SET nickname = '" + nickname + "', emp_name = '" + emp_name + "' WHERE emp_id = '" + emp_id + "'")
    # 0 비정상
    # 1 정상
    # cursor.execute(sql, (5,4,))
    conn.commit()
    conn.close()
    obj = {"cnt": cnt} 
    json_return = json.dumps(obj)
    this_logger.debug("ajax_upd 종료")
    return jsonify(json_return)
    
    
@app.route("/ins.ajax")
def ajax_ins():
    this_logger.debug("ajax_ins 진입")
    #emp_id = request.args.get('emp_id')
    emp_name = request.args.get('emp_name')
    nickname = request.args.get('nickname')
    this_logger.debug("추가 값 >> 기존emp_id : 자동생성됨, emp_name : %s, nickname : %s", emp_name, nickname)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "INSERT INTO emp (emp_name, nickname) VALUES (%s, %s)"
    cnt = curs.execute(sql, (emp_name, nickname))
    # 0 비정상
    # 1 정상
    # cursor.execute(sql, (5,4,))
    conn.commit()
    conn.close()
    obj = {"cnt": cnt} 
    json_return = json.dumps(obj)
    this_logger.debug("ajax_ins 종료")
    return jsonify(json_return)
    
    
@app.route("/del.ajax")
def ajax_del():
    this_logger.debug("ajax_del 진입")
    emp_id = request.args.get('emp_id')
    emp_name = request.args.get('emp_name')
    nickname = request.args.get('nickname')
    this_logger.debug("삭제 값 >> 기존emp_id : %s, emp_name : %s, nickname : %s", emp_id, emp_name, nickname)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "DELETE FROM emp WHERE emp_id = %s"
    cnt = curs.execute(sql, (emp_id))
    # 0 비정상
    # 1 정상
    # cursor.execute(sql, (5,4,))
    conn.commit()
    conn.close()
    obj = {"cnt": cnt} 
    json_return = json.dumps(obj)
    this_logger.debug("ajax_del 종료")
    return jsonify(json_return)


if __name__ == "__main__":
    app.run()
