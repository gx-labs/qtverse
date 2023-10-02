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

        # Create two separate QTabWidgets
        self.tab_widget1 = QTabWidget()
        self.tab_widget2 = QTabWidget()
        self.tab_widget3 = QTabWidget()


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

        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()

        self.tab_widget3.addTab(self.tab7, "Tab 7")
        self.tab_widget3.addTab(self.tab8, "Tab 8")
        self.tab_widget3.addTab(self.tab9, "Tab 9")

        # Create a QVBoxLayout for the main layout
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.tab_widget1)
        self.main_layout.addWidget(self.tab_widget2)
        self.main_layout.addWidget(self.tab_widget3)


        # Apply stylesheets for each QTabWidget
        self.tab_widget1.setStyleSheet("""
            QTabWidget::pane {
                border: 5px solid blue;
                border-radius: 5px;
                border-style : groove;                        

            }

            QTabWidget::tab-bar {
                alignment: left;
            }

            QTabBar::tab {
                background: #f0f0f0;
                border: 2px solid #d0d0d0;
                border-radius: 5px;
                padding: 5px 10px;
                min-width: 100px;
                min-height: 30px;
            }

            QTabBar::tab:selected {
                background: #3498db;
                color: white;
            }
        """)

        self.tab_widget2.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #ccc;
                border-radius: 10px;
            }

            QTabWidget::tab-bar {
                alignment: center;
            }

            QTabBar::tab {
                background: #dcdcdc;
                border: 2px solid #b0b0b0;
                border-radius: 10px;
                padding: 8px 10px;
                min-width: 120px;
                min-height: 40px;
            }

            QTabBar::tab:selected {
                background: #e74c3c;
                color: white;
            }
        """)
        self.tab_widget3.setStyleSheet("""
QTabWidget::pane { /* The tab widget frame */
    border-top: 2px solid #C2C7CB;
}

QTabWidget::tab-bar {
    left: 5px; 
}

QTabBar::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border: 2px solid #C4C4C3;
    border-bottom-color: #C2C7CB; /* same as the pane color */
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 100px;
    min-height: 30px;
}

QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB; /* same as pane color */
}

QTabBar::tab:!selected {
    margin-top: 2px; /* make non-selected tabs look smaller */
}

/* make use of negative margins for overlapping tabs */
QTabBar::tab:selected {
    /* expand/overlap to the left and right by 4px */
    margin-left: -4px;
    margin-right: -4px;
}

QTabBar::tab:first:selected {
    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
}

QTabBar::tab:last:selected {
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
}

QTabBar::tab:only-one {
    margin: 0; /* if there is only one tab, we don't want overlapping margins */
}
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyTabWidget()
    main_window.show()
    sys.exit(app.exec_())
