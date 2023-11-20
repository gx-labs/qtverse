import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class SpinWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Spinbox Styles")
        self.setFixedSize(QSize(500, 500))

        self.label_combo = QLabel("Spinbox Widgets")
        font = self.label_combo.font()
        font.setPointSize(14)
        self.label_combo.setFont(font)

        self.spin1 = QSpinBox()
        self.spin1.setStyleSheet('''
                                     QSpinBox{
                                        width: 8em;
                                        background-color: pink;
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                        padding: 10px;
                                        color: red;
                                        font-weight: bold;
                                        selection-background-color: orange;
                                        selection-color: green;
                                     }
                                     QSpinBox:hover{
                                        border: 2px solid blue;
                                        background-color: #FFFFED;
                                        color: blue;
                                     }                            
        ''')

        self.spin2 = QSpinBox()
        self.spin2.setStyleSheet('''
                                     QSpinBox{
                                        width: 8em;
                                        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 orange, stop: 1 yellow);
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                        padding: 10px;
                                        color: grey;
                                        font-weight: bold;
                                        selection-background-color: red;
                                        selection-color: green;
                                     }
                                     QSpinBox:up-button{
                                        subcontrol-origin: border;
                                        width: 20px;
                                        border: 2px solid #A9A9A9;
                                     }
                                     QSpinBox:up-button:hover{
                                        border: 2px solid blue;
                                        background: #3D2B1F;
                                     }
                                     QSpinBox:up-button:pressed{
                                        background: #4780a5;
                                     }
                                     QSpinBox:up-arrow{
                                        width: 8px;
                                        height: 8px;
                                        background:#ec2400;
                                     }
                                     QSpinBox:up-arrow:hover{
                                        width: 8px;
                                        height: 8px;
                                        background:#9F8170;
                                     }
                                     QSpinBox:down-button{
                                        subcontrol-origin: border;
                                        width: 20px;
                                        border: 2px solid #A9A9A9;
                                        background-color: pink;
                                     }
                                     QSpinBox:down-button:hover{
                                        border: 2px solid blue;
                                        background: green;
                                     }
                                     QSpinBox:down-button:pressed{
                                        background: #4780a5;
                                     }
                                     QSpinBox:down-arrow{
                                        width: 8px;
                                        height: 8px;
                                        background:purple;
                                     }
                                     QSpinBox:down-arrow:hover{
                                        background:#9F8170;
                                     }
                                                                
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_combo, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.spin1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.spin2, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = SpinWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()