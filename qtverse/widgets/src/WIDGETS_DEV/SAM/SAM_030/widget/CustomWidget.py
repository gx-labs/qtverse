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
        self.dialog.resize(500, 130)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 21px; color: #FD7B16; font-weight: bold; '>KEEP UP TO DATE ON WEB DEV</span>")
        self.label1.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label1, alignment=Qt.AlignLeft)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 12px; color: white;'>with our hand-crafted newsletter</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label2, alignment=Qt.AlignLeft)

        # self.layout.addSpacing(10)

        # Create a QHBoxLayout for buttons
        self.hori_layout = QHBoxLayout()

        # Create lineedit
        self.lineedit = QLineEdit()
        self.lineedit.setFixedHeight(35)  # Set the desired height
        self.lineedit.setPlaceholderText("abc@example.com")

        # Create buttons
        self.button = QPushButton("SUBSCRIBE")

        # Add buttons and spacers
        self.hori_layout.addWidget(self.lineedit)
        self.hori_layout.addWidget(self.button)

        # Add button layout to main layout
        self.layout.addLayout(self.hori_layout, alignment=Qt.AlignCenter)

        # Connect signals
        self.button.clicked.connect(self.static)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor("black")
        self.shadow.setBlurRadius(4)
        self.shadow.setOffset(2, 2)
        self.button.setGraphicsEffect(self.shadow)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def static(self):
        print("left button")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
