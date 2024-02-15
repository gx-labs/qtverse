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
        self.setFixedSize(140, 140)
            
        layout = QVBoxLayout()
      
        self.round_progress_bar = roundProgressBar()
     
        #style
        self.round_progress_bar.rpb_setBarStyle('Hybrid1')
        #text
        self.round_progress_bar.rpb_setTextColor((0,0,0))  
        self.round_progress_bar.rpb_setTextRatio(8)
        #line
        self.round_progress_bar.rpb_setLineColor((191,188,188)) 
        self.round_progress_bar.rpb_setLineWidth(5)
        self.round_progress_bar.rpb_setLineCap('RoundCap')
        #start position
        self.round_progress_bar.rpb_setInitialPos('East') 
        #path
        self.round_progress_bar.rpb_setPathWidth(2)
        self.round_progress_bar.rpb_setPathColor((0, 0, 0))
                                                  
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