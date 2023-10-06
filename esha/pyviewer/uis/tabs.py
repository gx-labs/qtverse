import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton

class tabs(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # central widget to hold the layout
        self.setFixedSize(500,400)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        tab_widget = QTabWidget()
        
        # orientation
        tab_widget.setTabPosition(QTabWidget.West)

        # add tabs
        tab1 = QWidget()
        tab2 = QWidget()

        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")

        
        # Add the tab widget to the layout
        layout.addWidget(tab_widget)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        self.setWindowTitle('Tabs')
        self.setGeometry(100, 100, 400, 300)

def main():
    app = QApplication(sys.argv)
    window = tabs()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
