import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
import random

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("evenoddgame.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.pb_click)

    # pb 눌리면 작동할 함수 >> 클릭시 해당범위 값 모두 더함.
    def pb_click(self):
        a = int(self.le1.text())
        
        if a % 2 == 1:
            a1 = "홀수"
            self.lb1a.setText(a1)    
        else:
            a1 = "짝수"
            self.lb1a.setText(a1)

        rnum = random.randint(1, 2)
        self.le2.setText(str(rnum))
        if rnum == 1:
            b = "홀수"
        else:
            b = "짝수"

        self.lb2a.setText(b)
            
        c = ""
        if a1 == b:
            c = "맞췄습니다"
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : green;"
                        "}")
        else:
            c = "틀렸습니다"
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : red;"
                        "}")
            
        self.le3.setText(str(c))

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = MyWindow()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()