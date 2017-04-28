#!/usr/bin/env python3

import numpy as np
from PIL import Image

def flip_horizontal(img):    
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    for i in range(0, cols-1):
        data_out = data[::-1, ::, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out


def flip_vertical(img):    
    data = np.asarray(img)
    rows, cols, colors = data.shape
    data_out = np.empty((cols, rows, colors), dtype = data.dtype)
    
    for i in range(0, cols-1):
        data_out = data[::, ::-1, ::]          
           
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
