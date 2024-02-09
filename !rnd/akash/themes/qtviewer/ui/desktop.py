import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DesktopAppWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        central_layout = QHBoxLayout()

        sidebar_widget = QListWidget()
        
        item_1 = QListWidgetItem("Boilerplate for Widgets")
        item_1.setSizeHint(QSize(10,30))
        

        item_2 = QListWidgetItem("Informatin Widgets")
        item_2.setSizeHint(QSize(10,30)) 

        item_3 = QListWidgetItem("Notificaition Widgets")
        item_3.setSizeHint(QSize(10,30)) 

        item_4 = QListWidgetItem("Tool Widgets")
        item_4.setSizeHint(QSize(10,30)) 

        item_5 = QListWidgetItem("App Widgets")
        item_5.setSizeHint(QSize(10,30)) 

        sidebar_widget.addItem(item_1)
        sidebar_widget.addItem(item_2)
        sidebar_widget.addItem(item_3)
        sidebar_widget.addItem(item_4)
        sidebar_widget.addItem(item_5)

        sidebar_widget.setUniformItemSizes(True)
        preview_widget = QListWidget()


        central_layout.addWidget(sidebar_widget)
        central_layout.addWidget(preview_widget)

        self.setLayout(central_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = DesktopAppWidget()
    window.show()

    sys.exit(app.exec_())