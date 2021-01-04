import requests

# 카카오 검색 영역 >> 카페
url = "https://dapi.kakao.com/v2/search/cafe"
# 검색어
queryString = {"query":"아이유"}
# 개발자 키 값
header = {'authorization':'KakaoAK 5538994d5ffa3de221ffdc494e637777'}
# 리퀘스트 요청 설정
r = requests.get(url, params=queryString, headers=header)

for i in r.json()["documents"]:
    print (i["title"])
    print (i["url"])
    print (i["datetime"])
    print (i["contents"])

