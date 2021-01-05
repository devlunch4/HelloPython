from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import time

# 크롤링할 사이트 설정
html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  

# 해당 html의 값 에서 html 타입으로 parser (변환/해석)
soup = BeautifulSoup(html, "html.parser") 

# 페이지에서 해당 클래스 찾기
findclass = soup.select('.st2')

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

# 실질적 데이터 가져오고 INSERT
for td in findclass:
    # findclass 수량 만큼 반복이 되는데 반복수에서 해당 st2 클래스에서 a 태그내 title을 가져오면 종목번호
    s_code = td.find(['a']).get('title')
    # findclass 에서의 텍스트 값만 가져오면 이름
    s_name = td.text
    # findclass 에서의 부모태그를 찾아 거기서 2번째 td 의 텍스트 값만 가져오면 가격, 콤마 제거
    s_price = td.parent.select('td')[1].text.replace(",", "")
    in_time = time.strftime('%Y%m%d.%H%M')
    # SQL문 실행
    # INSERT
    sql = "INSERT INTO stock (s_code, s_name, s_price, in_time) VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (s_code, s_name, s_price, in_time,))
    print(s_code, s_name, s_price, in_time, "INSERT 완료")
    
# 커밋
conn.commit()
print("커밋 완료")

# 데이타 Fetch
result = cursor.fetchall()
print(result)

conn.close()
print("최종 완료")
