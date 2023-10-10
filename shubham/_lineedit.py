import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PySide2.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Styled LineEdits")
        self.resize(400, 500)

        layout = QVBoxLayout()

        # Create three QLineEdit widgets
        line_edit1 = QLineEdit(self)
        line_edit2 = QLineEdit(self)
        line_edit3 = QLineEdit(self)
        line_edit3.setPlaceholderText("Please enter your name")

        layout.addWidget(line_edit1)
        layout.addWidget(line_edit2)
        layout.addWidget(line_edit3)

        # Apply stylesheets to the QLineEdit widgets
        line_edit1.setStyleSheet('''
            QLineEdit {
                background-color: lightgray;
                border: 2px solid darkgray;
                border-radius: 5px;
                padding: 5px;
            }
            
            QLineEdit:hover {
                background-color: lightblue;
            }
            
            QLineEdit:focus {
                border: 2px solid blue;
            }
        ''')

        line_edit2.setStyleSheet('''
QLineEdit {
    border: 1px solid #474747;
    border-radius: 10px;
    padding: 5px;
}

QLineEdit:hover, QLineEdit:focus {
    border: 5px solid #00aaaa;
}
        ''')

        line_edit3.setStyleSheet('''
            QLineEdit {
                background-color: white;
                border: 2px solid darkgray;
                border-radius: 5px;
                padding: 5px;
            }
            
            QLineEdit::placeholder {
                color: blue;
                font-style: italic;
            }
            QLineEdit::text {
                color: blue;
            }
        ''')

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
