#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *
from PyQt4 import uic, QtGui
 

# zobrazeni hlavniho okna programu
qtCreatorFile = "main_window.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Editor(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
 
    def open_file(self):        
        w = QWidget()
        filename = QFileDialog.getOpenFileName(w, 'Open File', '~')
        #TODO - dodelat nacteni obrazku Pillowem, vratit 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Editor()
    window.show()

    fileOpen = window.actionOpen
    fileOpen.triggered.connect(window.open_file)



    sys.exit(app.exec_())

