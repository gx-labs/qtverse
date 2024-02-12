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

        self.inputdialog = QInputDialog()
        self.inputdialog.setWindowTitle("Sample dialog")
        self.inputdialog.setLabelText("Enter text")
        self.inputdialog.setOkButtonText("✔ Ok")
        self.inputdialog.setCancelButtonText("🚫 Cancel")
        self.inputdialog.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.inputdialog, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())