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

        self.button1 = QPushButton("My Custom Button")
        self.button1.setStyleSheet('''QPushButton{
                                   font-family: Arial;
                                   font: bold italic;
                                   font-size: 15pt;
                                   color: black;
                                   background: #2980b9;
                                   border-color: black;
                                   border-style: outset;
                                   border-radius: 8px;
                                   padding: 12px;
                                   }
                                   QPushButton:hover{
                                    background: #1f618d;
                                    opacity: 0.5;
                                    padding: 8px;
                                   } 
                                   ''')

        self.button2 = QPushButton("Tap to login")
        self.button2.setStyleSheet('''QPushButton{
                                   font: bold italic;
                                   font-size: 15pt;
                                   background: #177245;
                                   border-top-right-radius: 10px;
                                   border-bottom-left-radius: 10px;
                                   padding: 12px;
                                   } 
                                   ''')
        
        self.button3 = QPushButton("Welcome")
        self.button3.setStyleSheet('''QPushButton{
                                   font: bold italic;
                                   font-size: 15pt;
                                   color:blue;
                                   border: 3px dotted red;
                                   border-top-right-radius: 15px;
                                   border-top-left-radius: 15px;
                                   padding: 10px;
                                   } 
                                   ''')

        self.button4 = QPushButton("Click on the link")
        self.button4.setStyleSheet('''QPushButton{
                                   font: bold italic;
                                   font-size: 15px;
                                   color: blue;
                                   border-top-right-radius: 10px;
                                   border-bottom-left-radius: 10px;
                                   padding: 10px;
                                   text-decoration: underline;
                                   }
                                   QPushButton:hover{
                                    font-size: 18px;
                                   }
                                   QPushButton:pressed{
                                   color: darkblue;
                                   }
                                   ''')

        self.button5 = QPushButton("Commercial Trial")
        self.button5.setStyleSheet('''QPushButton{
                                   font-weight: bold;
                                   font-size: 13pt;
                                   color:blue;
                                   background: #FAF9F6;
                                   border: 2px solid blue;
                                   border-radius: 14px;
                                   padding: 10px;
                                   }
                                   QPushButton:Pressed{
                                   background: grey;
                                   }
                                   ''')
        


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = PracWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

