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

        self.button1 = QRadioButton('Option 1')
        self.button1.setChecked(True)
        self.button1.setFixedSize(95, 35)
        self.button2 = QRadioButton('Option 2')
        self.button2.setFixedSize(95, 35)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())