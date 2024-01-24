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

        self.combo_box = QComboBox()
        self.combo_box.setFixedSize(280, 50)
        self.combo_box.addItem("Red Dead Redemption 2")
        self.combo_box.addItem("GTA 5 Online ")
        self.combo_box.addItem("CyberPunk 2077")
        self.combo_box.addItem("Justice League")
        indexs = [1,4,3,2]
 
        # adding separator at maximum index
        self.combo_box.insertSeparator(max(indexs))
 
        # adding separator at middle index
        index = 0
        for i in indexs:
            if i > min(indexs) and i < max(indexs):
                index = i
                self.combo_box.insertSeparator(index)
 
        # adding separator at minimum index
        self.combo_box.insertSeparator(min(indexs))

        # self.combo_box.setEditable(True)
        self.combo_box.setStyleSheet(css_data)
        self.setLayout(layout)
        layout.addWidget(self.combo_box, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())