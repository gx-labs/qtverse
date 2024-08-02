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
        self.dialog.resize(370, 210)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 32px; color: white; font-weight:bold; '>🖂</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("QLabel { background-color: #9867C5; border-radius: 25px; }")  # Set border and circular shape
        self.label1.setFixedSize(50, 50)  # Set fixed size to ensure it's a perfect circle
        self.layout.addWidget(self.label1, alignment=Qt.AlignCenter)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 25px; color: black;'>Subscribe for Updates</span>")
        self.label2.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        # Create label for the third item
        self.label3 = QLabel("<span style='font-size: 15px; color: grey;'>Enter your e-mail to get all the<br>latest updates about the products.</span>")
        self.label3.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label3, alignment=Qt.AlignCenter)

        # Add spacer item to create space between label and lineedit
        self.layout.addSpacing(10)

        # Create a line edit
        self.line_edit = QLineEdit()
        self.line_edit.setFixedHeight(35)  # Set the desired height
        self.line_edit.setPlaceholderText("abc@example.com")
        self.layout.addWidget(self.line_edit)

        # Add spacer item to create space between lineedit and buttons
        self.layout.addSpacing(5)

        # Create a single button
        self.button = QPushButton("Subscribe")
        self.layout.addWidget(self.button)

        # Connect signals
        self.button.clicked.connect(self.accept)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def accept(self):
        print("Subscribed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
