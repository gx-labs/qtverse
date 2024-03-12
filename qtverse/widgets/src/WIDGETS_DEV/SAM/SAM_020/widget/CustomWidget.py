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
        self.dialog.resize(450, 200)  # Width, Height
        self.dialog.setStyleSheet(css_data)

        # Create main layout for dialog
        self.layout = QVBoxLayout()

        # Create a frame for the first label
        self.label_frame1 = QFrame()
        self.label_frame1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.label_frame1_layout = QVBoxLayout(self.label_frame1)
        self.label_frame1_layout.setAlignment(Qt.AlignHCenter)  # Center align the label
        self.layout.addWidget(self.label_frame1)

        # Create label
        self.label1 = QLabel("<span style='font-size: 20px; color: black; font-weight:bold; '>Attention Required</span>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label_frame1_layout.addWidget(self.label1)

        # Create a frame for the second label
        self.label_frame2 = QFrame()
        self.label_frame2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.label_frame2_layout = QVBoxLayout(self.label_frame2)
        self.label_frame2_layout.setAlignment(Qt.AlignHCenter)  # Center align the label
        self.layout.addWidget(self.label_frame2)

        # Create label
        self.label2 = QLabel("<span style='font-size: 13px; color: black;'>By enabling cookies, you are giving us an opportunity to deliver the best results with<br>the advertisements on the website. Please accept the cookies and continue browsing<br>on the website.</span>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.label_frame2_layout.addWidget(self.label2)

    #     # Create a button box
    #     self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    #     self.layout.addWidget(self.button_box, alignment=Qt.AlignCenter)

    #     # Connect signals
    #     self.button_box.accepted.connect(self.accept)
    #     self.button_box.rejected.connect(self.reject)

    #     # Set layout for dialog
    #     self.dialog.setLayout(self.layout)

    # def accept(self):
    #     print("hello")

    # def reject(self):
    #     print("cancel")
        
        # Create a QHBoxLayout for buttons
        self.button_layout = QHBoxLayout()

        # Create buttons
        self.button_left = QPushButton("Reject Cookies")
        self.button_right = QPushButton("Accept Cookies")

        # Add buttons and spacers
        self.button_layout.addWidget(self.button_left)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.button_right)

        # Add button layout to main layout
        self.layout.addLayout(self.button_layout)

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
