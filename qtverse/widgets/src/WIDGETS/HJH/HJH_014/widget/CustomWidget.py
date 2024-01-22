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
        layout.setSpacing(0)

        self.radiobutton1 = QRadioButton("Option 1")
        self.radiobutton1.setFixedSize(100, 40)
        self.radiobutton1.setObjectName("button1")
        self.radiobutton2 = QRadioButton("Option 2")
        self.radiobutton2.setFixedSize(100, 40)
        self.radiobutton2.setObjectName("button2")
        self.radiobutton3 = QRadioButton("Option 3")
        self.radiobutton3.setFixedSize(100, 40)
        self.radiobutton3.setObjectName("button3")
        self.radiobutton1.setStyleSheet(css_data)
        self.radiobutton2.setStyleSheet(css_data)
        self.radiobutton3.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)
        layout.addWidget(self.radiobutton3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())