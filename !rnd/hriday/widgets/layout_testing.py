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
        
        self.layout = QVBoxLayout()

        self.pushbutton = QPushButton("Press")
        self.pushbutton.clicked.connect(self.remove_widget)
        
        self.label1 = QLabel("Label 1")
        self.label2 = QLabel("Label 2")

        self.setLayout(self.layout)
        self.layout.addWidget(self.pushbutton)
        self.layout.addWidget(self.label1)
        
        print(self.layout.isEmpty())
        
    def remove_widget(self):
        if self.layout.isEmpty():
            self.layout.addWidget(self.label2)
        else:
            preview = self.layout.takeAt(1)
            preview.widget().deleteLater()
            self.layout.addWidget(self.label2)

            
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())