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

        self.groupBox = QGroupBox()
        self.groupBox.setStyleSheet(css_data)

        self.button1 = QPushButton("Talk To Sales")
        self.button1.setFixedSize(180, 49)
        self.button1.setStyleSheet(css_data)

        self.button2 = QPushButton("Try For Free")
        self.button2.setFixedSize(180, 49)
        self.button2.setStyleSheet(css_data)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.groupBox.setLayout(self.layout)

        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.groupBox, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())