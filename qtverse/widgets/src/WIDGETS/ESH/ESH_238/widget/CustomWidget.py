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

        self.button = QPushButton("Confirm 🗸")  
        self.button.setFixedSize(170,60)
        self.button.setStyleSheet(css_data)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor("#585a5c")
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(4,4)
        self.button.setGraphicsEffect(self.shadow)

        layout.addWidget(self.button)  
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())




