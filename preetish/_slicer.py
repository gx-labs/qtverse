import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCheckBox, QSlider
from PySide2.QtCore import Qt, QPropertyAnimation, QRect

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBoxes")
        self.setFixedSize(800,800)
        layout = QVBoxLayout()

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMinimumSize(300, 40) 
        self.slider1.setStyleSheet("""
            QSlider {
                border: none;
                background: #D5DBE1;
                height: 10px;
                border-radius: 5px;
                opacity: 0.7;
                transition: opacity .2s;
            }

            QSlider::handle {
                width: 15px;
                height: 15px;
                border-radius: 50%;
                background-color: #000000;
            }

            QSlider::handle:pressed {
                background-color: #000000;
                margin-left: -5px; /* Add a slight animation effect when pressed */
            }

            QSlider::handle:hover {
                background-color: #000000;
                box-shadow: 0px 0px 0px 8px rgba(0, 0, 0, 0.16);
            }
        """)


        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMinimumSize(300, 40)
        self.slider2.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 2px;
            }

            QSlider::handle:horizontal {
                background: #2a2a2a;
                width: 10px;
                margin: -5px -1px;
                border-radius: 5px;
                border: 1px solid #2a2a2a
            }

            QSlider::add-page:horizontal{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0, #B1B1B1, stop:1, #c4c4c4)
            }

            QSlider::sub-page:horizontal{
                background: #2a2a2a
            }
        """)
        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.setMinimumSize(300, 40)
        self.slider3.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 10px;
            }

            QSlider::handle:horizontal {
                background: #fff;
                width: 10px;
                margin: -1px -1px;
                border-radius: 5px;
                border: 1px solid #5555ff;
            }

            QSlider::add-page:horizontal{
                background: qlineargradient(
                    spread:pad,x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgba(188,231,215,255), 
                stop:1 rgba(122,215,255,255))
            }

            QSlider::sub-page:horizontal{
                background: qlineargradient(spread:pad,x1:1, y1:0.585, x2:0, y2:0.556818, 
                stop:0 rgba(132,76,171,255), 
                stop:1 rgba(122,130,255,255))
            }
        
        """)
        self.slider4 = QSlider(Qt.Horizontal)
        self.slider4.setMinimumSize(300, 40)
        self.slider4.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 6px;
                width: 350px;
                background: grey;
                margin: 8px;
                border: 1px solid #c17d08;
                border-radius: 12px;
            }

            QSlider::sub-page:horizontal {
                background: #c17d08;
                height: 6px;
                border-radius: 12px;
            }

            QSlider::add-page:horizontal {
                background: #e9e9e9;
                height: 10px;
                border-radius: 12px;
            }

            QSlider::handle:horizontal {
                background: transparent;
                width: 22px;
                margin: -10px;
                border: 1px solid transparent;
                border-radius: 5px;
            }
        """)

        self.setLayout(layout)
        layout.addWidget(self.slider1, alignment=Qt.AlignCenter)
        layout.addWidget(self.slider2, alignment=Qt.AlignCenter)
        layout.addWidget(self.slider3, alignment=Qt.AlignCenter)
        layout.addWidget(self.slider4, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
