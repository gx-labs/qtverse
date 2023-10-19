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
                                                border: white;
                                                background: black;
                                                height: 15px;
                                                margin: 0px 21px 0 21px;
                                                border-radius: 1px;
                                            }
                                            QScrollBar::handle:horizontal {
                                                background: white;
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
                                                background: black;
                                            }
                                            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                                            {
                                                background: black;
                                            }
        """)

        self.H_scrollbar2 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar2.setMinimumSize(300,10)
        self.H_scrollbar2.setStyleSheet("""
QScrollBar:horizontal {
    border: 2px solid green;
    background: white;
    height: 20px;
    margin: 0px 40px 0 0px;
}

QScrollBar::handle:horizontal {
    background: gray;
    min-width: 20px;
}

QScrollBar::add-line:horizontal {
    background: white;
    width: 16px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    border: 2px solid black;
}

QScrollBar::sub-line:horizontal {
    background: grey;
    width: 16px;
    subcontrol-position: top right;
    subcontrol-origin: margin;
    border: 2px solid black;
    position: absolute;
    right: 20px;
}

QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    width: 3px;
    height: 3px;
    background: black;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

        """)

        self.H_scrollbar3 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar3.setMinimumSize(300,10)
        self.H_scrollbar3.setStyleSheet("""
QScrollBar:horizontal {
    border: none;
    background: #32CC99;
    height: 20px;
    margin: 0px 20px 0 20px;
}
QScrollBar::handle:horizontal {
    background: white;
    min-width: 20px;
}
QScrollBar::add-line:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    width: 20px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    width: 20px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
        """)

        self.H_scrollbar4 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar4.setMinimumSize(300,10)
        self.H_scrollbar4.setStyleSheet("""
                                            QScrollBar:horizontal {
                                                border: none;
                                                background: #F5F5F5;
                                                height: 12px;
                                                margin: 0px 20px 0 20px;
                                                border-radius: 10px;
                                            }
                                            QScrollBar::handle:horizontal {
                                                background: red;
                                                min-width: 30px;
                                                border-radius: 30px;
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

        self.H_scrollbar5 = QScrollBar(Qt.Horizontal)
        self.H_scrollbar5.setMinimumSize(300,10)
        self.H_scrollbar5.setStyleSheet("""

        """)

        self.setLayout(layout)
        layout.addWidget(self.H_scrollbar1 )
        layout.addWidget(self.H_scrollbar2)
        layout.addWidget(self.H_scrollbar3)


def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()