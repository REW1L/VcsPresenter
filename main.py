# -*- coding: utf-8 -*-

import sys
import os
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *

# QtWidgets.QApplication.setLibraryPaths([os.path.join(sys._MEIPASS, 'qt4_plugins'), sys._MEIPASS])
from views.mainview import MainView

app = QtWidgets.QApplication(sys.argv)

window = MainView()
window.show()
# Enter Qt application main loop

sys.exit(app.exec_())
