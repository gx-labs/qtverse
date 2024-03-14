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
        self.dialog.resize(550, 200)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create a frame for the label
        self.label_frame = QFrame()
        self.label_frame.setStyleSheet("QFrame { background-color: #1274AC; }")

        # Create label
        self.label = QLabel("<span style='font-size: 23px; color: white; '>Software Update</span>")
        self.label.setAlignment(Qt.AlignLeft)
        self.label_frame_layout = QVBoxLayout()
        self.label_frame_layout.addWidget(self.label)
        self.label_frame.setLayout(self.label_frame_layout)
        self.label_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(self.label_frame)

        # Create a frame for the label2
        self.label_frame1 = QFrame()
        self.label_frame1.setStyleSheet("QFrame { background-color: transparent; }")

        # Create label
        self.label1 = QLabel("<span style='font-size: 16px; color: black;'>A new version of Kendo UI is available. Would you like to download<br>and install it now?</span>")
        self.label1.setAlignment(Qt.AlignLeft)
        self.label_frame_layout1 = QVBoxLayout()
        self.label_frame_layout1.addWidget(self.label1)
        self.label_frame1.setLayout(self.label_frame_layout1)
        self.label_frame1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(self.label_frame1)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 1px solid transparent; border-top: 1px solid rgb(228, 228, 228);}")
        self.layout.addWidget(self.line)

        # Create a QHBoxLayout for buttons
        self.button_layout = QHBoxLayout()

        # Create buttons
        self.button_left = QPushButton("Skip this version")
        self.button_middle = QPushButton("Remind me later")
        self.button_right = QPushButton("Install Update")

        # Add buttons and spacers
        self.button_layout.addWidget(self.button_left)
        self.button_layout.addWidget(self.button_middle)
        self.button_layout.addWidget(self.button_right)

        # Add button layout to main layout
        self.layout.addLayout(self.button_layout, alignment=Qt.AlignLeft)

        # Connect signals
        self.button_left.clicked.connect(self.static)
        self.button_middle.clicked.connect(self.element)
        self.button_right.clicked.connect(self.remote)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def static(self):
        print("left button")

    def element(self):
        print("middle button")

    def remote(self):
        print("right button")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
