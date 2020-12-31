import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    user='root',
    passwd='java',
    host='127.0.0.1',
    db='python',
    charset='utf8'
)

# try catch DELETE
try:
    with conn.cursor() as cursor:
        sql = "DELETE FROM sample  WHERE col01 = %s"
        cursor.execute(sql, (4,))
        conn.commit()
        print(cursor.rowcount) # 1 (affected rows)s

finally:
    conn.close()
