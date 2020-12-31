import time
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
cursor = conn.cursor()
count = 0
# INSERT
sql = "INSERT INTO sample (col01, col02, col03) VALUES (%s,%s,%s);"

start = time.time()

for i in range(3000):
    cnt = cursor.execute(sql, (i, 4, 4,))
    count += 1
    # print("count:", count, "cnt:", cnt,)

conn.commit()
end = time.time()
elapse = end - start

print("시작시간 :", start, "끝난시간 ", end)
print("걸린시간 :", elapse)

