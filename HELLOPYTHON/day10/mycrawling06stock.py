from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  

# 해당 html의 값 에서 html 타입으로 parser (변환/해석)
soup = BeautifulSoup(html, "html.parser") 
# print(soup)  # 웹 문서 전체가 출력됩니다. 

# 페이지에서 해당 클래스 찾기
findclass = soup.select('.st2')

for td in findclass:
    # findclass 수량 만큼 반복이 되는데 반복수에서 해당 st2 클래스에서 a 태그내 title을 가져오면 종목번호
    s_code = td.find(['a']).get('title')
    # findclass 에서의 텍스트 값만 가져오면 이름
    s_name = td.text
    # findclass 에서의 부모태그를 찾아 거기서 2번째 td 의 텍스트 값만 가져오면 가격
    s_price = td.parent.select('td')[1].text
    # 출력
    print(s_code, s_name, s_price)
