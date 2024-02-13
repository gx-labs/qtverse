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

        self.widget = QWidget()
        self.widget.setFixedSize(170, 75)
        self.widget.setStyleSheet(css_data)

        widget_layout = QVBoxLayout(self.widget)  
        widget_layout.setAlignment(Qt.AlignCenter)  

        self.button = QPushButton("Read More")  
        self.button.setFixedSize(150, 55)
        self.button.setStyleSheet(css_data)

        layout.addWidget(self.widget, alignment=Qt.AlignCenter)  
        widget_layout.addWidget(self.button)  

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())




