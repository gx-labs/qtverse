import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QPainter, QColor, QPen

class CircularProgressWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('Circular Progress Bar')
        
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(50)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
                                    QLabel{ 
                                        color : #333; 
                                        background-color: transparent; 
                                        }
                                """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def updateProgress(self):
        self.angle += 1
        if self.angle > 360:
            self.angle = 0
        self.label.setText(f"{int(self.angle / 3.6)}%")
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor("#E0E0E0"))
        painter.setPen(pen)

        painter.drawArc(10, 10, width - 20, height - 20, 0, 360 * 16)
        
        pen.setColor(QColor("#4CAF50"))
        painter.setPen(pen)
        
        painter.drawArc(10, 10, width - 20, height - 20, 90 * 16, -self.angle * 16)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = CircularProgressWidget()
    main_widget.show()
    sys.exit(app.exec_())
