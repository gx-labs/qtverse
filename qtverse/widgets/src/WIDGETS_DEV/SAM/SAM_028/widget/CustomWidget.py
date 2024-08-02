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

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 20px; color: black;'>Dialog Action</span>")
        self.label1.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label1, alignment=Qt.AlignLeft)

        self.layout.addSpacing(5)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 18px; color: #818181;'>Update all progress in MULTIASSETLOCCI</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.layout.addSpacing(10)

        # Create a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignRight)

        # Connect signals
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

        # Change button labels
        self.button_box.button(self.button_box.Ok).setText("OK")
        self.button_box.button(self.button_box.Cancel).setText("Cancel")

    def accept(self):
        print("hello")

    def reject(self):
        print("cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
