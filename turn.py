#!/usr/bin/env python3

# Turn the picture

from PIL import Image
import numpy as np

def turn_image_left(img):
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    for i in range(0, cols-1):
        data_out[i, ::, ::] = data[::, cols-1-i, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
    
    
def turn_image_right(img):
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    for i in range(0, rows-1):
        data_out[::, i, ::] = data[rows-1-i, ::, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
    
    #    data_out = data[::-1, ::, ::]  TOTO JE FLIP!!!
