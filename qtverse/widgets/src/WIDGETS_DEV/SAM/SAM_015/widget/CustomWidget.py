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
        self.dialog.resize(400, 210)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 35px; color: #F13C21; font-weight:bold; '>!</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("QLabel { background-color: transparent; border: 2px solid #F13C21; border-radius: 25px; }")  # Set border and circular shape
        self.label1.setFixedSize(50, 50)  # Set fixed size to ensure it's a perfect circle
        self.layout.addWidget(self.label1, alignment=Qt.AlignCenter)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 23px; color: black; font-weight:bold;'>Confirm</span>")
        self.label2.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        # Create label for the third item
        self.label3 = QLabel("<span style='font-size: 16px; color: black;'>Are you sure you want to permanently<br>delete this photo?</span>")
        self.label3.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label3, alignment=Qt.AlignCenter)

        # Create a button box
        self.button_box = QDialogButtonBox()
        self.button_ok = QPushButton("Yes, Delete!")
        self.button_ok.setStyleSheet("background-color: #2980B9;")
        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.setStyleSheet("background-color: #F33C25;")
        self.button_box.addButton(self.button_ok, QDialogButtonBox.AcceptRole)
        self.button_box.addButton(self.button_cancel, QDialogButtonBox.RejectRole)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignCenter)

        # Connect signals
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def accept(self):
        print("hello")

    def reject(self):
        print("cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
