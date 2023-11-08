import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from PySide2.QtCore import Qt

class MyTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Styled Tabs Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.tab_widget1 = QTabWidget(self.central_widget)
        self.tab_widget2 = QTabWidget(self.central_widget)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tab_widget1.addTab(self.tab1, "Tab 1")
        self.tab_widget1.addTab(self.tab2, "Tab 2")
        self.tab_widget1.addTab(self.tab3, "Tab 3")

        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.tab_widget2.addTab(self.tab4, "Tab 4")
        self.tab_widget2.addTab(self.tab5, "Tab 5")
        self.tab_widget2.addTab(self.tab6, "Tab 6")

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget1)
        self.layout.addWidget(self.tab_widget2)

        self.setStyleSheet("""
            QTabWidget#tab_widget1::pane {
                border: 2px solid #e0e0e0;
                border-radius: 5px;
            }

            QTabWidget#tab_widget1::tab-bar {
                alignment: center;
            }

            QTabBar#tab_bar1::tab {
                background: #f0f0f0;
                border: 2px solid #d0d0d0;
                border-radius: 5px;
                padding: 5px 10px;
                min-width: 100px;
                min-height: 30px;
            }

            QTabBar#tab_bar1::tab:selected {
                background: #3498db;
                color: white;
            }

            QTabWidget#tab_widget2::pane {
                border: 2px solid #ccc;
                border-radius: 10px;
            }

            QTabWidget#tab_widget2::tab-bar {
                alignment: center;
            }

            QTabBar#tab_bar2::tab {
                background: #dcdcdc;
                border: 2px solid #b0b0b0;
                border-radius: 10px;
                padding: 8px 15px;
                min-width: 120px;
                min-height: 40px;
            }

            QTabBar#tab_bar2::tab:selected {
                background: #e74c3c;
                color: white;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyTabWidget()
    main_window.show()
    sys.exit(app.exec_())
