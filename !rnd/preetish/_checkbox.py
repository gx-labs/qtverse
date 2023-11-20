import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCheckBox
from PySide2.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBoxes")
        self.setFixedSize(800,800)
        layout = QVBoxLayout()

        self.checkbox1 = QCheckBox("Check me")
        self.checkbox1.setStyleSheet("""
                                        QCheckBox {
                                            background-color: transparent;
                                            border: 2px solid #3498db;
                                            border-radius: 5px;
                                            padding: 5px;
                                            color: #3498db;
                                        }

                                        QCheckBox::indicator {
                                            width: 20px;
                                            height: 20px;
                                            transform-origin: center;
                                        }

                                        QCheckBox::indicator:checked {
                                            background-color: #3498db;
                                            border: 2px solid #3498db;
                                            border-radius: 5px;
                                            animation: flip 0.5s;
                                        }

                                        QCheckBox::indicator:unchecked {
                                            background-color: transparent;
                                            border: 2px solid #3498db;
                                            border-radius: 5px;
                                        }
                                        
                                        @keyframes flip {
                                            0% {
                                                transform: rotateY(0deg);
                                            }
                                            100% {
                                                transform: rotateY(180deg);
                                            }
                                        }
        """)


        self.checkbox2 = QCheckBox()
        self.checkbox2.setStyleSheet("""
                                        QCheckBox::indicator {
                                            width: 30px;
                                            height: 30px;
                                            background-color: gray;
                                            border-radius: 15px;
                                            border-style: solid;
                                            border-width: 1px;
                                            border-color: white white black black;
                                        }
                                        QCheckBox::indicator:checked {
                                            background-color: qradialgradient(spread:pad, 
                                                                    cx:0.5,
                                                                    cy:0.5,
                                                                    radius:0.9,
                                                                    fx:0.5,
                                                                    fy:0.5,
                                                                    stop:0 rgba(0, 255, 0, 255), 
                                                                    stop:1 rgba(0, 64, 0, 255));
                                        }
                                        QCheckBox:checked, QCheckBox::indicator:checked {
                                            border-color: black black white white;
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
        """)
        self.checkbox3 = QCheckBox()
        self.checkbox3.setStyleSheet("""
                                        QCheckBox::indicator {
                                            border: 3px solid rgb(52, 59, 72);
                                            width: 15px;
                                            height: 15px;
                                            border-radius: 10px;
                                            background: rgb(44, 49, 60);
                                        }
                                        QCheckBox::indicator:hover {
                                            border: 3px solid rgb(58, 66, 81);
                                        }
                                        QCheckBox::indicator:checked {
                                            background: 3px solid red;
                                            border: 3px solid rgb(52, 59, 72);	
                                        }
        """)
        self.checkbox4 = QCheckBox()
        self.checkbox4.setStyleSheet("""
        """)
        self.checkbox5 = QCheckBox()



        self.setLayout(layout)
        layout.addWidget(self.checkbox1, alignment=Qt.AlignCenter)
        layout.addWidget(self.checkbox2, alignment=Qt.AlignCenter)
        layout.addWidget(self.checkbox3, alignment=Qt.AlignCenter)
        layout.addWidget(self.checkbox4, alignment=Qt.AlignCenter)
        layout.addWidget(self.checkbox5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
