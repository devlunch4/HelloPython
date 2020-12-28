import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("callbutton.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 버튼에 기능을 연결하는 코드
        self.pb0.clicked.connect(self.pb_click)
        self.pb1.clicked.connect(self.pb_click)
        self.pb2.clicked.connect(self.pb_click)
        self.pb3.clicked.connect(self.pb_click)
        self.pb4.clicked.connect(self.pb_click)
        self.pb5.clicked.connect(self.pb_click)
        self.pb6.clicked.connect(self.pb_click)
        self.pb7.clicked.connect(self.pb_click)
        self.pb8.clicked.connect(self.pb_click)
        self.pb9.clicked.connect(self.pb_click)
        self.pbreset.clicked.connect(self.pbreset_click)
        self.pbcall.clicked.connect(self.pbcall_click)

    # pb 눌리면 작동할 함수 >> 클릭시 해당범위 값 모두 더함.
    def pb_click(self):
        txt_old = self.le1.text()
        txt_new = self.sender().text()
        self.le1.setText(txt_old + txt_new)

    def pbreset_click(self):
        self.le1.setText("")
        self.le1.setStyleSheet("QLineEdit"
                        "{"
                        "background : none;"
                        "}")
    
    def pbcall_click(self):
        print("call")
        txt_old = self.le1.text()
        QMessageBox.about(self, "calling", txt_old)
        self.le1.setStyleSheet("QLineEdit"
                        "{"
                        "background : yellow;"
                        "}")


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = MyWindow()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
