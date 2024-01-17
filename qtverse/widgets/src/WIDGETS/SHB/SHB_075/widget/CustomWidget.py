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
        self.combo_box.setFixedSize(200, 40)
        self.combo_box.addItem("Profile")
        self.combo_box.addItem("Word")
        self.combo_box.addItem("HashTag")

        self.combo_box.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.combo_box, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())