import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class LineeditWidget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Line Edit Styles")
        self.setFixedSize(QSize(500, 500))

        self.label_combo = QLabel("Line Widgets")
        font = self.label_combo.font()
        font.setPointSize(14)
        self.label_combo.setFont(font)

        self.lineedit1 = QLineEdit()
        self.lineedit1.setStyleSheet('''
                                     QLineEdit{
                                        border: 2px solid brown;
                                        padding: 5px;
                                        min-width: 10em;
                                        color: gray;
                                     }
                                     
        ''')

        self.lineedit2 = QLineEdit()
        self.lineedit2.setStyleSheet('''
                                     QLineEdit{
                                        border: 2px solid blue;
                                        border-radius: 5px;
                                        min-width: 10em;
                                        font-weight: bold;
                                        font-style: italic;
                                        color: red;
                                        font-size: 12px;
                                        background: #FFFCC9;
                                        selection-background-color: orange;
                                        selection-color: blue;
                                     }
                                     
        ''')

        self.lineedit3 = QLineEdit()
        self.lineedit3.setEchoMode(QLineEdit.Password)
        self.lineedit3.setStyleSheet('''
                                     QLineEdit{
                                        background-color: pink; 
                                        min-width: 10em;
                                        border: 2px solid #FFFCC9;
                                        border-radius: 5px;
                                        padding: 2px 5px;
                                        color: green;
                                        selection-color: red;
                                        selection-background-color: yellow;
                                    }
                                     
        ''')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_combo, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.lineedit1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.lineedit2, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.lineedit3, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    widget = LineeditWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()