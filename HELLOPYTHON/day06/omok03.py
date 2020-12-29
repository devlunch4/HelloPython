import sys
from tkinter.constants import BUTT

from PyQt5 import QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        self.arr2pb = []
        self.arr2d = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                     ]
        # 흰돌 검은돌 설정
        self.count = 0
        # 흰돌 검은돌 시작
        self.flag_wb = True
        
        for y in range(0, 10):
            line = []
            for x in range(0, 10):
                # creating a push button 
                button = QPushButton("", self)
                # setting geometry of button 
                button.setGeometry((x * 40), 20 + (y * 40), 40, 40)
                # set icon size
                button.setIconSize(QtCore.QSize(40, 40))
                # setting icon to the button image
                button.setIcon(self.icon0)
                # setting icon button tooltip
                button.setToolTip(str(y) + str(x))
                # setting click event
                button.clicked.connect(self.pb_click)
                line.append(button)
                # setting click event
            self.arr2pb.append(line)
        # background graphic set
        self.myrender()

    # background graphic set
    def myrender(self):
        print("myrender 진입")
        
        for y in range(10):
            for x in range(10):
                if self.arr2d[y][x] == 0:
                    self.arr2pb[y][x].setIcon(self.icon0)
                elif self.arr2d[y][x] == 1:
                    self.arr2pb[y][x].setIcon(self.icon1)
                elif self.arr2d[y][x] == 2:
                    self.arr2pb[y][x].setIcon(self.icon2)

    # click set bL WH 
    def pb_click(self):
        print("pb_click 진입")
        loc = self.sender().toolTip()
        y = int(loc[0])
        x = int(loc[1])
        print(loc, "y:", str(y), "x:", str(x))
        
        if self.arr2d[y][x] != 0:
            print("리턴")
            return 

        stone_info = 0;

        # if self.count % 2 == 0:
        if self.flag_wb:
            self.arr2d[y][x] = 1
            # self.count += 1
            stone_info = 1
            # self.flag_wb = False
        # elif self.count % 2 == 1:
        else:
            self.arr2d[y][x] = 2
            # self.count += 1
            stone_info = 2
            # self.flag_wb = True

        up = self.getUP(y, x, stone_info)
        dw = self.getDW(y, x, stone_info)

        le = self.getLE(y, x, stone_info)
        ri = self.getRI(y, x, stone_info)

        ur = self.getUR(y, x, stone_info)
        ul = self.getUL(y, x, stone_info)

        dr = self.getDR(y, x, stone_info)
        dl = self.getDL(y, x, stone_info)

        print("up", up, "dw", dw, "left", le, "rigit", ri)
        print("upright", ur, "upleft", ul, "dwright", dr, "dwleft", dl)
        # re graphic 
        self.myrender()
        # flag change value
        self.flag_wb = not self.flag_wb

        dialog = QMessageBox(self)
        dialog.setWindowTitle('결과')
        # dialog.setMinimumHeight(500)
        # dialog.setFixedHeight(500)
        # dialog.setFixedWidth(500)
        # dialog.setSizeIncrement(300, 300)
        # dialog.setSizeIncrement(1, 1)
        dialog.setSizeGripEnabled(True)

        if up + dw == 4 or le + ri == 4 or ur + ul == 4 or dr + dl == 4:
            if stone_info == 1:
                dialog.setText("백돌 승리")
                dialog.show()
            elif stone_info == 2:
                dialog.setText("흑돌 승리")
                dialog.show()

            for y in range(10):
                    for x in range(10):
                        self.arr2d[y][x] = 0
                        self.arr2pb[y][x].setIcon(self.icon0)

    def getDL(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            y += 1
            x += -1
            if y < 0:
                return cnt
            if x < 0:
                return cnt

            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getDR(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            y += 1
            x += 1
            if y < 0:
                return cnt
            if x < 0:
                return cnt
            
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getUL(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            y += -1
            x += -1
            if y < 0:
                return cnt
            if x < 0:
                return cnt

            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
        
    def getUR(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            y += -1
            x += 1
            if y < 0:
                return cnt
            if x < 0:
                return cnt
            
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getRI(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            x += 1
            if y < 0:
                return cnt
            if x < 0:
                return cnt
            
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getLE(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            x += -1
            if y < 0:
                return cnt
            if x < 0:
                return cnt

            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getDW(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            y += 1
            if y < 0:
                return cnt
            if x < 0:
                return cnt

            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getUP(self, y, x, stone_info):
        print(self, y, x, stone_info)
        cnt = 0
        while True:
            y += -1

            # up down '0'position error care
            if y < 0:
                return cnt
            if x < 0:
                return cnt

            try:
                if self.arr2d[y][x] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = MyWindow()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
