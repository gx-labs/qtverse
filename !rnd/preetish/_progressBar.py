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
                                            QProgressBar
                                            {
                                                border: 1px solid #222222;
                                                background-color: #3d3d3d;
                                                text-align: center;
                                                color: #ffffff;
                                                font-size: 12px;
                                                font-weight: bold;
                                                padding: 1px;
                                                border-radius: 3px;
                                            }
                                            QProgressBar::chunk
                                            {
                                                background-color: #607cff;
                                            }
        """)

        self.progressBar2 = QProgressBar(self)
        self.progressBar2.setMinimumSize(300,40)
        self.progressBar2.setValue(50)
        self.progressBar2.setStyleSheet("""
                                            QProgressBar {
                                                border: 1px solid #ccc;
                                                border-radius: 5px;
                                                text-align: center;
                                                background-color: #eee;
                                            }

                                            QProgressBar::chunk {
                                                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.05 #0078D7, stop:0.1 #0078D7, stop:0.2 transparent, stop:0.8 transparent, stop:0.9 #0078D7, stop:0.95 #0078D7);
                                                border-radius: 5px;
                                            }
        """)

        self.progressBar3 = QProgressBar(self)
        self.progressBar3.setMinimumSize(300,40)
        self.progressBar3.setValue(50)
        self.progressBar3.setStyleSheet("""
                                            QProgressBar{
                                                background-color : yellow;
                                                text-align: center;
                                                border : 1px
                                            }

                                            QProgressBar::chunk{
                                                background : blue;
                                            }
        """)

        self.progressBar4 = QProgressBar(self)
        self.progressBar4.setMinimumSize(300,40)
        self.progressBar4.setValue(50)
        self.progressBar4.setStyleSheet("""
                                            QProgressBar {
                                                border: 2px solid gray;
                                                border-radius: 5px;
                                                color: white;
                                                text-align: center;
                                            }
                                            QProgressBar::chunk {
                                                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #000000, stop:1 #333333);
                                                width: 20px;
                                            }
        """)

        self.progressBar5 = QProgressBar(self)
        self.progressBar5.setMinimumSize(300,40)
        self.progressBar5.setValue(50)
        self.progressBar5.setStyleSheet("""
                                            QProgressBar {
                                                border: 2px solid gray;
                                                border-radius: 5px;
                                                text-align: center;
                                            }
                                            QProgressBar::chunk {
                                                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #78d0ff, stop:1 #0078d0);
                                                width: 5px;
                                                margin: 0.5px;
                                            }
        """)


    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.updateProgressBar)
    #     self.timer.start(100)  # Update the progress bar every 100 milliseconds

    # def updateProgressBar(self):
    #     value = self.progressBar3.value()
    #     if value < 100:
    #         self.progressBar3.setValue(value + 1)
    #     else:
    #         self.timer.stop()

        self.setLayout(layout)
        layout.addWidget(self.progressBar1, alignment=Qt.AlignCenter)
        layout.addWidget(self.progressBar2, alignment=Qt.AlignCenter)
        layout.addWidget(self.progressBar3, alignment=Qt.AlignCenter)
        layout.addWidget(self.progressBar4, alignment=Qt.AlignCenter)
        layout.addWidget(self.progressBar5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

