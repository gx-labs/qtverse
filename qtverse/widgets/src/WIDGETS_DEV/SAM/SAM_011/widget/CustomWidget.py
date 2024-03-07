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
        self.dialog.resize(500, 180)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create horizontal layout for frames
        self.horizontal_layout = QHBoxLayout()

        # Create a frame for the first label
        self.label_frame1 = QFrame()
        self.label_frame1.setStyleSheet("QFrame { background-color: #F62447; }")
        self.label_frame1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.label_frame1_layout = QVBoxLayout()
        self.label_frame1.setLayout(self.label_frame1_layout)
        self.horizontal_layout.addWidget(self.label_frame1)

        # Create label
        self.label1 = QLabel("<span style='font-size: 30px; color: white; font-weight:bold; '>!</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label_frame1_layout.addWidget(self.label1)

        # Create a frame for the second label
        self.label_frame2 = QFrame()
        self.label_frame2_layout = QVBoxLayout()
        self.label_frame2.setLayout(self.label_frame2_layout)
        self.horizontal_layout.addWidget(self.label_frame2)

        # Create label
        self.label2 = QLabel("<span style='font-size: 22px; color: black;'>Delete Image?</span><br><br><span style='font-size: 15px; color: grey;'>This image is also used by 10 other objects. All references<br>will be lost if you delete this image.</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.label_frame2_layout.addWidget(self.label2)

        self.layout.addLayout(self.horizontal_layout)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 1px solid transparent; border-top: 1px solid lightgrey;}")
        self.layout.addWidget(self.line)

        # Create a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignRight)

        # Connect signals
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

        # Change button labels
        self.button_box.button(self.button_box.Ok).setText("Keep image")
        self.button_box.button(self.button_box.Cancel).setText("Delete image")

    def accept(self):
        print("hello")

    def reject(self):
        print("cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())