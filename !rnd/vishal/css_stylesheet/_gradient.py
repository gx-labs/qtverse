from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

if __name__ == "__main__":
    app = QApplication([])

   
    window = QWidget()
    layout = QVBoxLayout()
  
    button1 = QPushButton("Gradient Button1")
    button2 = QPushButton("Gradient Button2")
    button3 = QPushButton("Gradient Button3")
    button1.setStyleSheet(
        """
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                             stop:0 #bdc3c7, stop:1 #2c3e50);
           
            color: white;
            padding: 25px;
            border-radius: 5px;
        }
       
        """
    )
    button2.setStyleSheet(
        """
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                             stop:0 #8360c3, stop:1 #2ebf91);
            
            color: white;
            padding: 25px;
            border-radius: 5px;
        }
        
        """
    )
    button3.setStyleSheet(
        """
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                             stop:0 #aa4b6b, stop:1 #6b6b83, stop:2 #3b8d99);
            
            color: white;
            padding: 25px;
            border-radius: 5px;
        }
        
        """
    )
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    window.setLayout(layout)
    window.show()

    app.exec_()