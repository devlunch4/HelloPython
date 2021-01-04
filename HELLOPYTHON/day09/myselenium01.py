import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from selenium import webdriver

# QT를 이용하여 로그인처리
# 창 띠우기
form_class = uic.loadUiType("myselenium01.ui")[0]

browser = webdriver.Chrome()
browser.get("http://localhost:8081/HELLOWEB/mycrawl")


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.pbFunction)

    # pb 눌리면 작동할 함수
    def pbFunction(self):
        print("버튼 클릭 진입")
        #자동 로그인 서블릿 호출
        browser.get("http://localhost:8081/HELLOWEB/mylogin")
        #크롤링할 서블릿 호출
        browser.get("http://localhost:8081/HELLOWEB/mycrawl")
        #크롤링 페이지에서 tr 태그 가져옴
        xxx = browser.find_element_by_tag_name('tr')
        ttt = xxx.text 
        self.label.setText(ttt)
        print(ttt)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = MyWindow()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
