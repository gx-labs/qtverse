import sys
import os

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(170,170)
        
        self.progress_bar = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)  

    def paintEvent(self, event):
        # Constants
        width = self.width()
        height = self.height()
        side = min(width, height)
        margin = 20
        pathWidth = 10
        strokeWidth = 10

        # Create painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Background
        painter.fillRect(event.rect(), Qt.transparent)

        # Path
        pen = QPen(QColor("#D8EBEA"))  
        pen.setWidth(pathWidth)
        pen.setCapStyle(Qt.SquareCap)  
        painter.setPen(pen)
        painter.drawArc(margin, margin, side - margin * 2, side - margin * 2, 90 * 16, 360 * 16)

        # Progress arc
        pen = QPen(QColor("#89E6E4"))
        pen.setWidth(strokeWidth)
        pen.setCapStyle(Qt.SquareCap)  
        painter.setPen(pen)
        painter.drawArc(margin, margin, side - margin * 2, side - margin * 2, 90 * 16, -(self.progress_bar * 360 // 100) * 16)

        # Text
        font = QFont()
        font.setPointSize(16)
        painter.setFont(font)
        painter.setPen(QColor("#000000"))
        painter.drawText(event.rect(), Qt.AlignCenter, "{}%".format(self.progress_bar))


        
    def update_progress(self):
        self.progress_bar += 1
        if self.progress_bar > 100:
            self.progress_bar = 0
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())