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

        self.button1 = QRadioButton('Light 1')
        self.button1.setObjectName('light')
        self.button1.setFixedSize(65, 25)
        self.button1.setChecked(True)
        self.button2 = QRadioButton('Light 2')
        self.button2.setObjectName('light')
        self.button2.setFixedSize(65, 25)
        
        self.button3 = QRadioButton('Dark 1')
        self.button3.setObjectName('dark')
        self.button3.setFixedSize(65, 25)
        self.button3.setChecked(True)
        self.button4 = QRadioButton('Dark 2')
        self.button4.setObjectName('dark')
        self.button4.setFixedSize(65, 25)

        lightlayout.addWidget(self.button1)
        lightlayout.addWidget(self.button2)
        darklayout.addWidget(self.button3)
        darklayout.addWidget(self.button4)
        
        layout.addWidget(lightframe)
        layout.addWidget(darkframe)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())