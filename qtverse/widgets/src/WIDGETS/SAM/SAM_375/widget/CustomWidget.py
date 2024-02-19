import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.messagebox = QMessageBox()
        self.messagebox.setWindowTitle("Styled MessageBox")
        self.messagebox.setText("Thanks for subscription to Geeks Portal.")
        self.messagebox.setStyleSheet(css_data)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor("rgb(115, 115, 115)")
        self.shadow.setBlurRadius(7)
        self.shadow.setOffset(2, 2)
        self.messagebox.setGraphicsEffect(self.shadow)

        self.messagebox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        self.messagebox.accepted.connect(self.ok_button_clicked)
        self.messagebox.rejected.connect(self.cancel_button_clicked)

        self.setLayout(layout)
        layout.addWidget(self.messagebox, alignment=Qt.AlignCenter)

    def ok_button_clicked(self):
        print("Ok button clicked")

    def cancel_button_clicked(self):
        print("Cancel button clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())
