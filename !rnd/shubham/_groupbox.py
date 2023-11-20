import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
class StyledGroupBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GroupBoxes')
        self.setFixedSize(800,800)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        self.group_box = QGroupBox("Styled GroupBox")
        self.group_box.setAlignment(Qt.AlignCenter)  
        self.group_box.setStyleSheet("""
    QGroupBox {
        border: 2px solid #007ACC; 
        border-radius: 6px; 
        margin-top: 10px; 
    }
    
    QGroupBox::title {
        subcontrol-origin: margin; 
        subcontrol-position: top center; 
        padding: 5px; 
        font-size: 16px; 
        font-weight: bold; 
    }
    
""")

        self.group_box1 = QGroupBox("Group Box 1")
        self.group_box1.setStyleSheet("""
                                        QGroupBox { 
                                            background-color: purple; 
                                            border: 2px solid black groove; 
                                            border-radius: 5px; 
                                            }
                                        QGroupBox::title  {
                                            color: white;
                                            font-size: 10em;
                                            font-weight: bold; 

                                        }
            """)
        
        self.group_box2 = QGroupBox("Group Box 2")
        self.group_box2.setStyleSheet("""
                                        QGroupBox  {
                                            border: 3px solid;
                                            border-color: white;
                                            margin-top: 27px;
                                            font-size: 14px;
                                        }
                                        
                                        QGroupBox::title  {
                                            color: #fff;
                                            background-color: black;
                                            subcontrol-origin: margin;
                                            subcontrol-position: top center;
                                            padding: 5px 8000px 5px 8000px;
                                        }
        """)

        self.group_box3 = QGroupBox("Group Box 3")
        self.group_box3.setStyleSheet("""
                                        QGroupBox {
                                            border: 1px solid;
                                            border-color: #025c0d;
                                            margin-top: 2em;
                                            font-size: 5em;
                                            border-top-right-radius: 6px;
                                            border-bottom-left-radius: 6px;
                                            border-bottom-right-radius: 6px;
                                        }
                                        
                                        QGroupBox::title {
                                            color: #fff;
                                            background-color: blue;
                                            subcontrol-origin: margin;
                                            padding: 2em 3em;
                                            border-top-left-radius: 6px;
                                            border-top-right-radius: 6px;
                                        }
        """)

        self.group_box4 = QGroupBox("Group Box 4")
        self.group_box4.setStyleSheet("""
                                        QGroupBox {
                                            border: 1px solid;
                                            border-color: #c3db5a;
                                            font-size: 5em;
                                            border-radius: 6px;
                                        }
                                        
                                        QGroupBox::title {
                                            color: black;
                                            background: transparent;
                                            subcontrol-origin: margin;
                                            subcontrol-position: top center;
                                            padding: 0.4em 0 0 0;
                                        }
        """)
        
        layout.addWidget(self.group_box)
        layout.addWidget(self.group_box1)
        layout.addWidget(self.group_box2)
        layout.addWidget(self.group_box3)
        
        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StyledGroupBoxExample()
    sys.exit(app.exec_())