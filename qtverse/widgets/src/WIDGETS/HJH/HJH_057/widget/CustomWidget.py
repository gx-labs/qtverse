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

        layout = QGridLayout()
        layout.setSpacing(0)
        
        self.radiobutton1 = QRadioButton('Yes')
        self.radiobutton1.setFixedSize(50, 40)
        self.radiobutton1.setObjectName('yes')
        self.radiobutton1.toggled.connect(self.radiobutton1_pressed)
        self.radiobutton2 = QRadioButton('No')
        self.radiobutton2.setFixedSize(50, 40)
        self.radiobutton2.setObjectName('no')
        self.radiobutton2.setChecked(True)
        self.radiobutton2.toggled.connect(self.radiobutton2_pressed)
        
        self.symbol = QLabel('X')
        self.symbol.setFixedSize (40, 40)
        
        layout.addWidget(self.radiobutton1, 0, 0)
        layout.addWidget(self.radiobutton2, 0, 2)
        layout.addWidget(self.symbol, 0, 1)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Toggled radiobutton1!')
        
        if self.radiobutton1.isChecked():
            self.symbol.setText('√')
            self.symbol.setStyleSheet('background-color: #0BDEB9;')
    
    def radiobutton2_pressed(self):
        print ('Toggled radiobutton2!')
        
        if self.radiobutton2.isChecked():
            self.symbol.setText('X')
            self.symbol.setStyleSheet('background-color: #FF6044;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())