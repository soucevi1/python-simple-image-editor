#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import editor 




app = QtGui.QApplication(sys.argv)
window = editor.Editor()
window.show()
window.actionOpen.triggered.connect(window.open_file)
window.actionRotateLeft.triggered.connect(window.turn_left)
window.actionRotateRight.triggered.connect(window.turn_right)
window.actionFlipHorizontalAxis.triggered.connect(window.flip_horizontal)
window.actionFlipVerticalAxis.triggered.connect(window.flip_vertical)
window.actionColorFiltersGreyscale.triggered.connect(window.filter_greyscale)
window.actionColorFiltersInvert.triggered.connect(window.filter_invert)
window.actionBrightness.triggered.connect(window.brightness)

sys.exit(app.exec_())

