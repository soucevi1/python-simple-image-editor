#!/usr/bin/env python3

from PyQt4.QtGui import *
from PyQt4 import uic, QtGui

qtCreatorFile = "crop_window.ui"
 
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Crop_editor(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
