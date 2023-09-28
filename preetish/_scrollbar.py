import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle('Scroll Bar')
        self.setFixedSize(800,800)

        self.H_scrollbar1 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar1.setMinimumSize(300,10)
        self.H_scrollbar1.setStyleSheet("""
                                            QScrollBar:horizontal {
                                                border: none;
                                                background: rgb(52, 59, 72);
                                                height: 8px;
                                                margin: 0px 21px 0 21px;
                                                border-radius: 0px;
                                            }
                                            QScrollBar::handle:horizontal {
                                                background: rgb(189, 147, 249);
                                                min-width: 25px;
                                                border-radius: 4px
                                            }
                                            QScrollBar::add-line:horizontal {
                                                border: none;
                                                background: rgb(55, 63, 77);
                                                width: 20px;
                                                border-top-right-radius: 4px;
                                                border-bottom-right-radius: 4px;
                                                subcontrol-position: right;
                                                subcontrol-origin: margin;
                                            }
                                            QScrollBar::sub-line:horizontal {
                                                border: none;
                                                background: rgb(55, 63, 77);
                                                width: 20px;
                                                border-top-left-radius: 4px;
                                                border-bottom-left-radius: 4px;
                                                subcontrol-position: left;
                                                subcontrol-origin: margin;
                                            }
                                            QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
                                            {
                                                background: none;
                                            }
                                            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                                            {
                                                background: none;
                                            }
        """)

        self.H_scrollbar2 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar2.setMinimumSize(300,10)
        self.H_scrollbar2.setStyleSheet("""
                                            QScrollBar:horizontal {
                                                border: none;
                                                background: #F5F5F5;
                                                height: 12px;
                                                margin: 0px 16px 0 16px;
                                                border-radius: 10px;
                                            }
                                            QScrollBar::handle:horizontal {
                                                background: #555;
                                                min-width: 20px;
                                                border-radius: 10px;
                                            }
                                            QScrollBar::add-line:horizontal {
                                                border: none;
                                                background: none;
                                            }
                                            QScrollBar::sub-line:horizontal {
                                                border: none;
                                                background: none;
                                            }

        """)

        self.H_scrollbar3 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar3.setMinimumSize(300,10)
        self.H_scrollbar3.setStyleSheet("""
                                            QScrollBar:horizontal {
                                                border: none;
                                                background: rgb(45, 45, 68);
                                                height: 14px; 
                                                margin: 0 15px 0 15px;
                                                border-radius: 0px;
                                            }

                                            QScrollBar::handle:horizontal {
                                                background-color: rgb(80, 80, 122);
                                                min-width: 30px;
                                                border-radius: 7px;
                                            }
                                            QScrollBar::handle:horizontal:hover {
                                                background-color: rgb(255, 0, 127);
                                            }
                                            QScrollBar::handle:horizontal:pressed {
                                                background-color: rgb(185, 0, 92);
                                            }

                                            QScrollBar::sub-line:horizontal {
                                                border: none;
                                                background-color: rgb(59, 59, 90);
                                                width: 15px; 
                                                border-top-left-radius: 7px;
                                                border-bottom-left-radius: 7px; 
                                                subcontrol-position: left;
                                                subcontrol-origin: margin; 
                                            }
                                            QScrollBar::sub-line:horizontal:hover {
                                                background-color: rgb(255, 0, 127);
                                            }
                                            QScrollBar::sub-line:horizontal:pressed {
                                                background-color: rgb(185, 0, 92);
                                            }

                                            QScrollBar::add-line:horizontal {
                                                border: none;
                                                background-color: rgb(59, 59, 90);
                                                width: 15px; 
                                                border-top-right-radius: 7px;
                                                border-bottom-right-radius: 7px; 
                                                subcontrol-position: right;
                                                subcontrol-origin: margin; 
                                            }
                                            QScrollBar::add-line:horizontal:hover {
                                                background-color: rgb(255, 0, 127);
                                            }
                                            QScrollBar::add-line:horizontal:pressed {
                                                background-color: rgb(185, 0, 92);
                                            }

                                            QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
                                                background: none;
                                            }
                                            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                                                background: none;
                                            }
        """)

        self.H_scrollbar4 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar4.setMinimumSize(300,10)
        self.H_scrollbar4.setStyleSheet("""
        """)

        self.H_scrollbar5 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar5.setMinimumSize(300,10)
        self.H_scrollbar5.setStyleSheet("""

        """)

        self.setLayout(layout)
        layout.addWidget(self.H_scrollbar1, alignment=Qt.AlignCenter)
        layout.addWidget(self.H_scrollbar2, alignment=Qt.AlignCenter)
        layout.addWidget(self.H_scrollbar3, alignment=Qt.AlignCenter)
        layout.addWidget(self.H_scrollbar4, alignment=Qt.AlignCenter)
        layout.addWidget(self.H_scrollbar5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

