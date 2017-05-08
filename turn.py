#!/usr/bin/env python3

from PIL import Image
import numpy as np

# Function that turns the picture left
def turn_image_left(img):
    """
    The function takes PIL Image as an argument and converts it to Numpy array.
    Then it takes every column of the original picture from last to first and 
    puts them in rows of the output array.
    Array is then converted back to PIL Image
    """
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    for i in range(0, cols-1):
        data_out[i, ::, ::] = data[::, cols-1-i, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
    

# Function that turns the picture right    
def turn_image_right(img):
    """
    The function takes PIL Image as an argument and converts it to Numpy array.
    Then it takes every row of the original picture from last to first and 
    puts them in columns of the output array.
    Array is then converted back to PIL Image
    """
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    for i in range(0, rows-1):
        data_out[::, i, ::] = data[rows-1-i, ::, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
