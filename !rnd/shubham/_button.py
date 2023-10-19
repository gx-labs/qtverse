import sys
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton,QHBoxLayout,QPushButton

class RadioButtonsApp(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()
        # hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        button1 = QPushButton("Button")
        button2 = QPushButton("Sign Up")
        button3 = QPushButton("Enroll")
        button4 = QPushButton("Register")
        button5 = QPushButton("Click Me")
        button6 = QPushButton("Log out")
        button7 = QPushButton("ADD")
        button8 = QPushButton("DELETE")
        button9 = QPushButton("REMOVE")
        push = QPushButton("End For All")

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
        button3.setStyleSheet("""
                            QPushButton {
                                        background-color: black;
                                        border-radius: 20px;
                                        padding: 15px 10px;   
                                        color: white;
                                        font-size: 25px;
                              
                                           }
                            QPushButton:hover {

                                        color: white;
                                        font-size: 30px;
                                    }''')
        
    """)

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
        
        button4.setStyleSheet("""
                            QPushButton {
                                        background-color: #ecf0f1;
                                        border: 5px dotted #bdc3c7;
                                        color: #2c3e50;
                                        font-size: 26px;
                                        font-weight: bold;}
                                QPushButton:hover {
                                        background-color: Grey;
                                        color: white;
                                        font-size: 20px;
                                    }
                              
                                           }
    """)
        button5.setStyleSheet("""
                                QPushButton {
                                        background-color: #e67e22;
                                        border: 2px outset #d35400;
                                        color: white;
                                        font-size: 28px;
                                        font-family: "Arial";}
                                QPushButton:hover {
                                        font-size: 20px;
                                        color: black;
                                    }
                              
                                           }
    """)
        button6.setStyleSheet("""
                            QPushButton {border-left: 4px solid #3498db;                                        
                                        padding: 10px 10px;   
                                        color: blue;
                                        font-size: 25px;
                              
                                           }
    """)
        button7.setStyleSheet("""
                                QPushButton {
                                        background-color: #f1c40f;
                                        padding: 20px 10px;

                                        border: none;
                                        color: #34495e;
                                        font-size: 20px;
                                        }
                                QPushButton:hover {
                                        color: white;
                                        font-size: 25px;
                                    }
                              
                                           }
    """)
        
        button8.setStyleSheet("""
                                QPushButton {
                                        background-color: white ;
                                        border: 10px outset black;
                                        border-radius: 10px;
                                        color: Grey;
                                        font-size: 28px;
                                        font-family: "Arial";}
                                QPushButton:hover {
                                        color: white;
                                        font-size: 20px;
                                        color: black;
                                    }
                              
                                           }
    """)
        button9.setStyleSheet("""
                                QPushButton {
                                        background-color: #e74c3c;
                                        border: 10px outset #e74c3c;
                                        color: Black;
                                        font-size: 28px;
                                        font-family: "Arial";}
                                QPushButton:hover {
                                        color: white;
                                        font-size: 20px;
                                        color: black;
                                    }
                              
                                           }
    """)
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
        # Add radio buttons to the layout
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addWidget(button4)
        vbox.addWidget(button5)
        vbox.addWidget(button6)
        vbox.addWidget(button7)
        #vbox.addWidget(button8)
        #vbox.addWidget(button9)

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
