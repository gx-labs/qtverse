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
        self.dialog.resize(350, 210)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 40px; color: #1DA1F2;'>☁</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label1, alignment=Qt.AlignCenter)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 20px; color: black; font-weight:bold;'>Reply to join the conversation.</span>")
        self.label2.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        # Create label for the third item
        self.label3 = QLabel("<span style='font-size: 13px; color: grey;'>Once you join twitter, you can respond to Sambhav Pathak's<br>Tweet.</span>")
        self.label3.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label3, alignment=Qt.AlignCenter)

        # Add spacer item to create space between lineedit and buttons
        self.layout.addSpacing(10)

        # Create a QHBoxLayout for buttons
        self.button_layout = QVBoxLayout()

        # Create buttons
        self.button_left = QPushButton("Login")
        self.button_right = QPushButton("Set Dark Theme")

        # Add buttons and spacers
        self.button_layout.addWidget(self.button_left)
        self.button_layout.addStretch()

        # Add spacer item to create space between buttons
        self.button_layout.addSpacing(10)

        self.button_layout.addWidget(self.button_right)

        # Add button layout to main layout
        self.layout.addLayout(self.button_layout)

        # Add spacer item to create space between button and bottom of dialog
        self.layout.addSpacing(10)

        # Connect signals
        self.button_left.clicked.connect(self.reject)
        self.button_right.clicked.connect(self.accept)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def reject(self):
        print("rejct")

    def accept(self):
        print("ok")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
