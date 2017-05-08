#!/usr/bin/env python3

from PIL import Image
import numpy as np
import brightness_editor as be


class Brightness:

    # Brightness class empty constructor
    def __init__(self):
        self.image_data = None
        self.value = 0
        self.slider = None

    # Brightness class constructor with arg
    def __init__(self, img):
        """
        Argument img contains Image data loaded using PIL. 
        Constructor creates special window containing a slider and a button 
        and calls functions connected to them 
        """
        self.image_data = img
        self.brightness_window = be.Brightness_editor()
        self.valueLabel = self.brightness_window.valueLabel
        self.slider = self.brightness_window.horizontalBrightnessSlider 
        self.value = self.slider.valueChanged.connect(self.value_change)
        self.brightness_window.brOKButton.clicked.connect(self.brightness_adjust)
        self.brightness_window.exec_()
        
    # Method detecting a change of the value of the slider    
    def value_change(self):
        self.value = self.slider.value()
        self.valueLabel.setText(str(self.value))
        
    # Method that adjusts image brightness    
    def brightness_adjust(self):
        """
        The method adjusts the brightness of the image using the value it reads from slider.
        The input data are converted to Numpy uint16 array.
        The function simply adds the slider value to all the color compounds.
        Result is converted back to uint8 and PIL Image
        """
        img = self.image_data
        coef = self.value
        data = np.asarray(img, dtype = np.uint16)
        data_out = data + coef
        data_out = data_out.clip(0,255)
        data_out = np.asarray(data_out, dtype=np.uint8)
        img_out = Image.fromarray(data_out, 'RGB')
        self.image_data = img_out
        self.brightness_window.accept()
