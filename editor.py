#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
from PIL import Image
from PIL.ImageQt import ImageQt

# zobrazeni hlavniho okna programu
qtCreatorFile = "main_window.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Editor(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.__image_file = Image.new("L", (1,1))
        self.__qimage = None
 
    def open_file(self):        
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilters(["Images (*.bmp *.png *.jpg)"])
        w = QWidget()
        filename = file_dialog.getOpenFileName(w, 'Open File', '~')
        self.__image_file = Image.open(filename)

    def show_image(self):
        self.PILimage_Qimage()
        self.labelImage.setPixmap(self.__qimage)
        self.labelImage.show()

    def PILimage_Qimage(self):
        qim = ImageQt(self.__image_file)
        self.__qimage = QtGui.QPixmap.fromImage(qim)

    @property
    def image_file(self): 
        return self.__image_file

    @image_file.setter
    def image_file(self, value):
        self.__image_file = value

