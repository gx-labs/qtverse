import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CancelWidget(QWidget):
    def __init__(self, parent=None):
        super(CancelWidget, self).__init__(parent)
        print("CancelWidget Improted")
        self.QVBoxLayout = QVBoxLayout()
        self.btn_1    = QPushButton("End Meeting")
        self.btn_2  = QPushButton("Cancel")
        self.QVBoxLayout.addWidget(self.btn_1)
        self.QVBoxLayout.addWidget(self.btn_2)
        self.setLayout(self.QVBoxLayout)

        self.setStyleSheet(
            """ QWidget {
                    background-color : rgb(50,50,50);
                    border-radius : 10px;
            }""")

        self.btn_1.setStyleSheet("""QPushButton {
                    min-width: 150 px;
                    min-height: 25 px;
                    color: white;
                    background-color: red;
                    border-radius: 10px; 
                    font-size: 50 px;
                    font-weight: bold;
                    font-family: Georgia;
	                }""")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Plastique")
    MainWindow = CancelWidget()
    MainWindow.show()
    sys.exit(app.exec_())















