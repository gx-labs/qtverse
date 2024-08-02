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
        self.label_frame.setStyleSheet("QFrame { background-color: #FF714D; }")

        # Create label
        self.label = QLabel("<span style='font-size: 23px; color: whitesmoke; '>Software Update</span>")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_frame_layout = QVBoxLayout()
        self.label_frame_layout.addWidget(self.label)
        self.label_frame.setLayout(self.label_frame_layout)
        self.label_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(self.label_frame)

        # Create a frame for the label2
        self.label_frame1 = QFrame()
        self.label_frame1.setStyleSheet("QFrame { background-color: transparent; }")

        # Create label
        self.label1 = QLabel("<span style='font-size: 15px; color: grey;'>A new version of Kendo UI is available. Would you like to download<br>and install it now?</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label_frame_layout1 = QVBoxLayout()
        self.label_frame_layout1.addWidget(self.label1)
        self.label_frame1.setLayout(self.label_frame_layout1)
        self.label_frame1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(self.label_frame1)

        self.layout.addSpacing(10)

        # Create buttons
        self.button = QPushButton("Learn More")

        # Add button layout to main layout
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)

        # Connect signals
        self.button.clicked.connect(self.static)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def static(self):
        print("left button")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
