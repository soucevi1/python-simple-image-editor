#!/usr/bin/env python3

from PIL import Image
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import numpy as np
import crop_editor as ce

# Class that represents the crop editor
class Crop:

    # Empty constructor
    def __init__(self):
        self.image_data = None
        
    # Constructor with img argument
    def __init__(self, img):
        """
        The constructor takes PIL Image array as argument.
        It creates a special window containing four text input fields
        It also displays the current image size
        """
        self.image_data = img
        self.crop_window = ce.Crop_editor()

        self.validator = QtGui.QIntValidator(1, 999999)
        
        self.rowLine = self.crop_window.rowLineEdit
        self.colLine = self.crop_window.colLineEdit
        self.numRowsLine = self.crop_window.newRowLineEdit
        self.numColsLine = self.crop_window.newColLineEdit
        
        self.rowLine.setValidator(self.validator)
        self.colLine.setValidator(self.validator)
        self.numRowsLine.setValidator(self.validator)
        self.numColsLine.setValidator(self.validator)
                
        self.actCols, self.actRows = self.image_data.size
        
        self.crop_window.cropSizeLabel.setText("Current image size: " + str(self.actCols) + " x " + str(self.actRows))
        
        self.errLabel = self.crop_window.errorCropLabel
        self.errLabel.setStyleSheet('color: red')
        
        self.crop_window.cropOKButton.clicked.connect(self.input_check)
        self.crop_window.exec_()

    # Method that verifies the input
    def input_check(self):
        """
        The method checks whether the text boxes are empty, 
        whether the top-left corner coordinates are in the array bounds,
        whether the new size is at least one pixel
        and whether the whole crop area is within the array bounds.
        """
        self.row = self.rowLine.text()
        if self.row == '':
            self.errLabel.setText("Row box cannot be empty")
            return
            
        self.col = self.colLine.text()        
        if self.col == '':
            self.errLabel.setText("Col box cannot be empty")    
            return
            
        self.numRows = self.numRowsLine.text()
        if self.numRows == '':
            self.errLabel.setText("Row count box cannot be empty")
            return 
            
        self.numCols = self.numColsLine.text()
        if self.numCols == '':
            self.errLabel.setText("Column count box cannot be empty")
            return
        
        self.row = int(self.row)
        self.col = int(self.col)
        self.numRows = int(self.numRows)
        self.numCols = int(self.numCols)
        
        if self.row > self.actRows:
            self.errLabel.setText("Starting row is outside the picture")                
        elif self.col > self.actCols:
            self.errLabel.setText("Starting column is outside the picture")
        elif (self.numRows + self.row) > self.actRows:
            self.errLabel.setText("Row size out of bounds")
        elif (self.numCols + self.col) > self.actCols:
            self.errLabel.setText("Column size out of bounds") 
        elif self.numRows < 1:
            self.errLabel.setText("Row size too low")
        elif self.numCols < 1:
            self.errLabel.setText("Column size too low")                        
        else:
            self.crop_adjust()
            
    # Method that applies the given crop area
    def crop_adjust(self):
        """
        The method converts the PIL Image data to Numpy array.
        It creates a crop out of the original picture.
        Then it takes the coordinates of top-left corner of the crop area 
        and the size of the desired crop area.
        At last it converts the Numpy array to PIL Image
        """
        img = self.image_data
        data = np.asarray(img)
        
        data_out = np.empty((self.numRows, self.numCols))
        
        data_out = data[self.row:self.row+self.numRows:, self.col:self.col+self.numCols:, :]

        self.image_data = Image.fromarray(data_out, 'RGB')
        self.crop_window.accept()
