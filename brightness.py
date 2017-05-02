#!/usr/bin/env python3

from PIL import Image
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import numpy as np
import brightness_editor as be
import sys
import time


class Brightness:
    def __init__(self):
        self.image_data = None
        self.value = 0
        self.slider = None

    def brightness_initialize(self, img):
        self.image_data = img
        self.brightness_window = be.Brightness_editor()
        self.slider = self.brightness_window.horizontalBrightnessSlider 
        self.value = self.slider.valueChanged.connect(self.value_change)
        self.brightness_window.brOKButton.clicked.connect(self.brightness_adjust)
        self.brightness_window.exec_()
        
        
    def value_change(self):
        self.value = self.slider.value()
        
        
    def brightness_adjust(self):
        img = self.image_data
        coef = self.value
        data = np.asarray(img, dtype = np.uint16)  #prevod kvuli preteceni
        if coef > 0:
            coef = coef + 1
            data_out = coef * data # zesvetleni
        elif coef < 0:
            coef = coef - 1
            data_out = 1/(-coef) * data #ztmaveni
        else:
            data_out = data
        data_out = data_out.clip(0,255) # orezani rozsahu na 0-255 kvuli preteceni pri nasobeni
        data_out = np.asarray(data_out, dtype=np.uint8)
        img_out = Image.fromarray(data_out, 'RGB')
        self.image_data = img_out
        self.brightness_window.accept()
