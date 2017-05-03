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

        self.validator = QtGui.QIntValidator(1, 99)
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
        rows, cols, colors = data.shape
        resRows = []
        resCols = []
        
        ctr = 0
        for i in range(rows):
            if ctr < self.num:
                resRows.append(i)
            ctr = (ctr+1) % self.denom
        ctr = 0
        for i in range(cols):
            if ctr < self.num:
                resCols.append(i)
            ctr = (ctr+1) % self.denom    
        
        data_out = np.empty( (len(resRows), len(resCols), colors), dtype = np.uint8 )

        for i in range(len(resRows)):
            for j in range(len(resCols)):
                data_out[i, j, :] = data[resRows[i], resCols[j], :]

        data_out = np.asarray(data_out, dtype=np.uint8)
        self.image_data = Image.fromarray(data_out, 'RGB')
        self.shrink_window.accept()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
