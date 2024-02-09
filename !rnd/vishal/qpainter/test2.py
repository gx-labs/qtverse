from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide2.QtGui import QPainter, QColor, QLinearGradient
from PySide2.QtCore import Qt

class GradientButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(200, 50)  # Set button size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

      
        gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        gradient.setColorAt(0.0, QColor(150, 150, 150))  
        gradient.setColorAt(1.0, QColor(100, 100, 100))  
        
        painter.fillRect(self.rect(), gradient)

        # Draw button text
        painter.setPen(Qt.white)  # Text color
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    button = GradientButton("Gradient Button")
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec_()
