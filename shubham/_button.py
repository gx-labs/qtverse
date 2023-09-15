import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton,QHBoxLayout,QPushButton

class RadioButtonsApp(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()
        # hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        button1 = QPushButton("Button")
        button1.setStyleSheet('''QPushButton {
                                        background-color: white;
                                        border: 2px solid #3498db;
                                        border-radius: 10px;
                                        color: #3498db;
                                        padding: 10px 20px;
                                        font-size: 16px;
                                    }
                                    
                                QPushButton:hover {
                                        background-color: #3498db;
                                        color: white;
                                        font-size: 20px;
                                    }''')

        button2 = QPushButton("Sign Up")
        button2.setStyleSheet('''QPushButton {
                                        background-color: white;
                                        border: 2px solid #3498db;
                                        border-radius: 20px;
                                        color: #3498db;
                                        padding: 10px 20px;
                                        font-size: 16px;
                                    }
                                    
                                QPushButton:hover {
                                        background-color: #3498db;
                                        color: white;
                                        font-size: 20px;
                                    }''')

        # Add radio buttons to the layout
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button4)
        vbox.addWidget(button5)
        vbox.addWidget(button6)
        vbox.addWidget(button7)

        # hbox.addLayout(vbox)
        mainlayout.addLayout(vbox)

        # Set the layout for the main window
        self.setLayout(mainlayout)

        self.setWindowTitle('Radio Buttons Example')
        self.setGeometry(100, 100, 300, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RadioButtonsApp()
    ex.show()
    sys.exit(app.exec_())
