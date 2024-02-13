import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2extn.RoundProgressBar import roundProgressBar 

x = 0
p = 1

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
            
        layout = QVBoxLayout()
      
        self.round_progress_bar = roundProgressBar()

        #style
        self.round_progress_bar.rpb_setBarStyle('Pizza')
        #circle
        self.round_progress_bar.rpb_setCircleColor((187,226,146))  
        #text
        self.round_progress_bar.rpb_setTextColor((78,147,6))  
        self.round_progress_bar.rpb_setTextRatio(4)
        #line
        self.round_progress_bar.rpb_setLineColor((78,147,6)) 
                                                  
        layout.addWidget(self.round_progress_bar)
        self.setLayout(layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)
        
    def update_progress(self):
        global x
        x += 2  # Adjust the increment to your desired speed
        if x >= 100:
            x = 0
        self.round_progress_bar.rpb_setValue(x)
     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())