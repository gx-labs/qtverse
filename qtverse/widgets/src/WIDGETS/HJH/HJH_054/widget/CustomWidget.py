import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        
        lightframe = QFrame(self)
        lightframe.setObjectName('lightframe')
        darkframe = QFrame(self)
        darkframe.setObjectName('darkframe')
        
        lightlayout = QVBoxLayout(lightframe)
        darklayout = QVBoxLayout(darkframe)

        self.radiobutton1 = QRadioButton('Light 1')
        self.radiobutton1.setObjectName('light')
        self.radiobutton1.setFixedSize(65, 25)
        self.radiobutton1.setChecked(True)
        self.radiobutton2 = QRadioButton('Light 2')
        self.radiobutton2.setObjectName('light')
        self.radiobutton2.setFixedSize(65, 25)
        
        self.radiobutton3 = QRadioButton('Dark 1')
        self.radiobutton3.setObjectName('dark')
        self.radiobutton3.setFixedSize(65, 25)
        self.radiobutton3.setChecked(True)
        self.radiobutton4 = QRadioButton('Dark 2')
        self.radiobutton4.setObjectName('dark')
        self.radiobutton4.setFixedSize(65, 25)

        lightlayout.addWidget(self.radiobutton1)
        lightlayout.addWidget(self.radiobutton2)
        darklayout.addWidget(self.radiobutton3)
        darklayout.addWidget(self.radiobutton4)
        
        layout.addWidget(lightframe)
        layout.addWidget(darkframe)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())