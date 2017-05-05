#!/usr/bin/env python3

from PIL import Image
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import numpy as np
import sys
import time
import custom_cf_editor as cce

def greyscale(img):    
    data = np.asarray(img)
    data_out = [0.299, 0.587, 0.114] * data
    data_out = data_out[:, :, 0] + data_out[:, :, 1] + data_out[:, :, 2] # R+G+B
    data_out = np.asarray(data_out, dtype = data.dtype) # conversion float -> uint8              
    data_out_RGB = to_RGB(data_out)
    img_out = Image.fromarray(data_out_RGB, 'RGB')
    return img_out
    
    
def invert(img):
    data = np.asarray(img)
    data_out = 255 - data
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out

    
# We need to convert Greyscale to RGB, so that it is compatible with other Editor's functions
# source: http://www.socouldanyone.com/2013/03/converting-grayscale-to-rgb-with-numpy.html    
def to_RGB(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, :] = img[:, :, np.newaxis]
    return ret
    
    
    
class Custom:

    def __init__(self):
        self.image_data = None
        
    def custom_initialize(self, img):
        self.image_data = img
        self.custom_cf_window = cce.Custom_editor()

        self.redSlider = self.custom_cf_window.redSlider
        self.blueSlider = self.custom_cf_window.blueSlider
        self.greenSlider = self.custom_cf_window.greenSlider
        
        self.redSlider.valueChanged.connect(self.value_change)
        self.blueSlider.valueChanged.connect(self.value_change)
        self.greenSlider.valueChanged.connect(self.value_change)                

        self.custom_cf_window.customCfOKButton.clicked.connect(self.custom_adjust)
        self.custom_cf_window.exec_()
            
    def value_change(self):
        self.redValue = self.redSlider.value()
        self.blueValue = self.blueSlider.value()
        self.greenValue = self.greenSlider.value()
        
        self.custom_cf_window.redLabel.setText(str(self.redValue))
        self.custom_cf_window.blueLabel.setText(str(self.blueValue))
        self.custom_cf_window.greenLabel.setText(str(self.greenValue))
    
    def custom_adjust(self):
        img = self.image_data
        data = np.asarray(img)
        data_out = np.empty(data.shape)
        
        data_out[::, ::, 0] = data[::, ::, 0] + self.redValue 
        data_out[::, ::, 1] = data[::, ::, 1] + self.greenValue
        data_out[::, ::, 2] = data[::, ::, 2] + self.blueValue

        data_out = data_out.clip(0,255)
        data_out = np.asarray(data_out, dtype=np.uint8)
        self.image_data = Image.fromarray(data_out, 'RGB')
        self.custom_cf_window.accept()
        
        
        
        
        
        
        
        
        
