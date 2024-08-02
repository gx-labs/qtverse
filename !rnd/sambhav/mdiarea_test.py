import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

widget = QWidget()
mdiarea = QMdiArea() 
layout = QVBoxLayout(widget)
layout.addWidget(mdiarea)
d = QInputDialog()
d.setLabelText("test2")
d.setInputMode(QInputDialog.TextInput)
w = mdiarea.addSubWindow(d)
w.show()
widget.show()