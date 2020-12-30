# 1 새 Python 콘솔을 열어 다음과 같이 Python에 CUBRID Python 드라이버를 import한다.
import CUBRIDdb
# 2 localhost에 위치한 demodb 데이터베이스에 연결을 생성한다.
conn = CUBRIDdb.connect('CUBRID:localhost:30000:dba:::')

# demodb 데이터베이스는 비밀번호가 필요하지 않으므로 비밀번호를 입력하지 않았다. 
#그러나 실제 데이터베이스에 연결할 때에는 비밀번호가 필요하다면 비밀번호를 입력해야 한다. 
# connect () 함수의 구문은 다음과 같다.
#connect (url[,user[password]])


#INSERT 문 실행

#테이블이 비어있으므로 데이터를 입력한다. 먼저 커서를 얻은 후에 INSERT 문을 실행해야 한다


# Plain insert statement
print("# Plain insert statement");
cur = conn.cursor()
cur.execute("INSERT INTO posts (id, title, body, last_updated) VALUES (1, 'Title 1', 'Test body #1', CURRENT_TIMESTAMP)")
conn.commit()

# Parameterized insert statement
print("# Parameterized insert statement");
args = (2, 'Title 2', 'Test body #2')
cur.execute("INSERT INTO posts (id, title, body, last_updated) VALUES (?, ?, ?, CURRENT_TIMESTAMP)", args)

conn.commit()


#전체 레코드 조회
print("#전체 레코드 조회")
cur.execute("SELECT * FROM posts ORDER BY last_updated")
rows = cur.fetchall()
for row in rows:
    print (row)