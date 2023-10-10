import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class PracWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Progress Styles")
        self.setFixedSize(QSize(500, 500))

        self.prgsbar1 = QProgressBar()
        self.prgsbar1.setValue(56)
        self.prgsbar1.setStyleSheet('''
                                   QProgressBar{
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                        text-align: center;
                                   }
                                    QProgressBar:chunk{
                                        background-color: #CD96CD;
                                        width: 10px;
                                        margin: 0.5px;
                                    }
        ''')
        self.prgsbar2 = QProgressBar()
        self.prgsbar2.setValue(56)
        self.prgsbar2.setStyleSheet('''
                                    QProgressBar{
                                        border: 2px solid pink;
                                        border-radius: 5px;
                                        text-align: center;
                                    }
                                    QProgressBar:chunk{
                                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.1 #32CD32, stop:0.2 yellow, stop:0.3 #32CD32, stop:0.4 yellow, stop:0.5 #32CD32, stop:0.6 yellow, stop:0.8 yellow, stop:0.9 #32CD32, stop:0.98 #32CD32);
                                        border-radius: 5px;
                                        margin: 0.5px;   
                                    }
        ''')

        self.prgsbar3 = QProgressBar()
        self.prgsbar3.setValue(56)
        self.prgsbar3.setStyleSheet('''
                                    QProgressBar{
                                        border: 2px solid brown;
                                        border-radius: 5px;
                                        text-align: center;
                                        font-weight: bold;
                                        color: red;
                                        font-size: 18px; 
                                    }
                                    QProgressBar:chunk{
                                        background-color: pink;
                                        width: 5px;
                                        margin: 0.5px;
                                    }
        ''')

        self.prgsbar4 = QProgressBar()
        self.prgsbar4.setValue(56)
        self.prgsbar4.setStyleSheet('''
                                    QProgressBar{
                                        border: 2px solid brown;
                                        border-radius: 5px;
                                        text-align: center;
                                        font-weight: bold;
                                        color: yellow; 
                                    }
                                    QProgressBar:chunk{
                                        background-color: #00ecff;
                                        border-radius: 5px;
                                        margin: 0.5px;
                                    }
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.prgsbar1)
        self.layout.addWidget(self.prgsbar2)
        self.layout.addWidget(self.prgsbar3)
        self.layout.addWidget(self.prgsbar4)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = PracWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

