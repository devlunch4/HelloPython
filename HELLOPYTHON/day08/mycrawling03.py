from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8081/HELLOWEB/crawl.jsp")  

print(html)
print(">>>!")

# 해당 html의 값 에서 html 타입으로 parser (변환/해석)
soup = BeautifulSoup(html, "html.parser") 
print(soup)  # 웹 문서 전체가 출력됩니다. 

tds = soup.select("td")
for i in tds:
    print("tds",":", i)
