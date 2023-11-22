import sys
import os

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from widgets.flow_layout import FlowLayout
from widgets.thumbnail import ThumbnailWidget

class ThumbnailViewer(QWidget):

    def __init__(self):
        super(ThumbnailViewer, self).__init__()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # ------------------------------
        self.scroll_area_layout = FlowLayout()
        self.scroll_area_layout.setAlignment(Qt.AlignTop)

        self.scroll_area_qwidget = QWidget()
        self.scroll_area_qwidget.setLayout(self.scroll_area_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.scroll_area_qwidget)

        self.main_layout.addWidget(self.scroll_area)

        self.populateThumbnails()
        

    def populateThumbnails(self):

        while self.scroll_area_layout.count():
            item = self.scroll_area_layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        for i in range(1, 20):
            self.thumbnail_widget = ThumbnailWidget(width = 200, height = 100)
            self.scroll_area_layout.addWidget(self.thumbnail_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ThumbnailViewer()
    window.show()
    sys.exit(app.exec_())