import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class CheckboxWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Checkbox Styles")
        self.setFixedSize(QSize(500, 500))

        self.checkbox1 = QCheckBox("Hit me up")
        self.checkbox1.setStyleSheet('''QCheckBox{
                                     font: bold italic "Times New Roman";
                                     }
                                     ''')
        
        self.checkbox2 = QCheckBox("Circular check")
        self.checkbox2.setStyleSheet('''
                                        QCheckBox{
                                            font-weight: bold;
                                            font-size: 13px;
                                            background-color: white;
                                            color: #3498db;
                                            border: 2px solid #3498db;
                                            border-radius: 20px;
                                            padding: 10px;
                                        }
                                        QCheckBox:indicator{
                                            width: 20px;
                                            height: 20px;
                                        }
                                        QCheckBox:indicator:unchecked{
                                            border-radius: 10px;
                                            border: 2px solid grey;
                                            background-color: #D3D3D3;
                                        }
                                        QCheckBox:indicator:checked{
                                            border-radius: 10px;
                                            border: 2px solid #3498db;
                                            background-color: pink;
                                        }
                                        QCheckBox:indicator:unchecked:hover{
                                            border: 2px solid #3498db;
                                        }
            ''')
        
        self.checkbox3 = QCheckBox()
        self.checkbox3.setStyleSheet('''
                                        QCheckBox{
                                            background-color: transparent;
                                        }
                                        QCheckBox:indicator{
                                            width: 20px;
                                            height: 20px;
                                            border: 2px solid black;
                                            border-radius: 10px;
                                            background-color:#D3D3D3;
                                        }
                                        QCheckBox:indicator:checked{
                                            background-color: qradialgradient(spread:pad,
                                                                    cx:0.5, cy:0.5, 
                                                                    radius:0.9, 
                                                                    fx:0.5, fy:0.5, 
                                                                    stop:0 rgba(255, 165, 0, 255), 
                                                                    stop:1 rgba(139, 69, 0, 255));
                                            
                                        }
                                        QCheckBox:checked {
                                            background-color: qradialgradient(spread:pad, 
                                                                    cx:0.739, 
                                                                    cy:0.278364, 
                                                                    radius:0.378, 
                                                                    fx:0.997289, 
                                                                    fy:0.00289117, 
                                                                    stop:0 rgba(255, 255, 255, 255), 
                                                                    stop:1 rgba(160, 160, 160, 255));
                                        }
        ''')

        self.checkbox4 = QCheckBox()
        self.checkbox4.setStyleSheet('''
                                        
                                        QCheckbox:indicator:unchecked{
                                            border: 2px solid #D3D3D3;
                                            background-color: white;
                                        }
                                        QCheckbox:indicator:checked{
                                            border: 2px solid black;
                                        }
                                        QCheckbox:indicator:unchecked:hover{
                                            border: 2px solid black;
                                        }
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.checkbox1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.checkbox2, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.checkbox3, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.checkbox4, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = CheckboxWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()