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
        push = QPushButton("End For All")
        button = QPushButton()
        button.setIcon(QIcon("D:\Pyside\Icons\X.png"))
        

#        button.setProperty('imageIndex', 0)
#        button.setStyleSheet('QPushButton {'
#                                  '   background-color: #3498db;'
#                                  '   border: none;'
#                                  '   padding: 10px;'
#                                  '   background-image: url(' + os.path.join('Icons', 'X.png') + ');'
#                                  '   background-repeat: no-repeat;'
#                                  '   background-position: center;'
#                                 '}'
#                                  'QPushButton:pressed {'
#                                  '   background-color: #e74c3c;'
#                                  '}'
#                                  'QPushButton[imageIndex="0"] {'
#                                  '   background-image: url(' + os.path.join('Icons', 'X.png') + ');'
#                                  '}'
#                                 'QPushButton[imageIndex="1"] {'
#                                 '   background-image: url(' + os.path.join('Icons', 'x1.png') + ');'
#                                  '}')

#        vbox.addWidget(button)

        push.setStyleSheet( """QPushButton {
    background-color: red;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: rgb(224, 0, 0);
    border-style: inset;
}""")
        checkbox = QCheckBox("CSS")
        checkbox.setStyleSheet('QCheckBox {'
                               '   padding: 10px;'
                               '   border: none;'

                               '}'
                               'QCheckBox:hover {'
                               '   background-color: blue;'
                               '    color : white '
                               '}'
                               'QCheckBox:checked {'
                               '   background-color: #e74c3c;'
                               '}')
        vbox.addWidget(push)
        vbox.addWidget(button)

        vbox.addWidget(checkbox)
       
        self.setLayout(vbox)

        self.setWindowTitle('Widget')
        self.setGeometry(100, 100, 300, 150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RadioButtonsApp()
    ex.show()
    sys.exit(app.exec_())

