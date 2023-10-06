import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class ComboboxWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Combobox Styles")
        self.setFixedSize(QSize(500, 500))

        self.label_combo = QLabel("Combo Widgets")
        font = self.label_combo.font()
        font.setPointSize(14)
        self.label_combo.setFont(font)

        self.combobox1 = QComboBox()
        self.combobox1.addItems(["File 1", "File 2", "File 3"])
        self.combobox1.setStyleSheet('''
                                     QComboBox{
                                        border: 1px solid gray;
                                        border-radius: 3px;
                                        padding: 1px 18px 1px 3px;
                                        min-width: 10em;
                                        font-weight: bold;
                                        font-size: 14px; 
                                     }
                                     QComboBox:!editable, QComboBox::drop-down:editable{
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
                                     }
                                     QListView{
                                            border: none;
                                            color: rgb(87, 96, 134);
                                            background-color: pink;
                                            font-weight: bold;
                                            selection-background-color: rgb(47, 175, 178);
                                            show-decoration-selected: 1;
                                            margin-left: -10px;
                                            padding-left: 5px;
                                        }
                                    
                                     

        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_combo, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.combobox1, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = ComboboxWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()