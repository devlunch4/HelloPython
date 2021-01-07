from flask import Flask
import requests

app = Flask(__name__)

 
# 접속자 설정 및 촤표 값 설정
def getLatLng(address):
    result = ""
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '5538994d5ffa3de221ffdc494e637777'
    
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        result_address = r.json()["documents"][0]["address"]
        
        result = result_address["y"], result_address["x"]
    else:
        result = "ERROR[" + str(r.status_code) + "]"
    return result

 
# 지도 API html 언어로 만들기
def getKakaoMapHtml(address_latlng):
    rest_api_key = '5538994d5ffa3de221ffdc494e637777'
    result = ""
    result += "<div id='map' style='width:1200px;height:1000px;display:inline-block;'></div>" + "\n"
    result += "<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + rest_api_key + "'></script>" + "\n"
    result += "<script>" + "\n"
    result += "    var container = document.getElementById('map'); " + "\n"
    result += "    var options = {" + "\n"
    result += "           center: new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ")," + "\n"
    result += "           level: 3" + "\n"
    result += "    }; " + "\n"
    result += "    var map = new kakao.maps.Map(container, options); " + "\n"
    result += "    var markerPosition  = new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ");  " + "\n"
    result += "    var marker = new kakao.maps.Marker({position: markerPosition}); " + "\n"
    result += "    var zoomControl = new kakao.maps.ZoomControl(); " + "\n"
    result += "    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT); " + "\n"
    result += "    var mapTypeControl = new kakao.maps.MapTypeControl(); " + "\n"
    result += "    map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT); " + "\n"
    result += "    marker.setMap(map); " + "\n"
    result += "</script>" + "\n"
    
    # 파일생성 같은 경로내 HTML 생성 >> 생성후 Dynamic Web Project에 생성된 WebContent html을 넣는다
    with open('C:/Users/PC-20/git/HelloPython/HELLOWEB/WebContent/kakaomap.html', 'w') as html_file:
        html_file.write(result)
    return result


# main()
if __name__ == "__main__":
    # 주소 설정 
    address = "대전 서구 대덕대로 211"
    # 해당 주소에 따른 좌표 설정 및 카카오 REST API로 좌표 구하기
    address_latlng = getLatLng(address)
    # 좌표로 지도 첨부 HTML 생성
    if str(address_latlng).find("ERROR") < 0:
        map_html = getKakaoMapHtml(address_latlng)
    # print(map_html)
    else:
        print("에러 발생 [ERROR]getLatLng")
    print("HELLOWEB 프로젝트 내 WebContent에 kakaomap.html 생성/수정 완료!")
