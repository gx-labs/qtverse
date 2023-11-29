import sys
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class PushButtonsApp(QWidget):
    def __init__(self):
        super().__init__()
        
        master_layout = QVBoxLayout()
        
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3')
        button4 = QPushButton('Button 4')
        button5 = QPushButton('Button 5')
        button6 = QPushButton('Button 6')
        
        button1.setStyleSheet('''QPushButton {
                                        background-color: #101275;
                                        padding: 5px;
                                        font-size: 12px;
                                        border: 1px solid #0078BD;
                                        border-radius: 5px;
                                    }
                                    
                                QPushButton:hover {
                                    background-color: #0095C8;
                                    }
                                
                                QPushButton:pressed {
                                    background-color: darkgrey
                                }
                                ''')
        
        master_layout.addWidget(button1)
        master_layout.addWidget(button2)
        master_layout.addWidget(button3)
        master_layout.addWidget(button4)
        master_layout.addWidget(button5)
        master_layout.addWidget(button6)
        
        self.setLayout(master_layout)
        self.setWindowTitle('Push Buttons')
        self.setGeometry(200, 200, 200, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButtonsApp()
    ex.show()
    sys.exit(app.exec_())
