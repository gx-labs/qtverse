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
        self.dialog.resize(500, 170)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 23px; color: #60A5FC;'>The More You Know</span>")
        self.label1.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label1, alignment=Qt.AlignLeft)

        self.layout.addSpacing(5)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 2px solid transparent; border-top: 2px solid #60A5FC;}")
        self.layout.addWidget(self.line)

        self.layout.addSpacing(5)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 13px; color: black;'>CodeHim is one of the BEST developer websites that provide web designers<br>and developers with simaple way to preview scripts.</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label2, alignment=Qt.AlignLeft)

        self.layout.addSpacing(10)

        # Create buttons
        self.button = QPushButton("Continue")

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
