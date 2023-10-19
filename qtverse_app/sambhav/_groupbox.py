import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class GroupbxWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Groupbox Styles")
        self.setFixedSize(QSize(800, 800))

        self.grpbx1 = QGroupBox("Group 1")
        self.grpbx1.setFixedSize(600,200)
        self.grpbx1.setStyleSheet('''
                                     QGroupBox{
                                        background-color: pink;
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                        font-size: 15px;
                                        font-weight: bold;
                                     }                                                   
        ''')

        self.grpbx2 = QGroupBox("Group 2")
        self.grpbx2.setFixedSize(600,200)
        self.grpbx2.setStyleSheet('''
                                     QGroupBox{
                                        background-color: #E3DAC9;
                                        border: 2px solid red;
                                        border-radius: 5px;
                                        font-size: 14px;
                                        font-weight: bold;
                                        color: purple;
                                     }
                                     QGroupBox:title{
                                        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 orange, stop: 1 yellow);
                                        padding: 5px 600px 5px 600px; 
                                        border: 2px solid grey;
                                        subcontrol-position: top center;
                                     }                                            
        ''')

        self.grpbx3 = QGroupBox("Group 3")
        self.grpbx3.setFixedSize(600,200)
        self.grpbx3.setStyleSheet('''
                                     QGroupBox {
                                            border: 1px solid blue;
                                            margin-top: 1em;
                                            font-size: 5em;
                                            border-top-right-radius: 6px;
                                            border-bottom-left-radius: 6px;
                                            border-bottom-right-radius: 6px;
                                        }
                                        
                                        QGroupBox::title {
                                            color: #fff;
                                            background-color: blue;
                                            border: 2px dotted yellow;
                                            subcontrol-origin: margin;
                                            padding: 0.5em 0.7em;
                                            border-top-left-radius: 6px;
                                            border-top-right-radius: 6px;
                                            border-bottom-right-radius: 6px;
                                            margin: 4px;
                                        }                                            
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.grpbx1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.grpbx2, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.grpbx3, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = GroupbxWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()