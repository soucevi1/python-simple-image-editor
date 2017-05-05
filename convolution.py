#!/usr/bin/env python3

from PIL import Image
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import numpy as np
import sys
import time
import convolution_editor as ce

# uzivatel zada cislo, kolikrat se obrazek zmensi
# cislo se pote prepocita na koeficient, ktery rekne, kolikaty pixel se vzdy ma vynechat
# prepocet: pokud se ma obrazek zmensit na n/m puvodni velikosti
#   n pixelu nechat, (m-n) pixelu vzit


class Convolution:

    def __init__(self):
        self.image_data = None
        self.maskLine = []
        self.mask = []
        
    def convolution_initialize(self, img):
        self.image_data = img
        self.conv_window = ce.Convolution_editor()

        self.validator = QtGui.QDoubleValidator(-99, 99, 0)
        
        self.maskLine.append(self.conv_window.convMask1)
        self.maskLine.append(self.conv_window.convMask2)
        self.maskLine.append(self.conv_window.convMask3)
        self.maskLine.append(self.conv_window.convMask4)
        self.maskLine.append(self.conv_window.convMask5)
        self.maskLine.append(self.conv_window.convMask6)
        self.maskLine.append(self.conv_window.convMask7)
        self.maskLine.append(self.conv_window.convMask8)
        self.maskLine.append(self.conv_window.convMask9)
        
        for i in range(9):
            self.maskLine[i].setValidator(self.validator)
        
        self.conv_window.convOKButton.clicked.connect(self.convolution_adjust)
        self.conv_window.exec_()
  

    def convolution_adjust(self):
        img = self.image_data
        data = np.asarray(img)
        rows, cols, colors = data.shape        
        cut = slice(1,-1), slice(1,-1)        
        data_real = data[cut]        
        
        for i in range(9):
            self.mask.append(float(self.maskLine[i].text()))
        
        data_out = (
            self.mask[0]*data[0:-2, 0:-2] + self.mask[1]*data[0:-2, 1:-1] + self.mask[2]*data[0:-2, 2:] +
            self.mask[3]*data[1:-1, 0:-2] + self.mask[4]*data[1:-1, 1:-1] + self.mask[5]*data[1:-1, 2:] +
            self.mask[6]*data[2:  , 0:-2] + self.mask[7]*data[2:  , 1:-1] + self.mask[8]*data[2:  , 2:]
        )
        data_out = data_out.clip(0,255)
        data_out = np.asarray(data_out, dtype=np.uint8)
        self.image_data = Image.fromarray(data_out, 'RGB')
        self.conv_window.accept()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
