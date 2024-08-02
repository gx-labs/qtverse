import sys
import os

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(150,150)
        
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
        strokeWidth = 7
        
        # Create painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Background
        painter.fillRect(event.rect(), Qt.transparent)
        
        # Progress arc
        progress_color = QColor("#000000")  # Black color
        progress_rect = QRectF(margin, margin, side - margin * 2, side - margin * 2)
        painter.setPen(Qt.NoPen)  
        painter.setBrush(QBrush(progress_color))  
        start_angle = 90 * 16  
        span_angle = -(self.progress_bar * 360 / 100) * 16  
        painter.drawPie(progress_rect, start_angle, span_angle)
        
        # Text
        font = QFont()
        font.setPointSize(16)
        painter.setFont(font)
        painter.setPen(QColor("#FFFFFF"))
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
