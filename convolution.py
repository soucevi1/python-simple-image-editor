#!/usr/bin/env python3

from PIL import Image
import numpy as np
import convolution_editor as ce
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui

# Class that represents the convolution editor
class Convolution:

    # Empty constructor
    def __init__(self):
        self.image_data = None
        self.maskLine = []
        self.mask = []
        
    # Constructor with img argument    
    def __init__(self, img):
        """
        The constructor takes the PIL Image data as an arguments. 
        It creates a special window containing 9 text slots and a few 
        radio buttons with preset values.
        The input allowed to the text slots is float that is up to 3 characters long.
        """
        self.image_data = img
        self.conv_window = ce.Convolution_editor()

        self.validator = QtGui.QDoubleValidator(-99, 99, 2)
        
        self.mask = []
        self.maskLine = []
        
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
        
        self.conv_window.sharpenButton.clicked.connect(self.setSharpen)
        self.conv_window.simpleEdgeButton.clicked.connect(self.setSimpleEdge)
        self.conv_window.edgeButton.clicked.connect(self.setEdge)
        self.conv_window.blurButton.clicked.connect(self.setBlur)
        self.conv_window.excessiveButton.clicked.connect(self.setExcessive)
        self.conv_window.embossButton.clicked.connect(self.setEmboss)
        
        self.conv_window.convOKButton.clicked.connect(self.convolution_adjust)
        self.conv_window.exec_()
  
    # Sharpen preset
    def setSharpen(self):
        self.maskLine[0].setText("0")
        self.maskLine[1].setText("-1")
        self.maskLine[2].setText("0")
        self.maskLine[3].setText("-1")
        self.maskLine[4].setText("5")
        self.maskLine[5].setText("-1")
        self.maskLine[6].setText("0")
        self.maskLine[7].setText("-1")
        self.maskLine[8].setText("0")

    # Simple Edge Detection preset
    def setSimpleEdge(self):
        self.maskLine[0].setText("0")
        self.maskLine[1].setText("1")
        self.maskLine[2].setText("0")
        self.maskLine[3].setText("1")
        self.maskLine[4].setText("-4")
        self.maskLine[5].setText("1")
        self.maskLine[6].setText("0")
        self.maskLine[7].setText("1")
        self.maskLine[8].setText("0")
        
    # Edge detection preset
    def setEdge(self):
        self.maskLine[0].setText("1")
        self.maskLine[1].setText("1")
        self.maskLine[2].setText("1")
        self.maskLine[3].setText("1")
        self.maskLine[4].setText("-8")
        self.maskLine[5].setText("1")
        self.maskLine[6].setText("1")
        self.maskLine[7].setText("1")
        self.maskLine[8].setText("1")
        
    # Blur preset
    def setBlur(self):
        self.maskLine[0].setText("0")
        self.maskLine[1].setText("0.2")
        self.maskLine[2].setText("0")
        self.maskLine[3].setText("0.2")
        self.maskLine[4].setText("0.2")
        self.maskLine[5].setText("0.2")
        self.maskLine[6].setText("0")
        self.maskLine[7].setText("0.2")
        self.maskLine[8].setText("0")
        
    # Excessive Edges preset
    def setExcessive(self):
        self.maskLine[0].setText("1")
        self.maskLine[1].setText("1")
        self.maskLine[2].setText("1")
        self.maskLine[3].setText("1")
        self.maskLine[4].setText("-7")
        self.maskLine[5].setText("1")
        self.maskLine[6].setText("1")
        self.maskLine[7].setText("1")
        self.maskLine[8].setText("1")
        
    # Emboss preset
    def setEmboss(self):
        self.maskLine[0].setText("-1")
        self.maskLine[1].setText("-1")
        self.maskLine[2].setText("0")
        self.maskLine[3].setText("-1")
        self.maskLine[4].setText("0")
        self.maskLine[5].setText("1")
        self.maskLine[6].setText("0")
        self.maskLine[7].setText("1")
        self.maskLine[8].setText("1")        

    # Method that applies the convolution mask
    def convolution_adjust(self):
        """
        The method converts the PIL Image to Numpy uint16 array.
        It applies the convolution mask using Numpy broadcasting.
        All the 9 parts of the mask are applied simultaneously to the whole input array
        The output is then converted to uint8 in order to prevent pixel overflowing and
        then back to PIL Image.
        """
        img = self.image_data
        data = np.asarray(img)
        
        data_out = np.empty(data.shape, dtype=np.uint16)
        
        self.mask = []
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
