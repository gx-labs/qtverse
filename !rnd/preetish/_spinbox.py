import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

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
        self.spinbox3.setAlignment(Qt.AlignCenter)
        self.spinbox3.setGeometry(0, 0, 200, 200)
        self.spinbox3.setStyleSheet("""
                                        QSpinBox
                                        {
                                            border: none;

                                            padding-right: 0px;
                                            padding-left: 0px;
                                            padding-top: 20px;
                                            padding-bottom: 20px;

                                            background-image: url(:/Images/CustomSpinBox/SpinBoxBody.png);
                                            background-color: rgba(0, 0, 0, 0);
                                            background-repeat: no-repeat;
                                            background-position: center;
                                            background-clip: content;

                                        }

                                        QSpinBox::up-button
                                        {
                                            min-width: 40px;
                                            min-height: 40px;

                                            top: 25px;

                                            background-image: url(:/Images/CustomSpinBox/SpinBoxPlus.png);
                                            background-repeat: no-repeat;
                                            background-position: top center;

                                            subcontrol-position: top center; 
                                            subcontrol-origin: padding;
                                        }

                                        QSpinBox::down-button
                                        {
                                            min-width: 40px;
                                            min-height: 40px;

                                            bottom: 25px;

                                            background-image: url(:/Images/CustomSpinBox/SpinBoxMinus.png);
                                            background-repeat: no-repeat;
                                            background-position: bottom center;

                                            subcontrol-position: bottom  center;
                                            subcontrol-origin: padding;
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
