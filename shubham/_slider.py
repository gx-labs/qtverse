import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class SliderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create four QSlider widgets
        slider1 = QSlider(Qt.Horizontal)
        slider2 = QSlider(Qt.Horizontal)
        slider3 = QSlider(Qt.Vertical)
        slider4 = QSlider(Qt.Vertical)

        # Apply different stylesheets for handle and overall look
        slider1.setStyleSheet(
            """
                                QSlider {
                                        border: groove;
                                        background: #D5DBE1;
                                        height: 25px;
                                        border-radius: 10px;
                                        opacity: 0.7;
                                    }

                                    QSlider::handle {
                                        width: 30px;
                                        height: 30px;
                                        border-radius: 20%;
                                        background-color: #000000;
                                    }

                                    QSlider::handle:pressed {
                                        background-color: blue;
                                        margin-left: -10px; /* Add a slight animation effect when pressed */
                                    }

                                    QSlider::handle:hover {
                                        background-color: grey;
                                    }
            """
        )

        slider2.setStyleSheet(
            """
            QSlider::groove:horizontal {
                background: lightgray;
                border: 1px solid #222222;
                height: 10px;
                border-radius: 5px;
            }

            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E74C3C, stop:1 #D35400);
                border: 1px solid #222222;
                width: 20px;
                margin: -5px 0px;
                border-radius: 10px;
            }
            """
        )

        slider3.setStyleSheet(
            """
QSlider::groove:vertical {
    background: red;
    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */
    left: 4px; right: 4px;
}

QSlider::handle:vertical {
    height: 10px;
    background: Red;
    margin: 0 -4px; /* expand outside the groove */
}

QSlider::add-page:vertical {
    background: white;
}

QSlider::sub-page:vertical {
    background: pink;
}
            """
        )

        slider4.setStyleSheet(
            """
            QSlider::groove:vertical {
                background: lightgray;
                border: 1px solid #222222;
                width: 10px;
                border-radius: 5px;
            }

            QSlider::handle:vertical {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #8E44AD, stop:1 #F39C12);
                border: 1px solid #222222;
                height: 20px;
                margin: 0px -5px;
                border-radius: 10px;
            }
            """
        )

        layout.addWidget(slider1)
        layout.addWidget(slider2)
        layout.addWidget(slider3)
        layout.addWidget(slider4)

        self.setLayout(layout)

        self.setWindowTitle('Styled Sliders')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SliderApp()
    ex.show()
    sys.exit(app.exec_())
