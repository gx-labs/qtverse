import sys,os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class ComboBoxApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create five QComboBox widgets
        combo1 = QComboBox()
        combo2 = QComboBox()
        combo3 = QComboBox()
        combo4 = QComboBox()
        combo5 = QComboBox()
        
        combo1.addItem("Item 1")
        combo1.addItem("Item 2")
        combo1.addItem("Item 3")

        combo2.addItem("Item 1")
        combo2.addItem("Item 2")
        combo2.addItem("Item 3")

        combo3.addItem("Item 1")
        combo3.addItem("Item 2")
        combo3.addItem("Item 3")

        combo4.addItem("Item 1")
        combo4.addItem("Item 2")
        combo4.addItem("Item 3")

        # Apply different stylesheets for each QComboBox
        combo1.setStyleSheet(
            """
            QComboBox {
                background-color: Grey;
                border: 2px solid Black;
                padding: 10px;
                border-radius: 10px;
                font-weight: bold;


            }
            
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: right top;
                width: 20px;
                background-color: Black;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;

            }

            QListView{
                border: 2px solid Black;
                background-color: Grey;
                font-weight: bold;
                selection-background-color: Light blue;
                show-decoration-selected: 1;
                margin-left: -10px;
                padding-left: 5px;
                                        }

            QComboBox::down-arrow {
                width: 40px;
                height: 14px;
            }
            """
        )

        combo2.setStyleSheet(
            """
            QComboBox {
            background-color: pink;
            border: 4px solid Red;
            border-radius: 10px;
            padding: 5px;
            font-family: "Roboto", sans-serif;
            color: Red;
            font-weight: bold;
            padding-left: 100px; 
            }
            QComboBox::item {
                padding-left: 30px; /* Adjust the padding as needed */
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: right top;
                width: 20px;
                background-color: white;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
            QComboBox::down-arrow:hover {
                background-color: red;
                                        }
            QComboBox::down-arrow {
                width: 15px;
                height: 15px;
            }
            QComboBox QAbstractItemView {
                background-color: pink;
                border: 1px solid #dddddd;
                selection-background-color: red;

                                        }
            """
        )

        combo3.setStyleSheet(
            """
            QComboBox {
                background-color: white;
                padding: 5px;
                border-radius: 15px;
                min-width: 100px;
                color: blue;
                font-weight: bold;

            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: right top;
                width: 20px;

                background-color: #3498DB;
                border: 1px solid #2980B9;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 10px;
            }

            QComboBox QAbstractItemView {
                background-color: #ebebeb;
                border: 1px solid #dddddd;
                selection-background-color: rgba(0, 0, 0, 0.1);
                                        }

            """
        )

        combo4.setStyleSheet(
            """
            QComboBox {
                background-color: #ECF0F1;
                border: 1px solid #BDC3C7;
                padding: 5px;
                border-radius: 5px;
                min-width: 100px;
            }

            QComboBox::drop-down {
                                            border: 5px solid black;
                                            width: 5px;

                                        }

            QComboBox::down-arrow {
                width: 14px;
                height: 20px;
            }
            QComboBox::down-arrow:hover {
                background-color: Black;
                                        }
            """
        )

        combo5.setStyleSheet(
            """
            QComboBox {
                background-color: #ECF0F1;
                border: 1px solid #BDC3C7;
                padding: 2px;
                border-radius: 5px;
                min-width: 100px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: right top;
                width: 20px;

                background-color: #8E44AD;
                border: 1px solid #6C3483;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }

            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 14px;
                height: 14px;
            }
            """
        )

        layout.addWidget(combo1)
        layout.addWidget(combo2)
        layout.addWidget(combo3)
        layout.addWidget(combo4)

        self.setLayout(layout)

        self.setWindowTitle('ComboBoxes')
        self.resize(300,400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComboBoxApp()
    ex.show()
    sys.exit(app.exec_())
