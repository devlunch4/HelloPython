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

# UPDATEs
sql = "UPDATE sample SET col03 = 4 WHERE col01 = 5"
cursor.execute(sql)
conn.commit()

result = cursor.rowcount

print(result)
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])

# Connection 닫기
conn.close()
