import numpy as np
import pandas as pd
import keras
import tensorflow as tf
from IPython.display import display
#import PIL
from tensorflow.python.client import device_lib
from keras import models, layers
from keras import Input
from keras.models import Model, load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras import optimizers, initializers, regularizers, metrics
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import BatchNormalization, Conv2D, Activation, Dense, GlobalAveragePooling2D, MaxPooling2D, ZeroPadding2D, Add
import os
import matplotlib.pyplot as plt
import math
from keras.models import load_model
from selenium import webdriver

def testdir(filedir):
    # 분류 모델 불러오기
    model = load_model('res_net50modelWpatience_camp7.h5')


    labels ={}
    for s,i in enumerate(open('labels.csv',encoding = 'utf-8').read().split('\n')):
        if s == 392:
            break
        name = i.split(',')
        labels[name[0]] = name[1]


    # 예측할 이미지 전처리
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory('img', batch_size=16, target_size=(224, 224), color_mode='rgb')
    output=model.predict_generator(test_generator)
    print(labels.get(str(output.argmax())))
    place=labels.get(str(output.argmax()))
    
    # 크롬 드라이버 실행
    driver = webdriver.Chrome("chromedriver.exe")
    # 구글지도 이동
    url = "http://www.google.com/maps/"
    driver.get(url)

    # 검색창에 "카페" 입력하기 
    searchbox = driver.find_element_by_css_selector("input#searchboxinput") 
    if place=='campus7':
        place='SAC아트홀'
    searchbox.send_keys(place) 

    # 검색버튼 누르기 
    searchbutton = driver.find_element_by_css_selector("button#searchbox-searchbutton") 
    searchbutton.click()

    return place