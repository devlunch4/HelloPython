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

# SQL문 실행 SELECT
sql = "SELECT s_code, s_name, s_price, in_time FROM stock WHERE s_name = '삼성전자' ORDER BY in_time DESC;"
cursor.execute(sql)

# 데이타 Fetch
rows = cursor.fetchall()
print(rows)
prices = []
for row in rows:
    prices.append(row[0])
    print(row[0])

# Connection 닫기
conn.close()
