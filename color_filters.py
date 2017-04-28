#!/usr/bin/env python3

import numpy as np
from PIL import Image

def greyscale(img):    
    data = np.asarray(img)
    data_out = [0.299, 0.587, 0.114] * data
    data_out = data_out[:, :, 0] + data_out[:, :, 1] + data_out[:, :, 2] # R+G+B
    data_out = np.asarray(data_out, dtype = data.dtype) # conversion float -> uint8              
    data_out_RGB = to_RGB(data_out)
    img_out = Image.fromarray(data_out_RGB, 'RGB')
    return img_out
    
    
# We need to convert Greyscale to RGB, so that it is compatible with other Editor's functions
# source: http://www.socouldanyone.com/2013/03/converting-grayscale-to-rgb-with-numpy.html    
def to_RGB(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, :] = img[:, :, np.newaxis]
    return ret
