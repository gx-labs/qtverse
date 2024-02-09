from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtGui import QPainter, QColor, QLinearGradient
from PySide2.QtCore import Qt

class GradientButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(200, 50) 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Create a gradient
        gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        gradient.setColorAt(0.0, QColor(255, 0, 0))  
        gradient.setColorAt(1.0, QColor(0, 0, 255))  

      
        painter.fillRect(self.rect(), gradient)

       
        painter.setPen(Qt.white) 
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

if __name__ == "__main__":
    app = QApplication([])
    button = GradientButton("Gradient Button")
    button.show()
    app.exec_()
