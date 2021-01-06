from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import time

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

cnt = 0;
# while 활용 반복
while True:
    # 크롤링할 사이트 설정
    html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  
    # 해당 html의 값 에서 html 타입으로 parser (변환/해석)
    soup = BeautifulSoup(html, "html.parser") 
    # 페이지에서 해당 클래스 찾기
    tds = soup.select('.st2')
    # 시간 설정
    in_time = time.strftime('%Y%m%d.%H%M')
    # 실질적 데이터 가져오고 INSERT
    for td in tds:
        # tds 수량 만큼 반복이 되는데 반복수에서 해당 st2 클래스에서 a 태그내 title을 가져오면 종목번호
        s_code = td.find(['a']).get('title')
        # tds 에서의 텍스트 값만 가져오면 이름
        s_name = td.text
        # tds 에서의 부모태그를 찾아 거기서 2번째 td 의 텍스트 값만 가져오면 가격, 콤마 제거
        s_price = td.parent.select('td')[1].text.replace(",", "")
        
        # SQL문 실행
        # INSERT
        sql = "INSERT INTO stock (s_code, s_name, s_price, in_time) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, (s_code, s_name, s_price, in_time,))
        # print(s_code, s_name, s_price, in_time, "INSERT 완료")
    
    conn.commit()
    print("커밋 완료 : ", cnt)
    cnt += 1
    time.sleep(60)
    if cnt > 5:
        break

# 데이타 Fetch
result = cursor.fetchall()
print(result)

conn.close()
print("최종 완료")
