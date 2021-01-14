# XOR problem
# 입력 2 - 히든 16 - 출력 1, 잘 학습됨. 
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

EPOCHS=2000 # 훈련 회수
# XOR 입력 변수, 4가지 상태
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
# XOR 출력 변수, 같으면 0, 다르면 1이 되어야 함.
target_data = np.array([[0],[1],[1],[0]], "float32")
# 모델 생성
model = Sequential()
# 히든 레이어, 2개 입력의 16개 노드
model.add(Dense(16, input_shape=(2,), activation='relu'))
# 출력 레이어, 1개의 출력 노드
model.add(Dense(1, activation='sigmoid'))
# optimizer : sgd, adam, ... 등을 사용할 수 있다. 변경하면서 테스트 가능
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
# 그래프 출력을 위하여 계산 과정을 history에 저장한다.
print("not training :",model.predict(training_data))

# verbose를 1로 주면 훈련 과정을 출력한다.
history = model.fit(training_data, target_data, 
                    epochs=EPOCHS, verbose=0)
# 입력에 따른 훈련값을 출력해 본다.
print("trained :",model.predict(training_data[3:]))

# loss 출력
#model.evaluate(training_data, target_data, steps=2)