#!/usr/bin/env python3

import numpy as np
from PIL import Image

# Function that flips the image using its horizontal axis
def flip_horizontal(img):
    """
    The function takes the original picture, 
    reverts its columns and uses it as a new row in the output
    """
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    data_out = data[::-1, ::, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out

# Function that flips the image using its vertical axis
def flip_vertical(img):    
    """
    The function takes the original image and
    reverts its rows.
    """
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    data_out = data[::, ::-1, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
