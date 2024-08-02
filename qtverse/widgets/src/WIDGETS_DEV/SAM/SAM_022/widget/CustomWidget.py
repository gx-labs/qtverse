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
        self.dialog.resize(370, 170)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a label for the first item
        self.label1 = QLabel("<span style='font-size: 27px; color: black;'>Awesome!</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label1, alignment=Qt.AlignCenter)

        # Create label for the second item
        self.label2 = QLabel("<span style='font-size: 16px; color: grey;'>You just found my pastel gradient button.<br>Now let's see what else it does!</span>")
        self.label2.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        # Add spacer item to create space between lineedit and buttons
        self.layout.addSpacing(10)

        # Create a single button
        self.button = QPushButton("HOVER ME")
        self.layout.addWidget(self.button)

        # Connect signals
        self.button.clicked.connect(self.accept)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor("#DCDCE6")
        self.shadow.setBlurRadius(4)
        self.shadow.setOffset(2, 2)
        self.button.setGraphicsEffect(self.shadow)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

    def accept(self):
        print("Subscribed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomDialog()
    widget.dialog.show()
    sys.exit(app.exec_())
