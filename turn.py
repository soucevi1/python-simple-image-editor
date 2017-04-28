#!/usr/bin/env python3

# Turn the picture

from PIL import Image
import numpy as np

def turn_image_left(img):
    data = np.asarray(img)
    rows, cols, colors = data.shape
    print(rows, cols, colors)
    data_out = np.empty((cols, rows, colors))
    for i in range(0,rows-1):
        for j in range(0,cols-1):
            data_out[j, i,:] = data[i, j, :]
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
