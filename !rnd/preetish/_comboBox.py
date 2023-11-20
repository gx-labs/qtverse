import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox")
        self.setFixedSize(800,800)
        layout = QVBoxLayout()

        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("Option1")
        self.comboBox1.addItem("Option2")
        self.comboBox1.addItem("Option3")
        self.comboBox1.setStyleSheet("""
                                        QComboBox{
                                        border: none;
                                        background-color:rgb(87, 96, 134);
                                        color: rgb(255, 255, 255);
                                        font-weight: bold;
                                        padding: 5px 

                                        }

                                        QComboBox::drop-down{
                                            border: none;
                                            background-color: rgb(87, 96, 134);
                                            color: rgb(255, 255, 255);
                                            font-weight: bold;
                                            padding: 0px;
                                        }

                                        QComboBox::down-arrow{
                                            background-image: url(/images/down-arrow.png)
                                            padding-right: 5px;
                                        }

                                        QListView{
                                            border: none;
                                            color: rgb(87, 96, 134);
                                            background-color: rgb(255, 255, 255);
                                            font-weight: bold;
                                            selection-background-color: rgb(47, 175, 178);
                                            show-decoration-selected: 1;
                                            margin-left: -10px;
                                            padding-left: 5px;
                                        }

                                        QListView::item:hover{

                                            background-color: rgb(47, 175, 178);
                                            border: none;
                                        }
        """)

        self.comboBox2 = QComboBox()
        self.comboBox2.addItem("Option1")
        self.comboBox2.addItem("Option2")
        self.comboBox2.addItem("Option3")
        self.comboBox2.setStyleSheet("""
                                        QComboBox {
                                            background-color: #ffffff;
                                            border: 1px solid #dddddd;
                                            padding: 5px;
                                            font-family: "Roboto", sans-serif;
                                            color: #555555;
                                        }
                                        QComboBox::drop-down {
                                            background-color: #9dc852;
                                            width: 20px;
                                        }
                                        QComboBox::down-arrow {
                                            image: url(/preetish/images/down-arrow.png); 
                                        }
                                        QComboBox::down-arrow:hover {
                                            background-color: #8db842;
                                        }
                                        QComboBox QAbstractItemView {
                                            background-color: #ebebeb;
                                            border: 1px solid #dddddd;
                                            selection-background-color: rgba(0, 0, 0, 0.1);
                                        }

        """)

        self.comboBox3 = QComboBox()
        self.comboBox3.addItem("Option1")
        self.comboBox3.addItem("Option2")
        self.comboBox3.addItem("Option3")
        self.comboBox3.setStyleSheet("""
                                        QComboBox{
                                            color: #F5F3F4;
                                            font-weight: bold;
                                            border: 2px solid #E5383B;
                                            border-radius: 15px;
                                            background-color: #BA181B;
                                            padding: 8px;
                                            padding-left: 20px;
                                            padding-right: 20px;
                                        }

                                        QComboBox::drop-down {
                                            border: 10px;
                                            width: 0px;
                                        }

                                        QComboBox QAbstractItemView {
                                            border: 2px solid #E5383B;
                                            selection-background-color: #A4161A;
                                            color: #F5F3F4;
                                            background-color: #BA181B;
                                            border-radius: 2px;
                                        }
        """)
        self.comboBox4 = QComboBox()
        self.comboBox5 = QComboBox()



        self.setLayout(layout)
        layout.addWidget(self.comboBox1, alignment=Qt.AlignCenter)
        layout.addWidget(self.comboBox2, alignment=Qt.AlignCenter)
        layout.addWidget(self.comboBox3, alignment=Qt.AlignCenter)
        layout.addWidget(self.comboBox4, alignment=Qt.AlignCenter)
        layout.addWidget(self.comboBox5, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
