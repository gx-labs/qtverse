import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget
from PySide2.QtCore import Qt

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar Style Example")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        calendar1 = QCalendarWidget(self)
        calendar1.setStyleSheet('''
            QCalendarWidget {
                background-color: lightgrey;
                border: 2px solid darkgrey;
            }
            
            QToolButton#qt_calendar_prevmonth {
                background-color: #cc0000;
            }
            
            QToolButton#qt_calendar_nextmonth {
                background-color: #00cc00;
            }
            
            QToolButton#qt_calendar_monthbutton {
                background-color: #0000cc;
                color: white;
            }
        ''')

        calendar2 = QCalendarWidget(self)
        calendar2.setStyleSheet('''
  QCalendarWidget QToolButton {
  	height: 60px;
  	width: 150px;
  	color: white;
  	font-size: 24px;
  	icon-size: 56px, 56px;
  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);
  }
            QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }

            QCalendarWidget QMenu {
  	width: 150px;
  	left: 20px;
  	color: white;
  	font-size: 18px;
  	background-color: rgb(100, 100, 100);
  }
                                
  QCalendarWidget QSpinBox { 
  	width: 150px; 
  	font-size:24px; 
  	color: white; 
  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); 
  	selection-background-color: rgb(136, 136, 136);
  	selection-color: rgb(255, 255, 255);
  }
  QCalendarWidget QAbstractItemView:enabled 
  {
  	font-size:24px;  
  	color: rgb(180, 180, 180);  
  	background-color: black;  
  	selection-background-color: rgb(64, 64, 64); 
  	selection-color: rgb(0, 255, 0); 
  }
        ''')

        layout.addWidget(calendar1)
        layout.addWidget(calendar2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())
