#!/usr/bin/env python3

from PIL import Image
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import numpy as np
import shrink_editor as se


# Class that represents the shrinking editor
class Shrink:

    # Empty constructor
    def __init__(self):
        self.image_data = None
        
    # Constructor with the argument img    
    def __init__(self, img):
        """
        Constructor takes PIL Image data as an argument.
        It creates a special window that contains two text input fields.
        The upper field takes the numerator and the lower one takes the denominator.
        Nominator and denominator are then used to form a fraction. This fraction
        represents the new size of the image. The numerator cannot be higher than the 
        denominator. Neither of them can be zero.
        """
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

    # Method that verifies the input
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
            
    # Method that edits the size of the picture
    def shrink_adjust(self):
        """
        The method converts PIL Image to Numpy array.
        With the nominator (NOM) and denominator (DEN) read from the user, 
        it divides the rows and columns to groups of DEN pixels and always assigns
        first NOM pixels of every group to the output.
        Note that this means that although 1/2 and 49/98 are the same number, the output of both
        is different.
        At first, the method counts the indexes of the pixels that will be assigned to the output.
        Then it copies the pixels to the output array and converts it back to PIL Image
        """
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
