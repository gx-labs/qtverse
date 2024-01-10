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

        self.button1 = QRadioButton('All')
        self.button1.setChecked(True)
        self.button1.setFixedSize(35, 25)
        self.button2 = QRadioButton('Upcoming')
        self.button2.setFixedSize(65, 25)
        self.button3 = QRadioButton('Ongoing')
        self.button3.setFixedSize(65, 25)
        self.button4 = QRadioButton('Complete')
        self.button4.setFixedSize(65, 25)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        frame.setLayout(layout)

        central_layout = QVBoxLayout(self)
        central_layout.addWidget(frame)
        
        self.setStyleSheet(css_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())