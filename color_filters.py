#!/usr/bin/env python3

from PIL import Image
import numpy as np
import custom_cf_editor as cce

# Function that converts image to greyscale
def greyscale(img):    
    """
    The function converts the PIL Image to Numpy array.
    The color compounds are multiplied by magical constants 
    that repersent weights of the colors as perceived by the human eye.
    All the compounds are then added together.
    The output data is then converted to RGB in order to be compatible 
    with the rest of the program.
    At last the output is converted back to PIL Image.
    """
    data = np.asarray(img)
    data_out = [0.299, 0.587, 0.114] * data
    data_out = data_out[:, :, 0] + data_out[:, :, 1] + data_out[:, :, 2]
    data_out = np.asarray(data_out, dtype = data.dtype)
    data_out_RGB = to_RGB(data_out)
    img_out = Image.fromarray(data_out_RGB, 'RGB')
    return img_out
    
# Function that inverts the colors of the image    
def invert(img):
    """
    The function converts the PIL Image to Numpy array.
    It substracts all the color compounds from 255. 
    This means that all the pixels have the opposite color than they had before.
    The output is converted back to PIL Image
    """
    data = np.asarray(img)
    data_out = 255 - data
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out

    
# Function that converts greyscale image to RGB
def to_RGB(img):
    """
    The function adds a new axis (representing color compounds) 
    to the 2D array of greyscale image.
    All three color compounds have the same value.
    
    Source: http://www.socouldanyone.com/2013/03/converting-grayscale-to-rgb-with-numpy.html    
    """
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, :] = img[:, :, np.newaxis]
    return ret
    
    
# Class representing custom color balancing
class Custom:

    # Empty constructor
    def __init__(self):
        self.image_data = None
        
    # Constructor with img argument
    def __init__(self, img):
        """
        The constructor takes PIL Image as an argument. 
        It creates a special window containing three sliders for R, G and B.
        It also connects the appropriate functions to them.
        """
        self.image_data = img
        self.custom_cf_window = cce.Custom_editor()

        self.redSlider = self.custom_cf_window.redSlider
        self.blueSlider = self.custom_cf_window.blueSlider
        self.greenSlider = self.custom_cf_window.greenSlider
        
        self.redSlider.valueChanged.connect(self.value_change)
        self.blueSlider.valueChanged.connect(self.value_change)
        self.greenSlider.valueChanged.connect(self.value_change)                

        self.custom_cf_window.customCfOKButton.clicked.connect(self.custom_adjust)
        self.custom_cf_window.exec_()
        
    # Method that detects a change of the slider value        
    def value_change(self):
        self.redValue = self.redSlider.value()
        self.blueValue = self.blueSlider.value()
        self.greenValue = self.greenSlider.value()
        
        self.custom_cf_window.redLabel.setText(str(self.redValue))
        self.custom_cf_window.blueLabel.setText(str(self.blueValue))
        self.custom_cf_window.greenLabel.setText(str(self.greenValue))
    
    # Method that applies the custom color filter
    def custom_adjust(self):
        """
        The method converts the PIL Image to Numpy array.
        It uses values read from the sliders.
        These values are then added to the corresponding color 
        compounds contained in the input data.
        The output is then converted to uint8 in order to prevent overflowing of the pixels
        and then back to PIL Image
        """
        img = self.image_data
        data = np.asarray(img, dtype = np.uint16)
        data_out = np.empty(data.shape)
        
        data_out[::, ::, 0] = data[::, ::, 0] + self.redValue 
        data_out[::, ::, 1] = data[::, ::, 1] + self.greenValue
        data_out[::, ::, 2] = data[::, ::, 2] + self.blueValue

        data_out = data_out.clip(0,255)
        data_out = np.asarray(data_out, dtype=np.uint8)
        self.image_data = Image.fromarray(data_out, 'RGB')
        self.custom_cf_window.accept()
