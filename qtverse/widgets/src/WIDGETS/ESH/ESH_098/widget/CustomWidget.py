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

        self.button = QPushButton("NEW")
        self.button.setFixedSize(175, 65)
        self.button.setStyleSheet(css_data)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(40)
        self.shadow.setColor("#174caf")
        self.shadow.setOffset(10,10)
        self.button.setGraphicsEffect(self.shadow)


        self.setLayout(layout)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())

    app.exec_()

