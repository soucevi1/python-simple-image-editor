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



sys.exit(app.exec_())

