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

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sample Dialog")
        self.setStyleSheet(css_data)

        # Set size of the dialog
        self.resize(400, 200)  # Width, Height

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create label
        self.label = QLabel("Dialog Sample")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Create buttons
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        # Create button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)

        # Set layout for dialog
        self.setLayout(self.layout)

        # Connect signals
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = CustomDialog()
    dialog.show()
    sys.exit(app.exec_())
