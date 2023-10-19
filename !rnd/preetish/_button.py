import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(800,800)
        self.setWindowTitle("Styled Buttons")
        layout = QVBoxLayout()

        self.button1 = QPushButton("Click Me!")
        self.button1.setMinimumSize(200, 60) 
        self.button1.setMaximumSize(400, 120)
        self.button1.setStyleSheet("""
                                    QPushButton{
                                        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
                                        font-weight: 500;
                                        font: 12pt "STIX MathJax Fraktur";
                                        background: #1F2937;
                                        color: white;
                                        border: none;
                                        position: relative;
                                        overflow: hidden;
                                        border-radius: 0.6em;
                                    }

                                    QPushButton:hover{
                                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2980b9, stop:1 #1f618d);
                                    }
                                    """)  

        self.button2 = QPushButton("Click Me!")
        self.button2.setMinimumSize(200, 60) 
        self.button2.setMaximumSize(400, 120)
        self.button2.setStyleSheet("""
                                    QPushButton{
                                        font-family: monospace;
                                        font-weight: 500;
                                        font: 12pt "STIX MathJax Fraktur";
                                        background-color: #f3f7fe;
                                        color: #3b82f6;
                                        border: none;
                                        border-radius: 8px;
                                        width: 100px;
                                        height: 45px;
                                        transition: .3s;
                                    }

                                    QPushButton:hover{
                                        background-color: #3b82f6;
                                        box-shadow: 0 0 0 5px #3b83f65f;
                                        color: #fff;
                                    }
                """)   

        self.button3 = QPushButton("Click Me!")
        self.button3.setMinimumSize(200, 60) 
        self.button3.setMaximumSize(400, 120)
        self.button3.setStyleSheet("""
                                    QPushButton {
                                        color: orange;
                                        background-color: qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.507, y2:1, stop:0 rgba(15, 32, 39, 98), stop:0.513924 rgba(20, 40, 49, 170), stop:1 rgba(26, 50, 60, 147));
                                        border: none;
                                    }

                                    QPushButton::hover{
                                        color: rgba(20, 40, 49, 170);
                                        background-color: ;
                                            background-color: qlineargradient(spread:pad, x1:0.248473, y1:0.483, x2:1, y2:0, stop:0.208955 rgba(131, 62, 40, 231), stop:1 rgba(163, 13, 23, 248));
                                        border: none;
                                    }
                """)     

        self.button4 = QPushButton("Click Me!")
        self.button4.setMinimumSize(200, 60) 
        self.button4.setMaximumSize(400, 120)
        self.button4.setStyleSheet("""
                                    QPushButton {
                                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3498db, stop:1 #2980b9);
                                        border: 2px solid #2980b9;
                                        color: #ffffff;
                                        padding: 10px 20px;
                                        border-radius: 10px;
                                        font-size: 16px;
                                        font-weight: bold;
                                        text-align: center;
                                        text-transform: uppercase;
                                    }

                                    QPushButton:hover {
                                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2980b9, stop:1 #1f618d);
                                    }

                                    QPushButton:pressed {
                                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1f618d, stop:1 #15467c);
                                        border: 2px solid #1863a0;
                                    }

                                    QPushButton:focus {
                                        border: 2px solid #3498db;
                                        outline: none;
                                    }

                                    QPushButton:disabled {
                                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bdc3c7, stop:1 #bdc3c7);
                                        border: 2px solid #bdc3c7;
                                        color: #95a5a6;
                                    }
                """) 


        self.button5 = QPushButton("Click Me!")
        self.button5.setMinimumSize(200, 60) 
        self.button5.setMaximumSize(400, 120)
        self.button5.setStyleSheet("""
                                    QPushButton {
                                        margin: 12px;
                                        height: 50px;
                                        width: 120px;
                                        border-radius: 10px;
                                        background: #333;
                                        justify-content: center;
                                        align-items: center;
                                        box-shadow: -5px -5px 15px #444, 5px 5px 15px #222, inset 5px 5px 10px #444, inset -5px -5px 10px #222;
                                        font-family: 'Damion', cursive;
                                        border: none;
                                        font-size: 16px;
                                        color: rgb(161, 161, 161);
                                        transition: 500ms;
                                    }

                                    QPushButton:hover {
                                        box-shadow: -5px -5px 15px #444, 5px 5px 15px #222, inset 5px 5px 10px #222, inset -5px -5px 10px #444;
                                        color: #d6d6d6;
                                        transition: 500ms;
                                    }
        """)  

        self.button6 = QPushButton("Click Me!")
        self.button6.setMinimumSize(200, 60) 
        self.button6.setMaximumSize(400, 120)
        self.button6.setStyleSheet("""
                                    QPushButton{
                                        border-style: solid;
                                        border-color: #050a0e;
                                        border-width: 1px;
                                        border-radius: 5px;
                                        color: #d3dae3;
                                        padding: 2px;
                                        background-color: #100E19;
                                    }
                            
                                    QPushButton::default{
                                        border-style: solid;
                                        border-color: #050a0e;
                                        border-width: 1px;
                                        border-radius: 5px;
                                        color: #FFFFFF;
                                        padding: 2px;
                                        background-color: #151a1e;
                                    }
                                    
                                    QPushButton:hover{
                                        border-style: solid;
                                        border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
                                        border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);
                                        border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
                                        border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
                                        border-width: 2px;
                                        border-radius: 1px;
                                        color: #d3dae3;
                                        padding: 2px;
                                    }

                                    QPushButton:pressed{
                                        border-style: solid;
                                        border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);
                                        border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);
                                        border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
                                        border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
                                        border-width: 2px;
                                        border-radius: 1px;
                                        color: #d3dae3;
                                        padding: 2px;
                                    }
        """)  

        self.setLayout(layout)
        layout.addWidget(self.button1, alignment=Qt.AlignCenter)
        layout.addWidget(self.button2, alignment=Qt.AlignCenter)
        layout.addWidget(self.button3, alignment=Qt.AlignCenter)
        layout.addWidget(self.button4, alignment=Qt.AlignCenter)
        layout.addWidget(self.button5, alignment=Qt.AlignCenter)
        layout.addWidget(self.button6, alignment=Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()