import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class PracWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Button Styles")
        self.setFixedSize(QSize(500, 500))

        self.button1 = QPushButton("OK")
        self.button2 = QPushButton("Click")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = PracWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

