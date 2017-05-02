#!/usr/bin/env python3

from PIL import Image
import numpy as np
import brightness_editor as be

def brightness(img):
    brightness_window = be.Brightness_editor()
    brightness_window.show()
    data = np.asarray(img, dtype = np.uint16)  #prevod kvuli preteceni
    data_out = 3 * data # zesvetleni
    data_out = data_out.clip(0,255) # orezani rozsahu na 0-255 kvuli preteceni pri nasobeni
    data_out = np.asarray(data_out, dtype=np.uint8)
    img_out = Image.fromarray(data_out, 'RGB')
    return img_out
