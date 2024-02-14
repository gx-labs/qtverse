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
        layout.setAlignment(Qt.AlignCenter)

        self.button_group = QButtonGroup()

        self.option1 = QRadioButton("Radio 1")
        self.option2 = QRadioButton("Radio 2")
        self.option3 = QRadioButton("Radio 3")

        self.option1.setStyleSheet(css_data)
        self.option2.setStyleSheet(css_data)
        self.option3.setStyleSheet(css_data)

        layout.addWidget(self.option1)
        layout.addWidget(self.option2)
        layout.addWidget(self.option3)

        self.button_group.addButton(self.option1)
        self.button_group.addButton(self.option2)
        self.button_group.addButton(self.option3)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())




    