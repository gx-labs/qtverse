from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class ClickableLabel(QLabel):
    clicked = Signal()
    

    def __init__(self, text='', parent=None):
        super(ClickableLabel, self).__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super(ClickableLabel, self).mousePressEvent(event)
        print("clicked")