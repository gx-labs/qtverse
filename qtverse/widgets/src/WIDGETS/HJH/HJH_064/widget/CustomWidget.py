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

        self.radiobutton1 = QRadioButton('')
        self.radiobutton1.setChecked(True)
        self.radiobutton1.setFixedSize(28, 28)
        self.radiobutton1.toggled.connect(self.radiobutton1_toggled)
        self.radiobutton1.clicked.connect(self.radiobutton1_pressed)
        self.radiobutton2 = QRadioButton('')
        self.radiobutton2.setFixedSize(28, 28)
        self.radiobutton2.toggled.connect(self.radiobutton2_toggled)
        self.radiobutton2.clicked.connect(self.radiobutton2_pressed)
        self.radiobutton3 = QRadioButton('')
        self.radiobutton3.setFixedSize(28, 28)
        self.radiobutton3.toggled.connect(self.radiobutton3_toggled)
        self.radiobutton3.clicked.connect(self.radiobutton3_pressed)

        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)
        layout.addWidget(self.radiobutton3)
        
        self.setLayout(layout)
        
        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Pressed radiobutton1!')
        
    def radiobutton2_pressed(self):
        print ('Pressed radiobutton2!')
        
    def radiobutton3_pressed(self):
        print ('Pressed radiobutton3!')
        
    def radiobutton1_toggled(self):
        if self.radiobutton1.isChecked():
            self.radiobutton1.setText('✘')
            self.radiobutton2.setText('')
            self.radiobutton3.setText('')
        
    def radiobutton2_toggled(self):
        if self.radiobutton2.isChecked():
            self.radiobutton1.setText('')
            self.radiobutton2.setText('✘')
            self.radiobutton3.setText('')
        
    def radiobutton3_toggled(self):
        if self.radiobutton3.isChecked():
            self.radiobutton1.setText('')
            self.radiobutton2.setText('')
            self.radiobutton3.setText('✘')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())