import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import keras.optimizers
from keras.datasets import mnist
from sklearn import preprocessing 

if __name__ == "__main__":
  # Load Mnist data
  (train_x, train_y), (test_x, test_y) = mnist.load_data()

  # Display data information
  print('train data records = ', len(train_x))
  print('test data records = ', len(test_x))
  print(train_x.shape)
  print(train_y.shape)

  # Display image of hand written number.
  plot_image(train_x[10])
  print('Label:' , str(train_y[10]))

  # Vectorization
  X_train = train_x.reshape(len(train_x), 28*28).astype('float32')
  X_test = test_x.reshape(len(test_x), 28*28).astype('float32')

  # Perform Standardization.
  X_train = preprocessing.scale(X_train)
  X_test = preprocessing.scale(X_test)

  # Convert Y to one-hot vector
  Y_train = np_utils.to_categorical(train_y)
  Y_test = np_utils.to_categorical(test_y)


  # Define the NN:
  model = Sequential()

  # First layer, 100 hidden units
  model.add(Dense(100, input_shape=(28*28,)))
  model.add(Activation('elu'))
  model.add(Dropout(0.25))
  # 2nd layer, 100 hidden units
  model.add(Dense(100))
  model.add(Activation('elu'))
  model.add(Dropout(0.25))

  # 3rd layer
  model.add(Dense(100))
  model.add(Activation('elu'))
  model.add(Dropout(0.25))

  # output layer
  model.add(Dense(len(Y_train[0])))
  model.add(Activation('softmax'))

  Ada = keras.optimizers.Adagrad(lr=0.01, epsilon=None, decay=0.0)
  model.compile(loss = 'categorical_crossentropy', optimizer=Ada, metrics=['accuracy'])

  # Perform training & CV
  model.fit(X_train, Y_train, epochs = 64, batch_size=128, validation_data=(X_test, Y_test))


def plot_image(img):
  fig = plt.gcf()
  plt.imshow(img)
  plt.show