# This program divide data into test set and training set.

import numpy as np
import random
from sklearn import preprocessing

# divide data into test set(20%) and training set(80%)
def divide_data(data):
    sep = int(len(data) * 0.8)
    train = []
    test = []
    for i in range(sep):
        train.append(data[i])
    
    for i in range(sep,len(data)):
        test.append(data[i])
    
    return (train,test)


data=np.loadtxt('data.txt')
# preprocessing data, scale every data to [-1,1]
X=data[:,0:11]
X = preprocessing.scale(X)
data[:,0:11] = X

a_3 = []
a_4 = []
a_5 = []
a_6 = []
a_7 = []
a_8 = []

for i in data:
	if i[-1] == 3:
		a_3.append(i)
	elif i[-1] == 4:
		a_4.append(i)
	elif i[-1] == 5:
		a_5.append(i)
	elif i[-1] == 6:
		a_6.append(i)
	elif i[-1] == 7:
		a_7.append(i)
	else:
		a_8.append(i)       

random.shuffle(a_3)
random.shuffle(a_4)
random.shuffle(a_5)
random.shuffle(a_6)
random.shuffle(a_7)
random.shuffle(a_8)

train_x_3, test_x_3 = divide_data(a_3)
train_x_4, test_x_4 = divide_data(a_4)
train_x_5, test_x_5 = divide_data(a_5)
train_x_6, test_x_6 = divide_data(a_6)
train_x_7, test_x_7 = divide_data(a_7)
train_x_8, test_x_8 = divide_data(a_8)

train = []
test = []

train += train_x_3
train += train_x_4
train += train_x_5
train += train_x_6
train += train_x_7
train += train_x_8


test += test_x_3
test += test_x_4
test += test_x_5
test += test_x_6
test += test_x_7
test += test_x_8

np.savetxt('train_data.txt', train, delimiter = ' ', newline = '\n', fmt='%.6f')
np.savetxt('test_data.txt', test, delimiter = ' ', newline = '\n', fmt='%.6f')
