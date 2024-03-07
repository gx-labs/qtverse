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
        self.dialog.resize(550, 180)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create a frame for the label
        self.label_frame = QFrame()
        self.label_frame.setStyleSheet("QFrame { background-color: #575757; }")

        # Create label
        self.label = QLabel("<span style='font-size: 18px; color: white; font-weight:bold; '>Custom Confirm Dialog</span>")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_frame_layout = QVBoxLayout()
        self.label_frame_layout.addWidget(self.label)
        self.label_frame.setLayout(self.label_frame_layout)
        self.label_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(self.label_frame)

        # Create label
        self.label1 = QLabel("<span style='font-size: 18px; color: black;'>Do you want to visit the channel?</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label1)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 1px solid transparent; border-top: 1px solid rgb(228, 228, 228);}")
        self.layout.addWidget(self.line)

        # Create button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignCenter)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

        # Change button labels
        self.button_box.button(self.button_box.Ok).setText("OK")
        self.button_box.button(self.button_box.Cancel).setText("Cancel")

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
