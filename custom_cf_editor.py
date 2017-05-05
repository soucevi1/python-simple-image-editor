#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
from PIL import Image
from PIL.ImageQt import ImageQt

qtCreatorFile = "custom_cf_window.ui"
 
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Custom_editor(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
