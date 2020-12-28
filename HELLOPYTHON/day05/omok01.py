import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok01.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for j in range(0, 10):
            for i in range(0, 10):
                # creating a push button 
                button = QPushButton("", self)
                # setting geometry of button 
                button.setGeometry((j * 40), 20 + (i * 40), 40, 40)
                # set icon size
                button.setIconSize(QtCore.QSize(40, 40))
                # setting icon to the button image
                button.setIcon(QIcon("0.png")) 
                button.clicked.connect(self.pb_click)
                #!!!! 앞에 SELF를 붙여서 전역 변수를 넣어준다.
        
    # 버튼에 기능을 연결하는 코드
        # self.pb.clicked.connect(self.pb_click)
        # self.lbl.clicked.connect(self.lbl_click)

    # pb 눌리면 작동할 함수 >> 클릭시 흰돌로 변경
    def pb_click(self):
    #     self.pb.setIcon(QtGui.QIcon("1.png"))
        print("pb_click")


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = MyWindow()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
