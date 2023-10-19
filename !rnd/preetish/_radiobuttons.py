import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class RadioButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Radio Buttons")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.radio_button1 = QRadioButton("Option 1")
        self.radio_button1.setStyleSheet("""
                                        QRadioButton {
                                            color: #333;
                                        }
                                        QRadioButton::indicator {
                                            width: 15px; 
                                            height: 15px; 
                                            border: 2px solid #0078d4;
                                            border-radius: 7px;
                                        }
                                        QRadioButton::indicator:checked {
                                            background-color: #0078d4;
                                        }
            """)

        self.radio_button2 = QRadioButton("Option 2")
        self.radio_button2.setStyleSheet("""
                                            QRadioButton {
                                                color: #555;
                                            }
                                            QRadioButton::indicator {
                                                width: 20px;
                                                height: 20px;
                                            }
                                            QRadioButton::indicator:unchecked {
                                                background-color: #f2f2f2;
                                                border: 2px solid #999;
                                                border-radius: 10px;
                                            }
                                            QRadioButton::indicator:checked {
                                                background-color: #ff6f61;
                                                border: 2px solid #ff6f61;
                                            }
                                            QRadioButton::indicator:unchecked:hover {
                                                background-color: #e0e0e0;
                                            }
        """)
        
        self.radio_button3 = QRadioButton("Option 3")
        self.radio_button3.setStyleSheet("""
                                        QRadioButton::indicator {
                                            border: 3px solid rgb(52, 59, 72);
                                            width: 15px;
                                            height: 15px;
                                            border-radius: 10px;
                                            background: rgb(44, 49, 60);
                                        }
                                        QRadioButton::indicator:hover {
                                            border: 3px solid rgb(58, 66, 81);
                                        }
                                        QRadioButton::indicator:checked {
                                            background: 3px solid red;
                                            border: 3px solid rgb(52, 59, 72);	
                                        }
        """)

        layout.addWidget(self.radio_button1, alignment=Qt.AlignCenter)
        layout.addWidget(self.radio_button2, alignment=Qt.AlignCenter)
        layout.addWidget(self.radio_button3, alignment=Qt.AlignCenter)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = RadioButtonWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()