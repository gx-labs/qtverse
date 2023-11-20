import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class ScrollWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Scrollbar Styles")
        self.setFixedSize(QSize(500, 500))

        self.scrlbr1 = QScrollBar(Qt.Horizontal)
        self.scrlbr1.setMinimumSize(200,10)
        self.scrlbr1.setStyleSheet('''
                                     QScrollBar:horizontal{
                                        border: 2px solid black;
                                        background: #4780a5;
                                        height: 18px;
                                        margin: 0 20px 0 20px;
                                     }
                                     QScrollBar::handle:horizontal {
                                        background: #32CC99;
                                        min-width: 20px;
                                        border-radius: 20px;
                                     }
                                     QScrollBar::add-line:horizontal {
                                        background: orange;
                                        width: 20px;
                                        border-top-right-radius: 4px;
                                        border-bottom-right-radius: 4px;
                                        subcontrol-position: right;
                                        subcontrol-origin: margin;
                                     }
                                     QScrollBar::sub-line:horizontal {
                                        border: none;
                                        background: orange;
                                        width: 20px;
                                        border-top-left-radius: 4px;
                                        border-bottom-left-radius: 4px;
                                        subcontrol-position: left;
                                        subcontrol-origin: margin;
                                     }
                                     QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{
                                        background: pink;
                                     }
        ''')

        self.scrlbr2 = QScrollBar(Qt.Horizontal)
        self.scrlbr2.setMinimumSize(200,10)
        self.scrlbr2.setStyleSheet('''
                                     QScrollBar:horizontal{
                                        border: 2px dotted black;
                                        background: red;
                                        height: 14px; 
                                        margin: 0 12px 0 12px;
                                        border-radius: 4px;
                                     }
                                     QScrollBar::handle:horizontal {
                                        background-color: yellow;
                                        min-width: 30px;
                                        border-radius: 7px;
                                        border: 3px solid green;
                                     }
                                     QScrollBar::handle:horizontal:hover {
                                        background-color: pink;
                                        border: 3px solid blue;
                                     }
                                     QScrollBar::handle:horizontal:pressed {
                                        background-color: brown;
                                     }
                                     QScrollBar::sub-line:horizontal {
                                        border: none;
                                        background-color: orange;
                                        width: 15px; 
                                        border-top-left-radius: 7px;
                                        border-bottom-left-radius: 7px; 
                                        subcontrol-position: left;
                                        subcontrol-origin: margin; 
                                     }
                                     QScrollBar::sub-line:horizontal:hover {
                                        background-color: grey;
                                     }
                                     QScrollBar::sub-line:horizontal:pressed {
                                        background-color: maroon;
                                     }
                                     QScrollBar::add-line:horizontal {
                                        border: none;
                                        background-color: orange;
                                        width: 15px; 
                                        border-top-right-radius: 7px;
                                        border-bottom-right-radius: 7px; 
                                        subcontrol-position: right;
                                        subcontrol-origin: margin; 
                                     }
                                     QScrollBar::add-line:horizontal:hover {
                                        background-color: grey;
                                        border: 2px solid blue;
                                     }
                                     QScrollBar::add-line:horizontal:pressed {
                                        background-color: maroon;
                                     }
        ''')

        self.scrlbr3 = QScrollBar(Qt.Vertical)
        self.scrlbr3.setMinimumSize(10,200)
        self.scrlbr3.setStyleSheet('''
                                     QScrollBar:vertical{
                                        border: 2px dotted black;
                                        background: red;
                                        width: 8px;
                                        height: 18px; 
                                        margin: 5px 0 5px 0;
                                        border-radius: 4px;
                                     }
                                     QScrollBar::handle:vertical {
                                        background-color: yellow;
                                        min-height: 20px;
                                        border-radius: 7px;
                                        border: 3px solid green;
                                     }
                                     QScrollBar::handle:vertical:hover {
                                        background-color: pink;
                                        border: 3px solid blue;
                                     }
                                     QScrollBar::handle:vertical:pressed {
                                        background-color: brown;
                                     }
                                     QScrollBar::sub-line:vertical {
                                        border: none;
                                        background-color: orange;
                                        height: 20px; 
                                        border-top-left-radius: 7px;
                                        border-top-right-radius: 7px; 
                                        subcontrol-position: top;
                                        subcontrol-origin: margin; 
                                     }
                                     QScrollBar::sub-line:vertical:hover {
                                        background-color: grey;
                                     }
                                     QScrollBar::sub-line:vertical:pressed {
                                        background-color: maroon;
                                     }
                                     QScrollBar::add-line:vertical {
                                        border: 2px solid grey;
                                        background-color: orange;
                                        height: 20px; 
                                        border-bottom-left-radius: 7px;
                                        border-bottom-right-radius: 7px; 
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin; 
                                     }
                                     QScrollBar::add-line:vertical:hover {
                                        background-color: grey;
                                        border: 2px solid blue;
                                     }
                                     QScrollBar::add-line:vertical:pressed {
                                        background-color: maroon;
                                     }
        ''')    


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scrlbr1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.scrlbr2, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.scrlbr3, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = ScrollWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
