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
        self.label1 = QLabel("<span style='font-size: 25px; color: #D7E3F5; font-weight:bold; '>Modal Title</span>")
        self.label1.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label1, alignment=Qt.AlignLeft)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 16px; color: #D7E3F5;'>CodeHim is one of the BEST developer websites that provide web designers<br>and developers with simaple way to preview scripts. Here you can download<br>ready made plugins, (HTML, CSS, JavaScript) code snippets.</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        # Add spacer item to create space between lineedit and buttons
        self.layout.addSpacing(10)

        # Create a single button
        self.button = QPushButton("Button →")
        self.layout.addWidget(self.button, alignment=Qt.AlignLeft)

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
