import os
import sys
from PySide2.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel
from PySide2.QtCore import Qt

css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")

class CustomWidget:
    def __init__(self):
        super().__init__()

        self.dialog = QDialog()
        self.dialog.setWindowTitle("Sample Dialog")
        self.dialog.setStyleSheet(css_data)

        # Set size of the dialog
        self.dialog.resize(400, 200)  # Width, Height

        # Create layout for dialog
        self.layout = QVBoxLayout()

        # Create label
        self.label = QLabel("Dialog Sample")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Create buttons
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        # Set layout for dialog
        self.dialog.setLayout(self.layout)

        # Show the dialog
        self.dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    sys.exit(app.exec_())
