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
        self.message_text = "<div style='text-align: center;'><span style='font-size: 22px; color: #4E97FC;'>🛈</span><span style='font-size: 18px; color: white; font-weight:bold;'> Sample Alert</span><br><span style='font-size: 16px; color: whitesmoke;'>Use the selector at the top-right corner to<br>change a template. Click Show the Alert.</span></div>"
        self.messagebox.setText(self.message_text)
        self.messagebox.setStyleSheet(css_data)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor("rgb(115, 115, 115)")
        self.shadow.setBlurRadius(7)
        self.shadow.setOffset(1, 2)
        self.messagebox.setGraphicsEffect(self.shadow)

        # Set the standard buttons before accessing them
        self.messagebox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Get the QPushButton objects
        ok_button = self.messagebox.button(QMessageBox.Ok)
        cancel_button = self.messagebox.button(QMessageBox.Cancel)

        # Set the text for the QPushButton objects
        ok_button.setText("Okay")
        cancel_button.setText("Cancel")

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
