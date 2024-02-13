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

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(20)
        self.progress_bar.setFixedSize(290, 5)
        self.progress_bar.setStyleSheet(css_data)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

        layout.addWidget(self.progress_bar)
        self.setLayout(layout)
    
    def update_progress(self):
        current_value = self.progress_bar.value()
        new_value = current_value + 1

        if new_value > self.progress_bar.maximum():
            new_value = 0

        self.progress_bar.setValue(new_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())




