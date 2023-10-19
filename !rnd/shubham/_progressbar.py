import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle('Progress Bar')
        self.setFixedSize(800,800)

        self.progressBar1 = QProgressBar(self)
        self.progressBar1.setMinimumSize(300,40)
        self.progressBar1.setValue(50)
        self.progressBar1.setStyleSheet("""
QProgressBar {
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
    font-style: bold;
}

QProgressBar::chunk {
    background-color: #05B8CC;
    width: 20px;
}
        """)

        self.progressBar2 = QProgressBar(self)
        self.progressBar2.setMinimumSize(300,40)
        self.progressBar2.setValue(50)
        self.progressBar2.setStyleSheet("""
                                            QProgressBar {
                                                border: 2px solid gray;
                                                border-radius: 5px;
                                                color: white;
                                                text-align: left;
                                            }
                                            QProgressBar::chunk {
                                                background-color: red;
                                                width: 20px;
                                            }
        """)

        self.progressBar3 = QProgressBar(self)
        self.progressBar3.setMinimumSize(300,40)
        self.progressBar3.setValue(50)
        self.progressBar3.setStyleSheet("""
                                            QProgressBar {
                                                border: 2px solid gray;
                                                border-radius: 5px;
                                                text-align: center;
                                                background-color: white;

                                            }
                                            QProgressBar::chunk {
                                                background-color: black;
                                                width: 5px;
                                                margin: 3px;
                                            }
        """)



        self.setLayout(layout)
        layout.addWidget(self.progressBar1, )
        layout.addWidget(self.progressBar2, )
        layout.addWidget(self.progressBar3, )


def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()