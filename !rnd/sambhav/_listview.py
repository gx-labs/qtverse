import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class ListviewWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Listview Styles")
        self.setFixedSize(QSize(800, 800))

        self.label_combo = QLabel("Listview Widgets")
        font = self.label_combo.font()
        font.setPointSize(14)
        self.label_combo.setFont(font)

        self.listwidget1 = QListWidget()
        self.listwidget1.addItems(["File 1","File 2", "File 3", "File 4"])
        self.listwidget1.setStyleSheet('''
                                     QListView{
                                        border: 2px dotted brown;
                                        color: green;
                                        alternate-background-color: blue;
                                        background-color: pink;
                                        font-weight: bold;
                                        selection-background-color: yellow;
                                        show-decoration-selected: 1;
                                        padding-left: 5px;
                                     }
                                     QListView::item:selected:active {
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 orange, stop: 1 yellow);
                                        color: red;
                                     }    
                                     QListView:item:hover {
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #FAFBFE, stop: 1 orange);
                                        color: red;
                                     }                                  
        ''')

        self.combowidget1 = QComboBox()
        self.combowidget1.addItems(["File 1","File 2", "File 3", "File 4"])
        self.combowidget1.setStyleSheet('''
                                        QComboBox{
                                            min-width: 10em;
                                            border-radius: 5px;
                                            font-weight: bold;
                                        }
                                        QListView{
                                            border: 2px solid #ADD8E6;
                                            color: #e39752;
                                            font-weight: bold;
                                            background-color: #fffee0;
                                            selection-background-color: #FFCBC4;
                                            selection-color: blue;
                                        }
                                        
                                                                       
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_combo, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.listwidget1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.combowidget1, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = ListviewWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()