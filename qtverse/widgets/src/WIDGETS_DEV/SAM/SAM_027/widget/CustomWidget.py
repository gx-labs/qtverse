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
        self.dialog.resize(400, 200)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 25px; color: white; font-weight:bold; '>Circular Modal Example</span>")
        self.label1.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label1, alignment=Qt.AlignLeft)

        self.layout.addSpacing(5)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 1px solid transparent; border-top: 1px solid #1473A2;}")
        self.layout.addWidget(self.line)

        self.layout.addSpacing(5)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 15px; color: white;'>CodeHim is one of the BEST developer websites that provide web designers<br>and developers with simaple way to preview scripts. Here you can download<br>ready made plugins, (HTML, CSS, JavaScript) code snippets.</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label2, alignment=Qt.AlignLeft)

        # Add spacer item to create space between lineedit and buttons
        self.layout.addSpacing(5)

        # Add separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line.setStyleSheet("QFrame{ border: 1px solid transparent; border-top: 1px solid #1473A2;}")
        self.layout.addWidget(self.line)

        self.layout.addSpacing(5)

        # Create a QHBoxLayout for buttons
        self.button_layout = QHBoxLayout()

        # Create buttons
        self.button_left = QPushButton("Static")
        self.button_middle = QPushButton("Element")
        self.button_right = QPushButton("Remote")

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
