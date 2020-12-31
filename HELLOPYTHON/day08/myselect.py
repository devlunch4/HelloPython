import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    user='root',
    passwd='java',
    host='127.0.0.1',
    db='python',
    charset='utf8'
)

# Connection 으로부터 Cursor 생성
# Cursor는 자바의 ps(prepareStatement)와 비슷
cursor = conn.cursor()
cursorx = conn.cursor(pymysql.cursors.DictCursor)

# SQL문 실행 SELECT
sql = "SELECT * FROM sample;"
cursor.execute(sql)
cursorx.execute(sql)

# 데이타 Fetch
result = cursor.fetchall()
resultx = cursorx.fetchall()
print(result)
# print(result[0])
# print(result[1])
# print(result[2])
# 
# print(resultx)
# print(resultx[0])
# print(resultx[1])
# print(resultx[2])


# Connection 닫기
conn.close()

