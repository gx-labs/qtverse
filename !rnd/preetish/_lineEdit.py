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
                                        QLineEdit {
                                            width: 210px;
                                            height: 50px;
                                            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(227, 213, 255), stop:1 rgba(255, 231, 231));
                                            border-radius: 30px;
                                            letter-spacing: 0.8px;
                                            padding-left: 15px;
                                            cursor: pointer;
                                            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.075);
                                        }

                                        QLineEdit::hover {
                                            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(197, 184, 255), stop:1 rgba(255, 211, 211));
                                        }

                                        QLineEdit:focus {
                                            border: 2px solid rgb(255, 81, 0);
                                        }
        """)

        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setMinimumSize(300,10)
        self.lineEdit4.setPlaceholderText("Write Here")
        self.lineEdit4.setStyleSheet("""
                                        QLineEdit {
                                            color: #8707ff;
                                            border: 2px solid #8707ff;
                                            border-radius: 10px;
                                            padding: 10px 25px;
                                            background: transparent;
                                            max-width: 190px;
                                            }

                                        QLineEdit:active {
                                            shadow: 2px 2px 15px #8707ff inset;
                                            }

        """)

        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setMinimumSize(300,10)
        self.lineEdit5.setPlaceholderText("Write Here")
        self.lineEdit5.setStyleSheet("""
                                        QLineEdit {
                                            border: 2px solid transparent;
                                            width: 15em;
                                            height: 2.5em;
                                            padding-left: 0.8em;
                                            outline: none;
                                            background-color: #F3F3F3;
                                            border-radius: 10px;
                                        }

                                        QLineEdit:hover, QLineEdit:focus {
                                            border: 2px solid #4A9DEC;
                                            background-color: white;
                                            selection-background-color: #4A9DEC;
                                        }
        """)


        self.setLayout(layout)
        layout.addWidget(self.lineEdit1, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineEdit2, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineEdit3, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineEdit4, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineEdit5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

