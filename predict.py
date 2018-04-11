#!/usr/bin/python3
# -*- coding: utf-8  -*-
import cv2
from keras.utils import plot_model
from keras.applications.vgg16 import VGG16
from  keras.preprocessing.image import img_to_array
from  keras.preprocessing.image import load_img
import keras
from keras.models import Sequential
from keras.utils import plot_model
from keras.layers import Conv2D,MaxPooling2D
from keras import backend as K
from keras.layers import Dense,Dropout,Flatten
from keras.models import Sequential
import numpy as np


def predict():

  model=Sequential()
  model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28,28,1)))
  model.add(Conv2D(64,(3,3),activation='relu'))
  model.add(MaxPooling2D(pool_size=(2,2)))
  model.add(Dropout(0.25))
  model.add(Flatten())
  model.add(Dense(128,activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(10,activation='softmax'))

  return model

if __name__ == "__main__":

  #ここにOPEN CVいれる





  image_path ='trimming.png'
  img = load_img(image_path, grayscale = True, target_size=(28,28))
  x=img_to_array(img)
  x /= 255
  x = np.expand_dims(x,axis=0)
  print(x.shape)


  #深層学習のモデルを定義
  model = predict()
  model.summary()
  model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
  model.load_weights('mnist.h5')

  features = model.predict_classes(x, batch_size=32)
  print(features)
  #print(np.argmax(features))


