import json
import requests

# 카카오 검색 영역 >> 카페
url = "https://dapi.kakao.com/v2/search/cafe"
# 검색어
subj = "아이유"
# 개발자 키 값
apikey = "5538994d5ffa3de221ffdc494e637777"

# 리퀘스트 요청 설정
r = requests.get(url, params={'query':subj}, headers={'Authorization': 'KakaoAK ' + apikey })
# # js 변수에 가져온 값을 설정
# js = json.JSONEncoder().encode(r.json())
# # for 문 돌려서 출력
# for i in r.json()["documents"]:
#     print (i["title"])
#     print (i["url"])
#     print (i["datetime"])
#     print (i["contents"])

print(json.loads(r.text))