import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QIcon, QSize
from dask.dataframe.tests.test_rolling import idx

form_class = uic.loadUiType("omok05.ui")[0]


class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_ab = True
        self.flag_playing = True
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.icon3 = QIcon('3.png')
        self.arr2pb = []
        self.arr2d = [
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                    
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                     [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0]
                     
                     ]
        
        for y in range(0,19):
            line = []
            for x in range(0,19):
                button = QPushButton("", self)
                button.setGeometry(x * 40, y * 40, 40, 40)
                button.setIconSize(QSize(40, 40))   
                button.setIcon(self.icon0)
                button.setToolTip(str(y)+","+str(x))
                button.clicked.connect(self.pb_click)
                line.append(button)
            self.arr2pb.append(line)
        self.myrender()
        self.pbreset.clicked.connect(self.reset)
        
        
    def myrender(self): 
                for y in range(19):
                    for x in range(19):
                        if self.arr2d[y][x] == 0:
                            self.arr2pb[y][x].setIcon(self.icon0)
                            if y == 3 or y ==9 or y == 15 :
                                if x == 3 or x== 9 or  x== 15:
                                    self.arr2pb[y][x].setIcon(self.icon3)    
                            
                        elif self.arr2d[y][x] == 1:
                            self.arr2pb[y][x].setIcon(self.icon1)
                        elif self.arr2d[y][x] == 2:
                            self.arr2pb[y][x].setIcon(self.icon2)
    
        
    def pb_click(self):
        if not self.flag_playing:
            return
        loc = self.sender().toolTip()
        locs = loc.split(",")


        
        y = int(locs[0])
        x = int(locs[1])
        
        if self.arr2d[y][x] > 0:
            return 
        
        stone_info = 0
        
        if self.flag_ab==True: 
            self.flag_ab=False           
            self.arr2d[y][x]=1
            stone_info = 1
        else:
            self.flag_ab=True
            self.arr2d[y][x]=2
            stone_info = 2
        
        up = self.getUP(y,x,stone_info)
        dw = self.getDW(y,x,stone_info)
        le = self.getLE(y,x,stone_info)
        ri = self.getRI(y,x,stone_info)
         
        ur = self.getUR(y,x,stone_info)
        ul = self.getUL(y,x,stone_info)
        dr = self.getDR(y,x,stone_info)
        dl = self.getDL(y,x,stone_info)
                 
        print("up",up,"dw",dw,"le",le,"ri",ri)
         
        print("ur",ur,"ul",ul,"dr",dr,"dl",dl)
        
        d1=up + dw + 1
        d2=le + ri + 1
        d3=ur + dl + 1
        d4=ul + dr + 1
        
        self.myrender()        
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.flag_ab:                
                QMessageBox.about(self, "Omok", "흑돌 승")
            else:
                QMessageBox.about(self, "Omok", "백돌 승")
            self.flag_playing = False
        
        
    def getUP(self,y,x,stone_info):
        cnt = 0
        while True:
            y = y-1
            if y < 0:
                return cnt
            if x < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt
            
    def getDW(self,y,x,stone_info):
        cnt = 0
        while True:
             
            y = y+1
            if x < 0:
                return cnt
            if y < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt

    def getLE(self,y,x,stone_info):
        cnt = 0
        while True:
             
            x = x-1
            if x < 0:
                return cnt
            if y < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt
            
    def getRI(self,y,x,stone_info):
        cnt = 0
        while True:
             
            x = x+1
            if x < 0:
                return cnt
            if y < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt

    def getUR(self,y,x,stone_info):
        cnt = 0
        while True:
            y = y-1
            x = x+1
            if x < 0:
                return cnt
            if y < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt
            
    def getUL(self,y,x,stone_info):
        cnt = 0
        while True:
            y = y-1
            x = x-1
            if x < 0:
                return cnt
            if y < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt            

    def getDR(self,y,x,stone_info):
        cnt = 0
        while True:
            y = y+1
            x = x+1
            if x < 0:
                return cnt
            if y < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt
            
    def getDL(self,y,x,stone_info):
        cnt = 0
        while True:
            y = y+1
            x = x-1
            if y < 0:
                return cnt
            if x < 0:
                return cnt
            try:
                if self.arr2d[y][x] == stone_info:
                    cnt +=1
                else:
                    return cnt
            except:
                return cnt  
                                  
    def reset(self):
            self.flag_ab = True
            self.flag_playing = True                            
            for y in range(19):
                for x in range(19):
                    self.arr2d[y][x] = 0
                    
            self.myrender()                      
if __name__ == "__main__":
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 

    myWindow.show()

    app.exec_()
    
