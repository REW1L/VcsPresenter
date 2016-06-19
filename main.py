# -*- coding: utf-8 -*-

import sys
import os
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *

QtGui.QApplication.setLibraryPaths([os.path.join(sys._MEIPASS, 'qt4_plugins'), sys._MEIPASS])
from views.mainview import MainView

app = QtGui.QApplication(sys.argv)

window = MainView()
window.show()
# Enter Qt application main loop

sys.exit(app.exec_())