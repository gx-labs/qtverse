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
        
        self.radiobutton1 = QRadioButton()
        self.radiobutton1.setFixedSize(36, 36)
        self.radiobutton1.setObjectName('rdbtn1')
        self.radiobutton1.toggled.connect(self.radiobutton1_pressed)
        self.radiobutton2 = QRadioButton()
        self.radiobutton2.setFixedSize(36, 36)
        self.radiobutton2.setObjectName('rdbtn2')
        self.radiobutton2.toggled.connect(self.radiobutton2_pressed)
        self.radiobutton3 = QRadioButton()
        self.radiobutton3.setFixedSize(36, 36)
        self.radiobutton3.setObjectName('rdbtn3')
        self.radiobutton3.toggled.connect(self.radiobutton3_pressed)
        self.radiobutton4 = QRadioButton()
        self.radiobutton4.setFixedSize(36, 36)
        self.radiobutton4.setObjectName('rdbtn4')
        self.radiobutton4.toggled.connect(self.radiobutton4_pressed)
        
        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)
        layout.addWidget(self.radiobutton3)
        layout.addWidget(self.radiobutton4)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Toggled radiobutton1!')
        if self.radiobutton1.isChecked():
            self.radiobutton1.setText('✔')
        else:
            self.radiobutton1.setText('')
    
    def radiobutton2_pressed(self):
        print ('Toggled radiobutton2!')
        if self.radiobutton2.isChecked():
            self.radiobutton2.setText('✔')
        else:
            self.radiobutton2.setText('')
        
    def radiobutton3_pressed(self):
        print ('Toggled radiobutton3!')
        if self.radiobutton3.isChecked():
            self.radiobutton3.setText('✔')
        else:
            self.radiobutton3.setText('')
    
    def radiobutton4_pressed(self):
        print ('Toggled radiobutton4!')
        if self.radiobutton4.isChecked():
            self.radiobutton4.setText('✔')
        else:
            self.radiobutton4.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())