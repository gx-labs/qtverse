import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBoxes")
        self.setFixedSize(800,800)
        layout = QVBoxLayout()

        self.spinbox1 = QSpinBox()
        self.spinbox1.setMinimumSize(300, 40)
        self.spinbox1.setStyleSheet("""

                                     QSpinBox{
                                        width: 8em;
                                        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 white, stop: 1 grey);
                                        border: 2px solid grey;
                                        border-radius: 10px;
                                        padding: 10px;
                                        color: black;
                                        font-weight: bold;
                                        selection-background-color: white;
                                        selection-color: blue;
                                     }
                                     QSpinBox:up-button{
                                        subcontrol-origin: border;
                                        width: 20px;
                                        border: 2px solid white;
                                        background: black;

                                     }
                                     QSpinBox:up-button:hover{
                                        border: 2px solid blue;
                                        background: blue;
                                     }
                                     QSpinBox:up-button:pressed{
                                        background: blue;
                                     }
                                     QSpinBox:up-arrow{
                                        width: 8px;
                                        height: 8px;
                                        background: white;
                                     }
                                     QSpinBox:up-arrow:hover{
                                        width: 8px;
                                        height: 8px;
                                        background:#9F8170;
                                     }
                                     QSpinBox:down-button{
                                        subcontrol-origin: border;
                                        width: 20px;
                                        border: 2px solid white;
                                        background: black;

                                     }
                                     QSpinBox:down-button:hover{
                                        border: 2px solid blue;
                                        background: blue;
                                     }
                                     QSpinBox:down-button:pressed{
                                        background: blue;
                                     }
                                     QSpinBox:down-arrow{
                                        width: 8px;
                                        height: 8px;
                                        background: white;
                                     }
                                     QSpinBox:down-arrow:hover{
                                        width: 8px;
                                        height: 8px;
                                        background:#9F8170;
                                     }
        """)

        self.spinbox2 = QSpinBox()
        self.spinbox2.setAlignment(Qt.AlignCenter)
        self.spinbox2.setGeometry(0, 0, 200, 200)
        self.spinbox2.setStyleSheet("""
            QSpinBox {
                background-color: #f0f0f0;
                color: #333;
                border: 2px solid #999;
                border-radius: 5px;
            }

            QSpinBox::up-button, QSpinBox::down-button {
                width: 40px;
                border: 2px solid #999;
                border-radius: 5px;
            }
        """)

        self.setLayout(layout)
        layout.addWidget(self.spinbox1, alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox1, alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox2, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()