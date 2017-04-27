#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
from PIL import Image

# zobrazeni hlavniho okna programu
qtCreatorFile = "main_window.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Editor(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.__image_file = None
 
    def open_file(self):        
        w = QWidget()
        filename = QFileDialog.getOpenFileName(w, 'Open File', '~')
        self.__image_file = Image.open(filename)
        print("opening " + filename)

    @property
    def image_file(self): 
        return self.__image_file

    @image_file.setter
    def image_file(self, value):
        self.__image_file = value

