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
        self.dialog.resize(290, 170)  # Width, Height

        self.dialog.setWindowTitle("Delete Confirmation")

        self.dialog.setStyleSheet(css_data)

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Add horizontal separator line after title bar
        # self.h_line1 = QFrame(self)
        # self.h_line1.setFrameShape(QFrame.HLine)
        # self.h_line1.setFrameShadow(QFrame.Sunken)
        # self.h_line1.setGeometry(0, 0, self.width(), 1)
        # self.h_line1.setStyleSheet("QFrame { border: 1px solid transparent; border-top: 1px solid rgb(219, 219, 219); }")  # Change the color here
        # self.layout.addWidget(self.h_line1)

        # Create label
        self.label = QLabel("<span style='font-size: 15px; color: rgb(52, 52, 52);'>This is very dangerous, you shouldn't do it! Are you<br>really really sure?</span>")
        self.layout.addWidget(self.label, alignment=Qt.AlignLeft)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 1px solid transparent; border-top: 1px solid rgb(219, 219, 219);}")
        self.layout.addWidget(self.line)

        # Create button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignRight)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

        # Change button labels
        self.button_box.button(self.button_box.Ok).setText("Yes, I am")
        self.button_box.button(self.button_box.Cancel).setText("No")

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
