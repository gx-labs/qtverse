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
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor(100, 149, 237))
        self.setGraphicsEffect(self.shadow)
        
        layout = QVBoxLayout()

        self.radiobutton1 = QRadioButton("INSTAGRAM")
        self.radiobutton1.setFixedSize(250, 40)
        self.radiobutton1.clicked.connect(self.radiobutton1_pressed)

        self.setLayout(layout)
        layout.addWidget(self.radiobutton1, alignment=Qt.AlignCenter)

        self.setStyleSheet(css_data)
        
    def radiobutton1_pressed(self):
        print ('Pressed radiobutton1!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())