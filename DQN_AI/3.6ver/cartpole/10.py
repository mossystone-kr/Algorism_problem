import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import random
import numpy as np
import datetime
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '-1'

data_cnt = 100
random.seed(0)  #테스트를 위해!

x_data = []
for i in range(data_cnt):
    x_data.append([random.randint(7, 20), random.randint(80, 130)])
    x_data.append([random.randint(1, 10), random.randint(50, 100)])

y_data = []
for i in range(data_cnt):
    y_data.append(1)
    y_data.append(0)

X_train = np.array(x_data)
Y_train = np.array(y_data)

model = Sequential()
model.add(Dense(20, input_dim=2, activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

now = datetime.datetime.now()
hist = model.fit(X_train, Y_train, epochs=200, batch_size=10, validation_data=(X_train, Y_train))
print('elapsed: ', datetime.datetime.now() - now)

# 모델 평가 및 분석

x_data = []
for i in range(10):
    x_data.append([random.randint(7, 20), random.randint(80, 130)])
    x_data.append([random.randint(1, 10), random.randint(50, 100)])

y_data = []
for i in range(10):
    y_data.append(1)
    y_data.append(0)

X_test = np.array(x_data)
Y_test = np.array(y_data)

loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=1)

print('')
print('loss:', str(loss_and_metrics[0]))
print('accuracy', str(loss_and_metrics[1]))

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train_loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()