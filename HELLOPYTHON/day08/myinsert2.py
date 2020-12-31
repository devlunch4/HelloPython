import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    user='root',
    passwd='java',
    host='127.0.0.1',
    db='python',
    charset='utf8'
)

# try catch INSERT
try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO sample (col01, col02, col03) VALUES (%s, %s, %s)"
        cursor.execute(sql, (4, 4, 4,))
        conn.commit()
        print(cursor.lastrowid)

finally:
    conn.close()
