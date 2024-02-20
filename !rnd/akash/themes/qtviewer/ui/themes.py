import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ThemesAppWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        central_layout = QHBoxLayout()
        
        sidebar_widget = QWidget()
        sidebar_widget.setMaximumWidth(200)

        sidebar_layout = QVBoxLayout()
        sidebar_widget.setLayout(sidebar_layout)
        title = QLabel("List of Themes")

        list_widget = QListWidget()
        
        item_1 = QListWidgetItem("Item 1")
        item_1.setSizeHint(QSize(10,30)) 
        list_widget.addItem(item_1)

        list_widget.setUniformItemSizes(True)
        preview_widget = QListWidget()

        sidebar_layout.addWidget(title)
        sidebar_layout.addWidget(list_widget)

        central_layout.addWidget(sidebar_widget)
        central_layout.addWidget(preview_widget)

        self.setLayout(central_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = ThemesAppWidget()
    window.show()

    sys.exit(app.exec_())