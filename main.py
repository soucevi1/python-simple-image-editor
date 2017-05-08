#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import editor 



# Create Qt application
app = QtGui.QApplication(sys.argv)

# Create the main window
window = editor.Editor()
window.show()

# Connect the Editor methods to the buttons of the main window
window.actionOpen.triggered.connect(window.open_file)
window.actionSave.triggered.connect(window.save_file)
window.actionSaveAs.triggered.connect(window.save_file_as)

window.actionRotateLeft.triggered.connect(window.turn_left)
window.actionRotateRight.triggered.connect(window.turn_right)

window.actionCrop.triggered.connect(window.crop)

window.actionFlipHorizontalAxis.triggered.connect(window.flip_horizontal)
window.actionFlipVerticalAxis.triggered.connect(window.flip_vertical)

window.actionColorFiltersGreyscale.triggered.connect(window.filter_greyscale)
window.actionColorFiltersInvert.triggered.connect(window.filter_invert)
window.actionColorFiltersCustom.triggered.connect(window.filter_custom)

window.actionBrightness.triggered.connect(window.brightness)

window.actionResize.triggered.connect(window.shrink)

window.actionConvolution.triggered.connect(window.convolution)

# Execute the Qt application
sys.exit(app.exec_())

