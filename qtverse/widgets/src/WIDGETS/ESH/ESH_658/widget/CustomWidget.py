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

        main_layout = QVBoxLayout()

        horizontal_layout = QHBoxLayout()
        spacerItem1 = QSpacerItem(5, 20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem1)

        self.label = QLabel()
        self.label.setStyleSheet(css_data)
        horizontal_layout.addWidget(self.label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedSize(340, 35)
        self.progress_bar.setStyleSheet(css_data)
        horizontal_layout.addWidget(self.progress_bar)

        spacerItem2 = QSpacerItem(5, 20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem2)

        main_layout.addLayout(horizontal_layout)
        self.setLayout(main_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

    def update_progress(self):
        current_value = self.progress_bar.value()
        new_value = current_value + 1

        if new_value > self.progress_bar.maximum():
            new_value = 0

        self.progress_bar.setValue(new_value)
        self.label.setText(f"{new_value}%")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())




