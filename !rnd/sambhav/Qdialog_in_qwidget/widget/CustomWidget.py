import os
import sys
from PySide2.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QDialogButtonBox, QWidget
from PySide2.QtCore import Qt

# Read CSS file for styling
css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create QDialog as a member variable of CustomWidget
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Sample Dialog")
        self.dialog.setStyleSheet(css_data)

        # Set size of the dialog
        self.dialog.resize(400, 200)  # Width, Height

        # Create layout for dialog
        layout = QVBoxLayout(self.dialog)

        # Create label
        label = QLabel("Dialog Sample", self.dialog)
        layout.addWidget(label, alignment=Qt.AlignCenter)

        # Create buttons
        button1 = QPushButton("Button 1", self.dialog)
        button2 = QPushButton("Button 2", self.dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Create button box
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self.dialog)
        layout.addWidget(button_box)

        # Connect signals
        button_box.accepted.connect(self.dialog.accept)
        button_box.rejected.connect(self.dialog.reject)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.dialog.show()
    sys.exit(app.exec_())
