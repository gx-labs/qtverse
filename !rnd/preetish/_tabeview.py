import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TableWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Table View")
        self.setFixedSize(QSize(800, 800))

        self.model = QStandardItemModel()
        self.model.setColumnCount(4)
        self.model.setRowCount(4)

        self.model.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4"])

        self.tableView1 = QTableView()
        self.tableView1.setFixedSize(400, 160)
        self.tableView1.setModel(self.model)
        self.tableView1.setStyleSheet("""
                                        QTableWidget {
                                            background-color: #f5f5f5;
                                            border: 1px solid #ccc;
                                            selection-background-color: #4a90e2;
                                            selection-color: white;
                                        }

                                        QTableWidget::item {
                                            padding: 6px;
                                            border: none;
                                        }

                                        QTableWidget::item:selected {
                                            background-color: #4a90e2;
                                            color: white;
                                        }

                                        QHeaderView::section {
                                            background-color: #4a90e2;
                                            color: white;
                                            padding: 8px;
                                            border: none;
                                        }

                                        QHeaderView::section:checked {
                                            background-color: #4a90e2;
                                            color: white;
                                        }

                                        QHeaderView::section:horizontal {
                                            border-bottom: 1px solid #ccc;
                                        }

                                        QHeaderView::section:vertical {
                                            border-right: 1px solid #ccc;
                                        }                       
        """)

        self.tableView2 = QTableView()
        self.tableView2.setFixedSize(400, 160)
        self.tableView2.setModel(self.model)
        self.tableView2.setStyleSheet("""
                                        QTableView
                                        {
                                            background-color: #242526;
                                            border: 1px solid #32414B;
                                            color: #f0f0f0;
                                            gridline-color: #8faaff;
                                            outline : 0;
                                        }

                                        QTableView::disabled
                                        {
                                            background-color: #242526;
                                            border: 1px solid #32414B;
                                            color: #656565;
                                            gridline-color: #656565;
                                            outline : 0;
                                        }

                                        QTableView::item:hover 
                                        {
                                            background-color: #26264f;
                                            color: #f0f0f0;
                                        }

                                        QTableView::item:selected 
                                        {
                                            background-color: #1a1b1c;
                                            border: 2px solid #4969ff;
                                            color: #F0F0F0;
                                        }

                                        QTableView::item:selected:disabled
                                        {
                                            background-color: #1a1b1c;
                                            border: 2px solid #525251;
                                            color: #656565;
                                        }

                                        QTableCornerButton::section
                                        {
                                            background-color: #505050;
                                            color: #fff;
                                        }

                                        QHeaderView::section
                                        {
                                            background-color: #525251;
                                            color: #fff;
                                            text-align: left;
                                            padding: 4px;    
                                        }

                                        QHeaderView::section:disabled
                                        {
                                            background-color: #525251;
                                            color: #656565;
                                        }

                                        QHeaderView::section:checked
                                        {
                                            color: #fff;
                                            background-color: #4969ff;
                                        }

                                        QHeaderView::section:checked:disabled
                                        {
                                            color: #656565;
                                            background-color: #525251;
                                        }

                                        QHeaderView::section::vertical::first,
                                        QHeaderView::section::vertical::only-one
                                        {
                                            border-top: 1px solid #353635;
                                        }

                                        QHeaderView::section::vertical
                                        {
                                            border-top: 1px solid #353635;
                                        }

                                        QHeaderView::section::horizontal::first,
                                        QHeaderView::section::horizontal::only-one
                                        {
                                            border-left: 1px solid #353635;
                                        }

                                        QHeaderView::section::horizontal
                                        {
                                            border-left: 1px solid #353635;
                                        }       
        """)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableView1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.tableView2, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = TableWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()