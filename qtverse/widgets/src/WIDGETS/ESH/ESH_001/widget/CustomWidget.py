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

        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("Option1")
        self.comboBox1.addItem("Option2")
        self.comboBox1.addItem("Option3")
        self.comboBox1.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.comboBox1, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())