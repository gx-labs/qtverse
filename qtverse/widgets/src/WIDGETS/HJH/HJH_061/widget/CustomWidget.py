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
        layout.setSpacing(0)
        
        self.radiobutton1 = QRadioButton('  👤  Public Profile')
        self.radiobutton1.setFixedSize(130, 30)
        self.radiobutton1.clicked.connect(self.radiobutton1_pressed)
        self.radiobutton2 = QRadioButton('  ⚙   Account')
        self.radiobutton2.setFixedSize(130, 30)
        self.radiobutton2.clicked.connect(self.radiobutton2_pressed)
        self.radiobutton3 = QRadioButton('  ✏   Appearance')
        self.radiobutton3.setFixedSize(130, 30)
        self.radiobutton3.clicked.connect(self.radiobutton3_pressed)
        self.radiobutton4 = QRadioButton('  🫂  Accessibility')
        self.radiobutton4.setFixedSize(130, 30)
        self.radiobutton4.clicked.connect(self.radiobutton4_pressed)
        self.radiobutton5 = QRadioButton('  🔔  Notification')
        self.radiobutton5.setFixedSize(130, 30)
        self.radiobutton5.clicked.connect(self.radiobutton5_pressed)
        
        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)
        layout.addWidget(self.radiobutton3)
        layout.addWidget(self.radiobutton4)
        layout.addWidget(self.radiobutton5)
        
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
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())