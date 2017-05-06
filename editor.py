#!/usr/bin/env python3

from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
from PIL import Image
from PIL.ImageQt import ImageQt
import turn
import flip
import brightness
import shrink
import convolution
import crop
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
        self.filters = 'Image files (*.bmp *.png *.jpg)'        
 
    def open_file(self):        
        file_dialog = QFileDialog(self)
        self.__filename = file_dialog.getOpenFileName(None, 'Open File', '', self.filters)
        if self.__filename != '':
            self.__image_file = Image.open(self.__filename)
            self.__format = self.__image_file.format
            self.show_image()

    def save_file(self):
        if self.__image_file != None:
            self.__image_file.save(self.__filename, self.__format)
            
    def save_file_as(self):
        if self.__image_file != None:
            file_dialog = QFileDialog(self)
            self.__filename = file_dialog.getSaveFileName(None, 'Save File As...', '', self.filters)
            if self.__filename != '':
                self.__image_file.save(self.__filename, self.__format)

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
        if self.__image_file != None:
           	self.__image_file = turn.turn_image_left(self.__image_file)
           	self.show_image()
    
    def turn_right(self):
        if self.__image_file != None:
            self.__image_file = turn.turn_image_right(self.__image_file)
            self.show_image()
        
    def flip_horizontal(self):
        if self.__image_file != None:
            self.__image_file = flip.flip_horizontal(self.__image_file)
            self.show_image()

    def flip_vertical(self):
        if self.__image_file != None:
            self.__image_file = flip.flip_vertical(self.__image_file)
            self.show_image()
    
    def crop(self):
        if self.__image_file != None:
            cropEdit = crop.Crop(self.__image_file)
            self.__image_file = cropEdit.image_data
            self.show_image()
        
    def filter_greyscale(self):
        if self.__image_file != None:
            self.__image_file = cf.greyscale(self.__image_file)
            self.show_image()
        
    def filter_invert(self):
        if self.__image_file != None:
            self.__image_file = cf.invert(self.__image_file)
            self.show_image()
        
    def filter_custom(self):
        if self.__image_file != None:
            cfCustomEdit = cf.Custom(self.__image_file)
            self.__image_file = cfCustomEdit.image_data
            self.show_image()
        
    def brightness(self):
        if self.__image_file != None:
            brEdit = brightness.Brightness(self.__image_file)
            self.__image_file = brEdit.image_data
            self.show_image()
        
    def shrink(self):
        if self.__image_file != None:
            shEdit = shrink.Shrink(self.__image_file)
            self.__image_file = shEdit.image_data
            self.show_image()
        
    def convolution(self):
        if self.__image_file != None:
            convEdit = convolution.Convolution(self.__image_file)
            self.__image_file = convEdit.image_data
            self.show_image()
