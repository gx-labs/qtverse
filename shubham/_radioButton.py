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

        # Set the layout for the main window
        self.setLayout(vbox)

        self.setWindowTitle('Styled Radio Buttons Example')
        self.setGeometry(100, 100, 300, 150)

    def onHover(self, radio_button):
        radio_button.setStyleSheet("""QRadioButton {
                                    display: flex;
                                    cursor: pointer;
                                    font-weight: 500;
                                    position: relative;
                                    overflow: hidden;
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
