import requests
import json
# 카카오 검색 영역 >> 카페
url = "https://dapi.kakao.com/v2/search/cafe"
# 검색어
queryString = {"query":"아이유"}
# 개발자 키 값
header = {'authorization':'KakaoAK 5538994d5ffa3de221ffdc494e637777'}
# 리퀘스트 요청 설정
r = requests.get(url, params=queryString, headers=header)

jsonobj = json.loads(r.text)
docs = jsonobj.get("documents")

for i in docs:
    print ("cafename", ":", i.get("cafename"), end=" ")
    print ("contents", ":", i.get("contents"), end=" ")
    print ("datetime", ":", i.get("datetime"), end=" ")
    print ("thumbnail", ":", i.get("thumbnail"), end=" ")
    print ("title", ":", i.get("title"), end=" ")
    print ("url", ":", i.get("url"))

