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

        self.prgsbar = QProgressBar()
        self.prgsbar.setValue(0)
        self.prgsbar.setFixedSize(400, 25)
        self.prgsbar.setStyleSheet(css_data)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

        layout.addWidget(self.prgsbar, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def update_progress(self):
        current_value = self.prgsbar.value()
        new_value = current_value + 1

        # If the progress bar reaches maximum value, reset to minimum
        if new_value > self.prgsbar.maximum():
            new_value = 0

        self.prgsbar.setValue(new_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())