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

        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Address")
        self.lineedit.setStyleSheet(css_data)

        self.shadow = QGraphicsDropShadowEffect()

        self.shadow.setColor("#D9D9D9")
        self.shadow.setBlurRadius(7)
        self.shadow.setOffset(0,-2)
        self.lineedit.setGraphicsEffect(self.shadow)

        self.setLayout(layout)
        layout.addWidget(self.lineedit, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())