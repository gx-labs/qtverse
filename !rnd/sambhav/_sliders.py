import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class SliderWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Slider Styles")
        self.setFixedSize(QSize(500, 500))

        self.label_combo = QLabel("Slider Widgets")
        font = self.label_combo.font()
        font.setPointSize(14)
        self.label_combo.setFont(font)

        self.slider1 = QSlider(Qt.Vertical)
        self.slider1.setStyleSheet('''
                                     QSlider{
                                        min-height: 10em;
                                        width: 18px;
                                        background-color: pink;
                                        border: 2px dotted grey;
                                        border-radius: 5px;
                                     }
                                      QSlider:handle{
                                        width: 20px;
                                        border: 2px solid black;
                                        height: 20px;
                                        border-radius: 5px;
                                        background-color: green;
                                      }
                                      QSlider:handle:hover{
                                        border: 2px solid blue;
                                        background-color: grey;
                                      }
                                      QSlider:handle:pressed{
                                        background-color: red;
                                      }    
                                     
        ''')
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setStyleSheet('''
                                     QSlider{
                                        min-width: 10em;
                                        height: 18px;
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FAFBFE, stop:1 #b6661d);
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                     }
                                     QSlider:groove:horizontal{
                                        background: lightgray;
                                        border: 1px solid #222222;
                                        height: 10px;
                                        border-radius: 5px;
                                     }
                                     QSlider:handle:horizontal{
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E74C3C, stop:1 #D35400);
                                        border: 1px solid blue;
                                        width: 20px;
                                        margin: -5px;
                                        border-radius: 10px;
                                     }
        ''')
        self.slider3 = QSlider(Qt.Vertical)
        self.slider3.setStyleSheet('''
                                     QSlider:groove:vertical{
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FAFBFE, stop:1 #b6661d);
                                        position: absolute;
                                        left: 4px; right: 4px;
                                     }
                                     QSlider:handle:vertical {
                                        height: 10px;
                                        background: green;
                                        margin: 0 -5px;
                                     }
                                     QSlider:handle:hover{
                                        border: 2px solid blue;
                                        background-color: grey;
                                     }
                                     QSlider:handle:pressed{
                                        background-color: red;
                                     }
                                     QSlider:add-page:vertical {
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 pink);
                                     }
                                         
        ''')
        self.slider4 = QSlider(Qt.Horizontal)
        self.slider4.setStyleSheet('''
                                    QSlider{
                                        min-width: 10em;
                                        height: 18px;
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FAFBFE, stop:1 #b6661d);
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                    }
                                    QSlider:groove:horizontal{
                                        border: 2px solid blue;
                                        height: 8px;
                                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
                                        margin: 2px;
                                    }
                                    QSlider:handle:horizontal{
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 blue, stop:1 orange);
                                        border: 2px solid green;
                                        width: 20px;
                                        margin: -5px 0; 
                                        border-radius: 3px;
                                    }
                                    QSlider:sub-page:horizontal {
                                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 pink);
                                    }
                                         
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_combo, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.slider1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.slider2, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.slider3, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.slider4, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = SliderWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()