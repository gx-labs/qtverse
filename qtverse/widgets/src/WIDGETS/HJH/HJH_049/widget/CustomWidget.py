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

        layout = QVBoxLayout()

        self.radiobutton1 = QRadioButton('HTML')
        self.radiobutton1.setChecked(True)
        self.radiobutton1.setFixedSize(66, 35)
        self.radiobutton2 = QRadioButton('CSS')
        self.radiobutton2.setFixedSize(59, 35)
        self.radiobutton3 = QRadioButton('Javascript')
        self.radiobutton3.setFixedSize(90, 35)

        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)
        layout.addWidget(self.radiobutton3)
        
        self.setLayout(layout)
        
        self.setStyleSheet(css_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())