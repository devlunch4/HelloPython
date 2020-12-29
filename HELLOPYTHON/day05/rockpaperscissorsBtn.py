import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
import random

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("rockpaperscissorsBtn.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 버튼에 기능을 연결하는 코드
        self.pb1.clicked.connect(self.pb_click)
        self.pb2.clicked.connect(self.pb_click)
        self.pb3.clicked.connect(self.pb_click)

    # pb 눌리면 작동할 함수 >> 클릭시 해당범위 값 모두 더함. range를 활용 해당 시작 부터 해당 끝까지
    def pb_click(self):
        a = self.sender().text()
        print(a)
        self.le1.setText(a)
        
        com = random.randint(1, 3)
        print(com)
        comx = ""
        if com == 1:
            comx = "가위"
        elif com == 2:
            comx = "바위"
        elif com == 3:
            comx = "보"
          
        self.le2.setText(comx)
        print(comx)
        
        result = ""
        
        if a == comx: 
            result = "비겼습니다"
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : yellow;"
                        "}")
            
        elif (a == "가위" and comx == "보") or (a == "바위" and comx == "가위") or (a == "보" and comx == "바위"):
            result = "이겼습니다."
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : green;"
                        "}")
            
        else:
            result = "졌습니다."
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : red;"
                        "}")
        print(result)
        self.le3.setText(result) 


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = MyWindow()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
