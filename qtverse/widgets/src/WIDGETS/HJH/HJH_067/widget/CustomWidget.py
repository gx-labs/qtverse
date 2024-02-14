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

        frame = QFrame(self)

        layout = QHBoxLayout(frame)

        self.radiobutton1 = QRadioButton('HTML')
        self.radiobutton1.setChecked(True)
        self.radiobutton1.setFixedSize(65, 35)
        self.radiobutton1.clicked.connect(self.radiobutton1_pressed)
        self.radiobutton2 = QRadioButton('React')
        self.radiobutton2.setFixedSize(65, 35)
        self.radiobutton2.clicked.connect(self.radiobutton2_pressed)
        self.radiobutton3 = QRadioButton('Vue')
        self.radiobutton3.setFixedSize(65, 35)
        self.radiobutton3.clicked.connect(self.radiobutton3_pressed)

        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)
        layout.addWidget(self.radiobutton3)

        frame.setLayout(layout)

        central_layout = QVBoxLayout(self)
        central_layout.addWidget(frame)
        
        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Pressed radiobutton1!')
        
    def radiobutton2_pressed(self):
        print ('Pressed radiobutton2!')
        
    def radiobutton3_pressed(self):
        print ('Pressed radiobutton3!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())