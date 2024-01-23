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
        colorlayout = QHBoxLayout()
        # colorlayout.setSpacing(10)
        
        self.colorlabel = QLabel('Colour Picker')
        
        self.radiobutton1 = QRadioButton()
        self.radiobutton1.setFixedSize(20, 20)
        self.radiobutton1.setObjectName('red')
        self.radiobutton1.clicked.connect(self.radiobutton1_pressed)
        self.radiobutton2 = QRadioButton()
        self.radiobutton2.setFixedSize(20, 20)
        self.radiobutton2.setObjectName('green')
        self.radiobutton2.clicked.connect(self.radiobutton2_pressed)
        self.radiobutton3 = QRadioButton()
        self.radiobutton3.setFixedSize(20, 20)
        self.radiobutton3.setObjectName('yellow')
        self.radiobutton3.clicked.connect(self.radiobutton3_pressed)
        self.radiobutton4 = QRadioButton()
        self.radiobutton4.setFixedSize(20, 20)
        self.radiobutton4.setObjectName('lime')
        self.radiobutton4.clicked.connect(self.radiobutton4_pressed)
        self.radiobutton5 = QRadioButton()
        self.radiobutton5.setFixedSize(20, 20)
        self.radiobutton5.setObjectName('orange')
        self.radiobutton5.clicked.connect(self.radiobutton5_pressed)
        self.radiobutton6 = QRadioButton()
        self.radiobutton6.setFixedSize(20, 20)
        self.radiobutton6.setObjectName('cyan')
        self.radiobutton6.clicked.connect(self.radiobutton6_pressed)
        self.radiobutton7 = QRadioButton()
        self.radiobutton7.setFixedSize(20, 20)
        self.radiobutton7.setObjectName('blue')
        self.radiobutton7.clicked.connect(self.radiobutton7_pressed)
        self.radiobutton8 = QRadioButton()
        self.radiobutton8.setFixedSize(20, 20)
        self.radiobutton8.setObjectName('violet')
        self.radiobutton8.clicked.connect(self.radiobutton8_pressed)
        self.radiobutton9 = QRadioButton()
        self.radiobutton9.setFixedSize(20, 20)
        self.radiobutton9.setObjectName('purple')
        self.radiobutton9.clicked.connect(self.radiobutton9_pressed)
        self.radiobutton10 = QRadioButton()
        self.radiobutton10.setFixedSize(20, 20)
        self.radiobutton10.setObjectName('pink')
        self.radiobutton10.clicked.connect(self.radiobutton10_pressed)
        
        colorlayout.addWidget(self.radiobutton1)
        colorlayout.addWidget(self.radiobutton2)
        colorlayout.addWidget(self.radiobutton3)
        colorlayout.addWidget(self.radiobutton4)
        colorlayout.addWidget(self.radiobutton5)
        colorlayout.addWidget(self.radiobutton6)
        colorlayout.addWidget(self.radiobutton7)
        colorlayout.addWidget(self.radiobutton8)
        colorlayout.addWidget(self.radiobutton9)
        colorlayout.addWidget(self.radiobutton10)
        
        layout.addWidget(self.colorlabel)
        layout.addLayout(colorlayout)
        
        self.setLayout(layout)
        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Pressed radiobutton1!')
    
    def radiobutton2_pressed(self):
        print ('Pressed radiobutton2!')

    def radiobutton3_pressed(self):
        print ('Pressed radiobutton3!')

    def radiobutton4_pressed(self):
        print ('Pressed radiobutton4!')
        
    def radiobutton5_pressed(self):
        print ('Pressed radiobutton5!')
        
    def radiobutton6_pressed(self):
        print ('Pressed radiobutton6!')
        
    def radiobutton7_pressed(self):
        print ('Pressed radiobutton7!')
        
    def radiobutton8_pressed(self):
        print ('Pressed radiobutton8!')
        
    def radiobutton9_pressed(self):
        print ('Pressed radiobutton9!')
        
    def radiobutton10_pressed(self):
        print ('Pressed radiobutton10!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())