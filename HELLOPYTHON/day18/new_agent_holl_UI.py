import numpy as np
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential
from collections import deque
from random import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


def build_model():
	model = Sequential()
	model.add(Dense(10, input_dim=1, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(10, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(2, activation='linear', kernel_initializer='he_uniform'))
	model.compile(loss='mse', optimizer=Adam(lr=0.001))
	return model


form_class = uic.loadUiType("gameholjak.ui")[0]


class MyWindow(QMainWindow, form_class):

	def __init__(self):
		self.score = 0
		self.sq = 0
		
		super().__init__()
		self.setupUi(self)
		self.pb_hol.clicked.connect(self.pbHolClick)
		self.pb_jak.clicked.connect(self.pbJakClick)
		


		
	def pbHolClick(self):
		self.mySelect(0)
	
	def pbJakClick(self):
		self.mySelect(1)

	def mySelect(self, mine):
		print("mySelect 진입--------------------------")
		
		model = build_model()
		model.summary()
			
		numpy_mine = np.array([mine])
		numpy_mine = np.reshape(numpy_mine, [1, 1])
		numpy_mine = np.float32(numpy_mine)
		q_values = model.predict(numpy_mine)
		com = np.argmax(q_values[0])
		self.sq += 1
		if mine == 0:
			self.le_me.setText("홀")
		elif mine == 1:
			self.le_me.setText("짝")
		if com == 0:
			self.le_com.setText("홀")
		elif com == 1:
			self.le_com.setText("짝")
		if mine == com:
			self.score += 1
			self.le_result.setText("승리")
		else:
			self.le_result.setText("패배")
		
		self.le_score.setText(str(self.score))
		self.le_sq.setText(str(self.sq))
	


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = MyWindow()
	myWindow.show()
	app.exec_()
