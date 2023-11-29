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

        self.combo_box = QComboBox()
        self.combo_box.setFixedSize(150, 35)
        self.combo_box.addItem("Item 1")
        self.combo_box.addItem("Item 2")
        self.combo_box.addItem("Item 3")
        self.combo_box.addItem("Item 4")
        self.combo_box.addItem("Item 5")

        self.combo_box.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.combo_box, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())