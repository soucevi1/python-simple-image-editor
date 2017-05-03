#!/usr/bin/env python3

from PIL import Image
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import numpy as np
import sys
import time
import shrink_editor as se

# uzivatel zada cislo, kolikrat se obrazek zmensi
# cislo se pote prepocita na koeficient, ktery rekne, kolikaty pixel se vzdy ma vynechat
# prepocet: pokud se ma obrazek zmensit na n/m puvodni velikosti
#   n pixelu nechat, (m-n) pixelu vzit


class Shrink:

    def __init__(self):
        self.image_data = None
        
    def shrink_initialize(self, img):
        self.image_data = img
        self.shrink_window = se.Shrink_editor()

        self.validator = QtGui.QIntValidator(1, 100)
        self.numeratorLine = self.shrink_window.resizeNumerator
        self.denominatorLine = self.shrink_window.resizeDenominator
        self.numeratorLine.setValidator(self.validator)
        self.denominatorLine.setValidator(self.validator)
        
        self.errLabel = self.shrink_window.resizeErrorLabel
        self.errLabel.setStyleSheet('color: red')
        
        self.shrink_window.resizeOKButton.clicked.connect(self.input_check)
        self.shrink_window.exec_()

    def input_check(self):
        self.num = int(self.numeratorLine.text())
        self.denom = int(self.denominatorLine.text())
        if self.num > self.denom:
            self.errLabel.setText("Numerator cannot be higher than denominator")                
        elif self.num == 0:
            self.errLabel.setText("Numerator cannot be zero")
        elif self.denom == 0:
            self.errLabel.setText("Denominator cannot be zero")
        else:
            self.shrink_adjust()
            

    def shrink_adjust(self):
        img = self.image_data
        data = np.asarray(img) 
        data_out = data[::2, ::2, :] #zmenseni
        data_out = np.asarray(data_out, dtype=np.uint8)
        img_out = Image.fromarray(data_out, 'RGB')
        return img_out
