from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8081/HELLOWEB/crawl.jsp")  

print(html)
print(">>>!")

# 해당 html의 값 에서 html 타입으로 parser (변환/해석)
soup = BeautifulSoup(html, "html.parser") 
print(soup)  # 웹 문서 전체가 출력됩니다. 

# soup 페이지에서 td가 들어간 것을 모두 찾는다
soupfind = (soup.find_all("td"))
print(soup.find_all("td"))

# soupfind = (soup.table.text)
print(soupfind)
# for 문으로 해당 텍스트를 모두 출력한다
for i in range(soupfind.__len__()):
    print(soupfind[i].get_text())

# len() 함수를 사용하여 배열 길이 확인후  텍스트를 모두 출력한다
for i in range(len(soupfind)):
    print(soupfind[i].get_text())

tds = soup.find("td")
for i in tds:
    print("tds : ",i)
    
