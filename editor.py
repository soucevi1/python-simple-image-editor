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

qtCreatorFile = "main_window.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Class that represents the Editor (main window of the program) 
class Editor(QtGui.QMainWindow, Ui_MainWindow):

    # Empty constructor
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.__filename = None
        self.__image_file = None
        self.__qimage = None
        self.filters = 'Image files (*.bmp *.png *.jpg)'        
 
    # Method that opens the image file
    def open_file(self):        
        """
        The method displays the file dialog with filters applied (only image files are visible).
        After the user choses the file, it opens it as PIL Image and shows it.
        """
        file_dialog = QFileDialog(self)
        self.__filename = file_dialog.getOpenFileName(None, 'Open File', '', self.filters)
        if self.__filename != '':
            self.__image_file = Image.open(self.__filename)
            self.__format = self.__image_file.format
            self.show_image()
            
    # Method that saves the currently opened image
    def save_file(self):
        """
        The method simply saves the image using an inbuilt PIL method
        """
        if self.__image_file != None:
            self.__image_file.save(self.__filename, self.__format)

    # Method that saves the currently opened image            
    def save_file_as(self):
        """
        The method opens the file dialog and prompts the user to enter the new name
        for the file to be saved as. 
        Then it uses the PIL inbuilt method to save it.
        """
        if self.__image_file != None:
            file_dialog = QFileDialog(self)
            self.__filename = file_dialog.getSaveFileName(None, 'Save File As...', '', self.filters)
            if self.__filename != '':
                self.__image_file.save(self.__filename, self.__format)

    # Method that shows the image in the label in the main window
    def show_image(self):
        """
        The method gets the PIL Image converted to Qt pixmap and then
        sets it to the label.
        """
        pixmap = self.pil_to_qpixmap()
        self.labelImage.setPixmap(pixmap)

    # Method that converts PIL Image to Qt QPixmap
    def pil_to_qpixmap(self):
        """
        The method converts the PIL Image to byte array. The array is then used together
        with the original picture dimensions as an argument of the QImage constructor.
        The QImage is used to create the QPixmap.
        """
        w, h = self.__image_file.size
        data = self.__image_file.tobytes("raw", "BGRX")
        self.__qimage = QtGui.QImage(data, w, h, QtGui.QImage.Format_RGB32)
        pix = QtGui.QPixmap.fromImage(self.__qimage)
        return pix

    # Method that turns the image left
    def turn_left(self):
        """
        The method calls turn.turn_image_left() on the image data and then shows the result
        """
        if self.__image_file != None:
           	self.__image_file = turn.turn_image_left(self.__image_file)
           	self.show_image()
    
    # Method that turns the picture right
    def turn_right(self):
        """
        The method calls turn.turn_image_right() on the image data and then shows the result
        """
        if self.__image_file != None:
            self.__image_file = turn.turn_image_right(self.__image_file)
            self.show_image()
        
    # Method that flips the image using its horizontal axis
    def flip_horizontal(self):
        """
        The method calls flip.flip_horizontal() on the image data and then shows the result
        """
        if self.__image_file != None:
            self.__image_file = flip.flip_horizontal(self.__image_file)
            self.show_image()

    # Method that flips the image using its vertical axis
    def flip_vertical(self):
        """
        The method calls flip.flip_vertical() on the image data and then shows the result
        """
        if self.__image_file != None:
            self.__image_file = flip.flip_vertical(self.__image_file)
            self.show_image()
    
    # Method that crops the picture
    def crop(self):
        """
        The method creates an instance of crop.Crop, uses it to create the new image data and 
        show the result.
        """
        if self.__image_file != None:
            cropEdit = crop.Crop(self.__image_file)
            self.__image_file = cropEdit.image_data
            self.show_image()
        
    # Method that applies greyscale filter on the image data
    def filter_greyscale(self):
        """
        The method calls color_filters.greyscale() on the image data and then shows the result
        """
        if self.__image_file != None:
            self.__image_file = cf.greyscale(self.__image_file)
            self.show_image()
        
    # Method that inverts the colors of the image data
    def filter_invert(self):
        """
        The method calls color_filters.invert() on the image data and then shows the result
        """
        if self.__image_file != None:
            self.__image_file = cf.invert(self.__image_file)
            self.show_image()
        
    # Method that applies custom color filter on the image data
    def filter_custom(self):
        """
        The method creates an instance of color_filters.Custom and uses it to modify
        the image data. Then it shows the result.
        """
        if self.__image_file != None:
            cfCustomEdit = cf.Custom(self.__image_file)
            self.__image_file = cfCustomEdit.image_data
            self.show_image()
        
    # Method that adjusts the brightness of the image data
    def brightness(self):
        """
        The method creates an instance of brightness.Brightness and uses it to modify
        the image data. Then it shows the result.
        """
        if self.__image_file != None:
            brEdit = brightness.Brightness(self.__image_file)
            self.__image_file = brEdit.image_data
            self.show_image()
        
    # Method that adjusts the size of the image
    def shrink(self):
        """
        The method creates an instance of shrink.Shrink and uses it to modify
        the image data. Then it shows the result.
        """
        if self.__image_file != None:
            shEdit = shrink.Shrink(self.__image_file)
            self.__image_file = shEdit.image_data
            self.show_image()
        
    # The method that applies the convolution mask to the image data
    def convolution(self):
        """
        The method creates an instance of convolution.Convolution and uses it to modify
        the image data. Then it shows the result.
        """
        if self.__image_file != None:
            convEdit = convolution.Convolution(self.__image_file)
            self.__image_file = convEdit.image_data
            self.show_image()
