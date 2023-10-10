import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBoxes")
        self.setFixedSize(800,800)
        layout = QVBoxLayout()

        self.spinbox1 = QSpinBox()
        self.spinbox1.setMinimumSize(300, 40)
        self.spinbox1.setStyleSheet("""
                                        QSpinBox{
                                            color: black;
                                            font-weight: bold;
                                            background: transparent;
                                            height: 25px;
                                        }
                                        
                                        QSpinBox::down-button, QSpinBox::up-button {
                                            subcontrol-origin: border;
                                            background: #40dcda;
                                            width: 20px;
                                            height: 25px;
                                        }
                                        
                                        QSpinBox::down-button {
                                            subcontrol-position: center left;
                                            border-bottom-left-radius: 3px;
                                            border-top-left-radius: 3px;
                                        }
                                        
                                        QSpinBox::up-button {
                                            subcontrol-position: center right;
                                            border-bottom-right-radius: 3px;
                                            border-top-right-radius: 3px;
                                        }
                                        
                                        QSpinBox::up-button:hover,
                                        QSpinBox::down-button:hover {
                                            background: #788787;
                                        }
                                        
                                        QSpinBox::up-button:pressed,
                                        QSpinBox::down-button:pressed {
                                            background: #40dcda;
                                        }
                                        
                                        
                                        QSpinBox::up-arrow, QSpinBox::down-arrow {
                                            subcontrol-origin: content;
                                            width: 12px;
                                            height: 12px;
                                        }
                                        
                                        QSpinBox::up-arrow{
                                            image: url(:/images/plus.png);
                                        }
                                        
                                        QSpinBox::down-arrow{
                                            image: url(:/images/minus.png);
                                        }
        """)

        self.spinbox2 = QSpinBox()
        self.spinbox2.setMinimumSize(300, 40)
        self.spinbox2.setStyleSheet("""
                                        QSpinBox {
                                            color: black;
                                            font-weight: bold;
                                            background-color: transparent;
                                            border-style: none;
                                            width: 24px;
                                        }
                                        
                                        QSpinBox::down-button, QSpinBox::up-button {
                                            subcontrol-origin: margin;
                                            background: #3d525f;
                                            width: 24px;
                                            height: 24px;
                                        }
                                        
                                        QSpinBox::down-button {
                                            subcontrol-position: center left;
                                        }
                                        
                                        QSpinBox::up-button {
                                            subcontrol-position: center right;
                                        }
                                        
                                        QSpinBox::down-button,
                                        QSpinBox::up-button {
                                            border-radius: 12px;
                                        }
                                        
                                        QSpinBox::down-button:hover,
                                        QSpinBox::up-button:hover {
                                            background-color: #788787;
                                        }
                                        
                                        QSpinBox::down-button:pressed,
                                        QSpinBox::up-button:pressed {
                                            background-color: #c64236;
                                        }
                                        
                                        QSpinBox::up-arrow, QSpinBox::down-arrow {
                                            subcontrol-origin: content;
                                            width: 12px;
                                            height: 12px;
                                        }
                                        
                                        QSpinBox::up-arrow{
                                            image: url(:/images/plus.png);
                                        }
                                        
                                        QSpinBox::down-arrow{
                                            image: url(:/images/minus.png);
                                        }
        """)

        self.spinbox3 = QSpinBox()
        self.spinbox3.setAlignment(Qt.AlignHCenter)
        self.spinbox3.setGeometry(135, 80, 30, 64)
        self.spinbox3.setStyleSheet("""
                                        QSpinBox {
                                            background: #2c2c2c;
                                            margin: 5px 0;
                                            padding: 5px 0;
                                        }
                                        
                                        QSpinBox::down-button,
                                        QSpinBox::up-button {
                                            width: 200px;
                                            height: 10px;
                                            background-color: #444;
                                            subcontrol-origin: border;
                                        }
                                        
                                        QSpinBox::up-button {
                                            subcontrol-position: top center;
                                        }
                                        
                                        QSpinBox::down-button {
                                            subcontrol-position: bottom center;
                                        }
                                        
                                        QSpinBox::up-arrow,
                                        QSpinBox::down-arrow{
                                            width: 12px;
                                            height: 12px;
                                            bottom: 3px;
                                            background-color: transparent;
                                            image: url(":/icons/QSpinBox/arrow-drop-up-line.png");
                                        }
                                        
                                        QSpinBox::down-arrow{
                                            top: 3px;
                                            image: url(":/icons/QSpinBox/arrow-drop-down-line.png");
                                        }
                                        
                                        QSpinBox::up-arrow:hover{
                                            image: url(":/icons/QSpinBox/arrow-drop-up-line_hover.png");
                                        }
                                        
                                        QSpinBox::down-arrow:hover{
                                            image: url(":/icons/QSpinBox/arrow-drop-down-line_hover.png");
                                        }
                                        
                                        QSpinBox::up-arrow:pressed{
                                            image: url(":/icons/QSpinBox/arrow-drop-up-line.png");
                                        }
                                        
                                        QSpinBox::down-arrow:pressed{
                                            image: url(":/icons/QSpinBox/arrow-drop-down-line.png");
                                        }
        """)

        self.setLayout(layout)
        layout.addWidget(self.spinbox1, alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox2, alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox3, alignment=Qt.AlignCenter)
        # layout.addWidget(self.spinbox4, alignment=Qt.AlignCenter)
        # layout.addWidget(self.spinbox5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
