import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My Window Title")

        main_layout = QVBoxLayout()

        button1 = QPushButton("Button")
        button1.setToolTip("This is the tool tip text")
        button1.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")

        button2 = QPushButton("Button 2")
        button2.setToolTip("Button 2")
        button2.setStyleSheet("""QToolTip {
                        background-color: #179AE0;
                        border: 1px solid #232629;
                        color: #232629;
                        padding: 0;
                        opacity: 230;
                        }""")
                    

        button3 = QPushButton("Button 3")
        button3.setToolTip("This is the tool tip text")

        button4 = QPushButton("Button 4")
        button4.setToolTip("This is the tool tip text")

        button5 = QPushButton("Button")
        button5.setToolTip("This is the tool tip text")

        button6 = QPushButton("Button")
        button6.setToolTip("This is the tool tip text")

        button7 = QPushButton("Button")
        button7.setToolTip("This is the tool tip text")


         


        main_layout.addWidget(button1)
        main_layout.addWidget(button2)
        main_layout.addWidget(button3)
        main_layout.addWidget(button4)
        main_layout.addWidget(button5)
        main_layout.addWidget(button6)
        main_layout.addWidget(button7)
        self.setLayout(main_layout)
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())