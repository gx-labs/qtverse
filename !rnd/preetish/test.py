import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QColor, QBrush

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setup_ui()

    def setup_ui(self):
        button = QPushButton("Click Me", self)
        button.setGeometry(150, 80, 100, 40)

        # Apply styles using CSS
        button.setStyleSheet('''
            QPushButton {
                background: rgb(145, 92, 182);
                color: rgba(255, 255, 255, 0.8);
                border-radius: 4px;
                font-weight: normal;
                text-transform: uppercase;
            }
            QPushButton:hover {
                color: rgba(255, 255, 255, 1);
            }
        ''')

    def paintEvent(self, event):
        # Add a custom box shadow to the widget
        shadow = QPainter(self)
        shadow.setRenderHint(QPainter.Antialiasing)
        shadow.setBrush(QBrush(QColor(0, 0, 0, 128)))
        shadow.setPen(Qt.NoPen)
        shadow.drawRoundedRect(150, 80, 100, 40, 4, 4)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
