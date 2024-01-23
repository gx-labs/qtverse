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
        
        rb1layout = QHBoxLayout()
        self.radiobutton1 = QRadioButton('')
        self.radiobutton1.setFixedSize(30, 30)
        self.radiobutton1.setObjectName('1')
        self.radiobutton1.toggled.connect(self.radiobutton1_pressed)
        self.rb1label = QLabel('Option 1')
        rb1layout.addWidget(self.radiobutton1)
        rb1layout.addWidget(self.rb1label)
        
        rb2layout = QHBoxLayout()
        self.radiobutton2 = QRadioButton('')
        self.radiobutton2.setFixedSize(30, 30)
        self.radiobutton2.setObjectName('2')
        self.radiobutton2.toggled.connect(self.radiobutton2_pressed)
        self.rb2label = QLabel('Option 2')
        rb2layout.addWidget(self.radiobutton2)
        rb2layout.addWidget(self.rb2label)
        
        rb3layout = QHBoxLayout()
        self.radiobutton3 = QRadioButton('')
        self.radiobutton3.setFixedSize(30, 30)
        self.radiobutton3.setObjectName('3')
        self.radiobutton3.toggled.connect(self.radiobutton3_pressed)
        self.rb3label = QLabel('Option 3')
        rb3layout.addWidget(self.radiobutton3)
        rb3layout.addWidget(self.rb3label)
        
        layout.addLayout(rb1layout)
        layout.addLayout(rb2layout)
        layout.addLayout(rb3layout)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Toggled radiobutton1!')
        
        if self.radiobutton1.isChecked():
            self.radiobutton1.setText('√')
            self.radiobutton2.setText('')
            self.radiobutton3.setText('')
    
    def radiobutton2_pressed(self):
        print ('Toggled radiobutton2!')
        
        if self.radiobutton2.isChecked():
            self.radiobutton2.setText('√')
            self.radiobutton1.setText('')
            self.radiobutton3.setText('')

    def radiobutton3_pressed(self):
        print ('Toggled radiobutton3!')
        
        if self.radiobutton3.isChecked():
            self.radiobutton3.setText('√')
            self.radiobutton1.setText('')
            self.radiobutton2.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())