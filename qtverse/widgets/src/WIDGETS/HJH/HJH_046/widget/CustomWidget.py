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
        # layout.setSpacing(0)

        self.radiobutton1 = QRadioButton("Yes")
        self.radiobutton1.setFixedSize(200, 30)
        self.radiobutton1.setLayoutDirection(Qt.RightToLeft)
        self.radiobutton1.setChecked(True)
        self.radiobutton2 = QRadioButton("No")
        self.radiobutton2.setFixedSize(200, 30)
        self.radiobutton2.setLayoutDirection(Qt.RightToLeft)
        self.radiobutton1.setStyleSheet(css_data)
        self.radiobutton2.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())