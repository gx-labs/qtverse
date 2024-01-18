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

        self.button1 = QRadioButton("Low")
        self.button1.setFixedSize(100, 40)
        self.button1.setObjectName("low")
        self.button2 = QRadioButton("Medium")
        self.button2.setFixedSize(100, 40)
        self.button2.setObjectName("medium")
        self.button3 = QRadioButton("High")
        self.button3.setFixedSize(100, 40)
        self.button3.setObjectName("high")
        self.button1.setStyleSheet(css_data)
        self.button2.setStyleSheet(css_data)
        self.button3.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())