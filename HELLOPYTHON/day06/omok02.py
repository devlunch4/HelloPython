import sys

from PyQt5 import QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tkinter.constants import BUTT

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok02.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.icon0 = QIcon("0.png")
        self.icon1 = QIcon("1.png")
        self.icon2 = QIcon("2.png")
        self.arrpb = []
        self.arr2d = [
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                     ]
        
        for y in range(0, 10):
            for x in range(0, 10):
                # creating a push button 
                button = QPushButton("", self)
                # setting geometry of button 
                button.setGeometry((x * 40), 20 + (y * 40), 40, 40)
                # set icon size
                button.setIconSize(QtCore.QSize(40, 40))
                # setting icon to the button image
                button.setIcon(self.icon0) 
                # setting click event
                button.clicked.connect(self.pb_click)
                # setting click event
                self.arrpb.append(button)
        self.myrender()
    
    def myrender(self):
        print("myrender")
        
        for y in range(10):
            for x in range(10):
                idx = y * 10 + x
                if self.arr2d[y][x] == 0:
                    self.arrpb[idx].setIcon(self.icon0)
                elif self.arr2d[y][x] == 1:
                    self.arrpb[idx].setIcon(self.icon1)
                elif self.arr2d[y][x] == 2:
                    self.arrpb[idx].setIcon(self.icon2)

    def pb_click(self):
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
