import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QCalendarWidget
from PySide2.QtCore import Qt

class CalendarStylingExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QCalendarWidget
        calendar = QCalendarWidget(self)
        self.setCentralWidget(calendar)

        # Apply styles to the QCalendarWidget
        style_sheet = """
                        QCalendarWidget QWidget{
                        background-color:magenta;
                        color: green;

                        }

                        QCalendarWidget QToolButton{
                        background-color:black;
                        color: green;
                        icon-size: 30px;
                        }

                        QCalendarWidget QMenu{
                        background-color:magenta;
                        color: green;

                        }

                        QCalendarWidget QAbstractItemView:enabled{
                        background-color: yellow;
                        color: black;
                        }

                        QCalendarWidget QAbstractItemView:disabled{
                        background-color: yellow;
                        color: white;
                        }

                        QCalendarWidget QMenu{
                            background-color: rgb(255, 46, 221);
                        }

                        QCalendarWidget QSpinBox{
                            background-color: black;
                        }
        """

        calendar.setStyleSheet(style_sheet)

        # Set the initial date for the calendar
        calendar.setSelectedDate(calendar.selectedDate())

        self.setWindowTitle("Styled Calendar Widget")
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarStylingExample()
    window.show()
    sys.exit(app.exec_())
