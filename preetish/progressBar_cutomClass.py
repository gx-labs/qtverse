import sys
import random
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QProgressBar

class ProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        self.setValue(0)
        if self.minimum() != self.maximum():
            self.timer = QTimer(self, timeout=self.onTimeout)
            self.timer.start(random.randint(1, 3) * 1000)

    def onTimeout(self):
        if self.value() >= 100:
            self.timer.stop()
            self.timer.deleteLater()
            del self.timer
            return
        self.setValue(self.value() + 1)

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self)

        red_progressbar1 = ProgressBar(self, minimum=0, maximum=100)
        red_progressbar1.setStyleSheet('''
            QProgressBar{
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #F44336;
            }
        ''')
        layout.addWidget(red_progressbar1)

        red_progressbar2 = ProgressBar(self, minimum=0, maximum=0)
        red_progressbar2.setStyleSheet('''
            QProgressBar{
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #F44336;
            }
        ''')
        layout.addWidget(red_progressbar2)

        green_progressbar1 = ProgressBar(self, minimum=0, maximum=100)
        green_progressbar1.setStyleSheet('''
            QProgressBar {
                min-height: 12px;
                max-height: 12px;
                text-align: center;
                border-radius: 6px;
            }
            QProgressBar::chunk {
                border-radius: 6px;
                background-color: #009688;
            }
        ''')
        layout.addWidget(green_progressbar1)

        green_progressbar2 = ProgressBar(self, minimum=0, maximum=0)
        green_progressbar2.setStyleSheet('''
            QProgressBar {
                min-height: 12px;
                max-height: 12px;
                text-align: center;
                border-radius: 6px;
            }
            QProgressBar::chunk {
                border-radius: 6px;
                background-color: #009688;
            }
        ''')
        layout.addWidget(green_progressbar2)

        blue_progressbar1 = ProgressBar(self, minimum=0, maximum=100)
        blue_progressbar1.setStyleSheet('''
            QProgressBar{
                border: 2px solid #2196F3;
                text-align: center;
                border-radius: 5px;
                background-color: #E0E0E0;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                width: 10px;
                margin: 0.5px;
            }
        ''')
        layout.addWidget(blue_progressbar1)

        blue_progressbar2 = ProgressBar(self, minimum=0, maximum=0)
        blue_progressbar2.setStyleSheet('''
            QProgressBar{
                border: 2px solid #2196F3;
                text-align: center;
                border-radius: 5px;
                background-color: #E0E0E0;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                width: 10px;
                margin: 0.5px;
            }
        ''')
        layout.addWidget(blue_progressbar2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
