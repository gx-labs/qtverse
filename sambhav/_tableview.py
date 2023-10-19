import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TableWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Table Styles")
        self.setFixedSize(QSize(500, 500))

        self.label_combo = QLabel("Table Widgets")
        font = self.label_combo.font()
        font.setPointSize(14)
        self.label_combo.setFont(font)

        self.table1 = QTableView()
        self.table1.setFixedSize(400, 200)
        self.model = QStandardItemModel()
        self.model.setColumnCount(4)
        self.model.setRowCount(4)

        self.model.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4"])

        self.table1.setModel(self.model)
        self.table1.setStyleSheet('''
                                     QTableView{
                                        selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,
                                        stop: 0 #FBAED2, stop: 1 pink);
                                        selection-color: red;
                                        font: bold italic;
                                        color: green;
                                        border: 2px solid grey;
                                        background: yellow;
                                        gridline-color: red;
                                     }
                                     QTableView QTableCornerButton::section {
                                        background: red;
                                        border: 2px outset red;
                                     }
                                     QTableView:item:hover{
                                        background-color: #d3d3d3;
                                        border: 2px solid blue;
                                        color: violet;
                                     }
                                     QHeaderView:section{
                                        font-weight: bold;
                                        color: Orange;
                                        background-color: #d3d3d3;
                                        border-bottom-width: 2px solid #686868;
                                     } 
                                     QHeaderView:section:pressed{
                                        color: black;
                                        background-color: green;
                                     }                            
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_combo, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.table1, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = TableWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()