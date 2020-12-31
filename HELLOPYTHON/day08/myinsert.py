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

# SQL문 실행
# INSERT
sql = "INSERT INTO sample (col01, col02, col03) VALUES (4,4,4);"
cursor.execute(sql)
conn.commit()

# select
sql = "SELECT * FROM sample;"
cursor.execute(sql)


# 데이타 Fetch
result = cursor.fetchall()

print(result)
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])

# Connection 닫기
conn.close()

