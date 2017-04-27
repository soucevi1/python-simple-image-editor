#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
import editor 




app = QtGui.QApplication(sys.argv)
window = editor.Editor()
window.show()
fileOpen = window.actionOpen
fileOpen.triggered.connect(window.open_file)
window.show_image()



sys.exit(app.exec_())

