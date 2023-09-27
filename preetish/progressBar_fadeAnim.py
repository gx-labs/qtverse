import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtCore import Qt, QTimer

class CircularProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.progress = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(100)

    def initUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Circular Progress Bar')

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 200)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            background-color: transparent;
            border: 10px solid qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0078FF, stop:1 #00FFA8);
            border-radius: 100px;
        """)

    def updateProgress(self):
        self.progress += 1
        if self.progress > 100:
            self.progress = 0

        style_sheet = f"""
            background-color: transparent;
            border: 10px solid qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0078FF, stop:{1 - self.progress/100} transparent);
            border-radius: 100px;
        """
        self.label.setStyleSheet(style_sheet)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircularProgressBar()
    window.show()
    sys.exit(app.exec_())
