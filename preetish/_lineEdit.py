import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle('Scroll Bar')
        self.setFixedSize(800,800)

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("Write Here")
        self.lineEdit1.setMinimumSize(300,10)
        self.lineEdit1.setStyleSheet("""
                                        QLineEdit {
                                            border-radius: 12px;
                                            border: 1.5px solid blue;
                                            background-color: white;
                                            padding: 12px;
                                        }
                                        QLineEdit:hover {
                                            border: 2px solid yellow;
                                        }
                                        QLineEdit:active {
                                            transform: scale(0.95);
                                        }
                                        QLineEdit:focus {
                                            border: 2px solid green;
                                        }
        """)

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Write Here")
        self.lineEdit2.setMinimumSize(300,10)
        self.lineEdit2.setStyleSheet("""
                                        QLineEdit {
                                            background-color: rgb(27, 29, 35);
                                            border-radius: 12px;
                                            color: white;
                                            border: 2px solid rgb(27, 29, 35);
                                            padding: 10px;
                                        }
                                        QLineEdit:hover {
                                            border: 2px solid rgb(64, 71, 88);
                                        }
                                        QLineEdit:focus {
                                            border: 2px solid rgb(91, 101, 124);
                                        }
        """)

        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setPlaceholderText("Write Here")
        self.lineEdit3.setMinimumSize(300,10)
        self.lineEdit3.setStyleSheet("""
        
        """)


        self.setLayout(layout)
        layout.addWidget(self.lineEdit1, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineEdit2, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineEdit3, alignment=Qt.AlignCenter)
        # layout.addWidget(self.lineEdit4, alignment=Qt.AlignCenter)
        # layout.addWidget(self.lineEdit5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

