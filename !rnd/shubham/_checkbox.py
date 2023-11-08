import sys,os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class RadioButtonsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a QVBoxLayout as the main layout
        vbox = QVBoxLayout()

        # Create radio buttons with labels A, B, and C
        button = QPushButton()
        

        button.setProperty('imageIndex', 0)
        button.setStyleSheet('QPushButton {'
                                  '   background-color: #3498db;'
                                  '   border: none;'
                                  '   padding: 10px;'
                                  '   background-image: url(:/Icons/x1.png); '
                                  '   background-repeat: no-repeat;'
                                  '   background-position: center;'
                                 '}')
                                 # 'QPushButton:pressed {'
                                #  '   background-color: #e74c3c;'
                                #  '}'
                                 # 'QPushButton[imageIndex="0"] {'
                                 # '   background-image: url('Icons/X.png');'
                                #  '}'
                                 #'QPushButton[imageIndex="1"] {'
                                 #'   background-image: url('Icons/X1.png');'
                                #  '}')



        checkbox = QCheckBox("OPTION1")
        checkbox.setStyleSheet('QCheckBox {'
                               '   padding: 10px;'
                               '   border: none;'
                               # '   background-image: url('Icons/X.png'); '
                               '}'
                               'QCheckBox:hover {'
                               '   background-color: blue;'
                               '    color : white '
                               '}'
                               'QCheckBox:checked {'
                               '   background-color: #e74c3c;'
                               '}')
        
        checkbox1 = QCheckBox("OPTION2")
        checkbox1.setStyleSheet('''QCheckBox {
        font-size: 14px;
        color: Black;
        border : 3px solid blue;
    }
    QCheckBox::indicator {
        border : 5px solid blue;
        width: 10px;
        height: 10px;
    }
    QCheckBox::indicator:checked {
                                
        background-color: Blue;
        
    }
    QCheckBox::indicator:unchecked {
        background-color: white;
    }''')
        checkbox2 = QCheckBox("OPTION 3")
        checkbox2.setStyleSheet('''QCheckBox {
        font-size: 20px;
        color: Blue;
    }
    QCheckBox::indicator {
        border : 5px solid blue;
        border-radius: 10px;
        width: 10px;
        height: 10px;
    }
    QCheckBox::indicator:checked {
                                
        background-color: Blue;
    }
    QCheckBox::indicator:unchecked {
        background-color: white;
    }''')
        
        checkbox3 = QCheckBox("OPTION 4")
        checkbox3.setStyleSheet('''QCheckBox {
        font-size: 15px;
        color: Black;
    }
    QCheckBox::indicator {
        border : 5px solid Black;
        border-radius: 15px;
        width: 10px;
        height: 10px;
                                
    }
    QCheckBox::indicator:checked {
                                
        background-color: Black;
    }
    QCheckBox::indicator:unchecked {
        background-color: white;
    }''')
        
        checkbox4 = QCheckBox("OPTION 5")
        checkbox4.setStyleSheet('''QCheckBox {
        font-size: 20px;
        color: Blue;
    }
    QCheckBox::indicator {
        border : 8px solid Blue;
        border-style : groove;                        
        width: 20px;
        height: 20px;
                                
    }
    QCheckBox::indicator:checked {
                                
        background-color: Blue;
    }
    QCheckBox::indicator:unchecked {
        background-color: white;
    }''')
        
        checkbox5 = QCheckBox("OPTION 6")
        checkbox5.setStyleSheet('''QCheckBox {
        font-size: 20px;
        color: Blue;
        spacing: 20px;
    }
    QCheckBox::indicator {
        border : 5px solid blue;
        width: 30px;
        height: 30px;
    }
    QCheckBox::indicator:checked {
                                
        background-color: blue;
    }
    QCheckBox::indicator:checked:hover
                               {
                               background-color : red;
                               }
    QCheckBox::indicator:unchecked {
        background-color: white;
    }
    QCheckBox::indicator:unchecked:hover
                               {
                               background-color : yellow;
                               }                                '''
    )
        checkbox7 = QCheckBox("OPTION 7")
        checkbox7.setStyleSheet('''QCheckBox {
        font-size: 15px;
        color: Black;
    }
    QCheckBox::indicator {
        border : 2px solid Black;
        border-radius: 10px;
        border-style : dotted;
        width: 30px;
        height: 30px;}
    QCheckBox::indicator:checked {
                                background-color: Grey;
    
                                
    }''')
        checkbox6 = QCheckBox("OPTION 8")
        checkbox6.setTristate(True)
        checkbox6.setStyleSheet(    "QCheckBox::indicator {"
        "width: 30px;"
        "height: 30px;}"
            "QCheckBox::indicator:indeterminate"
                               "{"
                               "background-color : red;"
                               "}"
            "QCheckBox::indicator:indeterminate:hover"
"{"
"background-color : blue;"
"}"
)
        checkbox8 = QCheckBox("OPTION 9")
        checkbox8.setTristate(True)
        checkbox8.setStyleSheet(    "QCheckBox::indicator {"
        "width: 30px;"
        "height: 30px;}"
            "QCheckBox::indicator:indeterminate"
                               "{"
                               "background-color : red;"
                               "}"
            "QCheckBox::indicator:indeterminate:hover"
"{"
"background-color : blue;"
"}"
"QCheckBox::indicator:indeterminate:pressed"
"{"
"background-color : yellow;"
"}"
)

        checkbox4.setLayoutDirection(Qt.RightToLeft)
        
        vbox.addWidget(button)

        vbox.addWidget(checkbox)
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(checkbox3)
        vbox.addWidget(checkbox4)
        vbox.addWidget(checkbox5)
        vbox.addWidget(checkbox6)
        vbox.addWidget(checkbox7)
        vbox.addWidget(checkbox8)


        self.setLayout(vbox)

        self.setWindowTitle('Widget')
        self.setGeometry(100, 100, 300, 150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RadioButtonsApp()
    ex.show()
    sys.exit(app.exec_())

