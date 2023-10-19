import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TabWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tab Styles")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.tabwid1 = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabwid1.addTab(self.tab1, "Tab 1")
        self.tabwid1.addTab(self.tab2, "Tab 2")
        self.tabwid1.addTab(self.tab3, "Tab 3")

        self.tabwid2 = QTabWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.tabwid2.addTab(self.tab4, "Tab 1")
        self.tabwid2.addTab(self.tab5, "Tab 2")
        self.tabwid2.addTab(self.tab6, "Tab 3")

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.tabwid1)
        self.main_layout.addWidget(self.tabwid2)

        self.tabwid1.setStyleSheet("""
            QTabWidget:pane {
                border: 3px solid green;
                border-radius: 10px;
                border-style : groove;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 orange, stop: 1 yellow);                                           
            }
            QTabWidget:pane:hover {
                background: purple;
                color: grey;
            }
            QTabWidget:tab-bar {
                alignment: left;
            }
            QTabBar:tab {
                background: pink;
                border: 2px solid red;
                border-radius: 5px;
                padding: 6px;
                min-width: 100px;
                min-height: 30px;
                color: blue;
            }
            QTabBar:tab:!selected {
                margin-top: 4px; 
            }   
            QTabBar:tab:selected {
                background: green;
                color: white;
                margin-left: -4px;
                margin-right: -4px;
            }
            QTabBar:tab:hover {
                background: purple;
                color: grey;
                padding: 8px;
            }
            QTabBar::tab:first:selected {
                margin-left: 0; 
            }

            QTabBar::tab:last:selected {
                margin-right: 0; 
            }
        """)

        self.tabwid2.setStyleSheet("""
            QTabWidget::pane {
                border: 3px dotted black;
                border-radius: 10px;
                background-color: #FFE4C4;
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabBar::tab {
                background: #B5A642;
                border: 2px dotted blue;
                border-radius: 10px;
                padding: 10px;
                min-width: 120px;
                min-height: 40px;
                color: red;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: #61d8b1;
                color: grey;
            }
        """)
        

def main():
    app = QApplication(sys.argv)
    widget = TabWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()