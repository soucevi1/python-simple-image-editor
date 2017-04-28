#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
from PIL import Image
from PIL.ImageQt import ImageQt
import turn
import flip
import color_filters as cf

# zobrazeni hlavniho okna programu
qtCreatorFile = "main_window.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Editor(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.__filename = None
        self.__image_file = None
        self.__qimage = None
 
    def open_file(self):        
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilters(["Images (*.bmp *.png *.jpg)"])
        w = QWidget()
        self.__filename = file_dialog.getOpenFileName(w, 'Open File', '~')
        self.__image_file = Image.open(self.__filename)
        self.show_image()

    def show_image(self):
        pixmap = self.pil2qpixmap()
        self.labelImage.setPixmap(pixmap)

    def pil2qpixmap(self):
        w, h = self.__image_file.size
        data = self.__image_file.tobytes("raw", "BGRX")
        self.__qimage = QtGui.QImage(data, w, h, QtGui.QImage.Format_RGB32)
        qpixmap = QtGui.QPixmap(w,h)
        pix = QtGui.QPixmap.fromImage(self.__qimage)
        return pix

    def turn_left(self):
       	self.__image_file = turn.turn_image_left(self.__image_file)
        self.show_image()
    
    def turn_right(self):
        self.__image_file = turn.turn_image_right(self.__image_file)
        self.show_image()
        
    def flip_horizontal(self):
        self.__image_file = flip.flip_horizontal(self.__image_file)
        self.show_image()

    def flip_vertical(self):
        self.__image_file = flip.flip_vertical(self.__image_file)
        self.show_image()
        
    def filter_greyscale(self):
        self.__image_file = cf.greyscale(self.__image_file)
        self.show_image()
        
    @property
    def image_file(self): 
        return self.__image_file

    @image_file.setter
    def image_file(self, value):
        self.__image_file = value

