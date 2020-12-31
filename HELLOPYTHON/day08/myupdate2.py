import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    user='root',
    passwd='java',
    host='127.0.0.1',
    db='python',
    charset='utf8'
)

# try catch UPDATE
try:
    with conn.cursor() as cursor:
        sql = "UPDATE sample SET col03 = %s WHERE col01 = %s"
        cursor.execute(sql, (5,4,))
        conn.commit()
        print(cursor.rowcount) # 1 (affected rows)s

finally:
    conn.close()
