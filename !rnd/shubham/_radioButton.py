import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton
from PySide2.QtCore import Qt

class RadioButtonsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a QVBoxLayout as the main layout
        vbox = QVBoxLayout()

        # Create radio buttons with labels A, B, and C
        self.radio_button_a = QRadioButton("A")
        self.radio_button_b = QRadioButton("B")
        self.radio_button_c = QRadioButton("C")

        # Add radio buttons to the layout
        vbox.addWidget(self.radio_button_a)
        vbox.addWidget(self.radio_button_b)
        vbox.addWidget(self.radio_button_c)

        # Connect the hover events to slot functions
        self.radio_button_a.enterEvent = lambda event: self.onHover(self.radio_button_a)
        self.radio_button_a.leaveEvent = lambda event: self.onLeave(self.radio_button_a)
        
        self.radio_button_b.enterEvent = lambda event: self.onHover(self.radio_button_b)
        self.radio_button_b.leaveEvent = lambda event: self.onLeave(self.radio_button_b)
        
        self.radio_button_c.enterEvent = lambda event: self.onHover(self.radio_button_c)
        self.radio_button_c.leaveEvent = lambda event: self.onLeave(self.radio_button_c)

        radiobutton1 = QRadioButton("Radiobutton 3")
        radiobutton1.setStyleSheet("""QRadioButton {
                                           font-size: 14px;
                                            color: blue;
        spacing: 30px;

    }
                                    QRadioButton::indicator {
                                                    width: 20px;
                                                    height: 20px;
                                                    border : 5px BLUE;
                                                    border-style : groove;

    }
                                    QRadioButton::indicator:checked {
        background-color: blue;
        border : 5px solid white;

}
        QRadioButton::indicator:unchecked {
        background-color : white;
        border : 5px solid blue;


    }
    """)
        radiobutton2 = QRadioButton("Radiobutton 4")
        radiobutton2.setStyleSheet("""QRadioButton {
                                font-size: 20px;
                                color: black;
                                border : 1px solid black;
                                border-radius : 5px;
    }
                                QRadioButton::indicator {
                                border : 1px solid black;
                                width : 25;
                                height : 12;
                                border-radius : 7;
                                background-color: white;

                               }

                               QCheckBox::indicator:checked {


                                  background-color: black;
                               }
                                QCheckBox::indicator:unchecked {
                                  background-color: white;
                                   }
                                   """)
        radiobutton3 = QRadioButton("Radiobutton 5")
        radiobutton3.setStyleSheet("""QRadioButton {
                                font-size: 10px;
                                color: black;

    }
                            QRadioButton::indicator {
                                border : 1px solid black;
                               }

                               QCheckBox::indicator:checked {
                                  background-color: black;
                               }
                                QCheckBox::indicator:unchecked {
                                  background-color: white;}
                                   """)

        vbox.addWidget(radiobutton1)
        vbox.addWidget(radiobutton2)
        vbox.addWidget(radiobutton3)

        self.setLayout(vbox)

        self.setWindowTitle('Radio Buttons ')
        self.setGeometry(100, 100, 300, 150)




    def onHover(self, radio_button):
        radio_button.setStyleSheet("""QRadioButton {
                                    font-weight: 500;
                                    position: relative;
                                    margin-bottom: 0.375em;
                                   }""")

    def onLeave(self, radio_button):
        radio_button.setStyleSheet('QRadioButton {'
                                   '   border: 2px solid #3498db;'
                                   '}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RadioButtonsApp()
    ex.show()
    sys.exit(app.exec_())
