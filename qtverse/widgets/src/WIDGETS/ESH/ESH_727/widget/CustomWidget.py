from random import randint
import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
 
css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")
 
class ProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setValue(0)
        self.setFixedSize(350, 30)
        self.setStyleSheet(css_data)
        if self.minimum() != self.maximum():
            self.timer = QTimer(self, timeout=self.update_progress)
            self.timer.start(randint(1, 3) * 1000)
 
    def update_progress(self):
        if self.value() >= 100:
            self.timer.stop()
            self.timer.deleteLater()
            del self.timer
            return
        self.setValue(self.value() + 1)
  
class CustomWidget(QWidget):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
       
        layout.addWidget(  
            ProgressBar(self, minimum=0, maximum=0, textVisible=False))
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())



