import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# Read CSS file for styling
css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")

class CustomDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.dialog = QDialog()
        self.dialog.setWindowTitle("Sample Dialog")
        self.dialog.resize(400, 150)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create label
        self.label = QLabel("<div style='text-align: center;'><span style='font-size: 20px; color: black; font-weight:bold;'>Delete</span><br><span style='font-size: 16px; color: grey;'>Are you sure you want to delete this post?</span></div>")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Create button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignCenter)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

        # Connect signals
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def accept(self):
        print("hello")

    def reject(self):
        print("cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
