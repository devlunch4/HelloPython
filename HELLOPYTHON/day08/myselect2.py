import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    user='root',
    passwd='java',
    host='127.0.0.1',
    db='python',
    charset='utf8'
)

# try catch SELECT
try:
    with conn.cursor() as cursor:
        #값이 4가 있는 것만 출력
        sql = "SELECT * FROM sample WHERE col01 = %s"
        cursor.execute(sql, (4,))
        result = cursor.fetchall()
        print(result)
        
        #모든 값 출력
        sql = "SELECT * FROM sample"
        cursor.execute(sql, ())
        result = cursor.fetchall()
        print(result)

finally:
    conn.close()
