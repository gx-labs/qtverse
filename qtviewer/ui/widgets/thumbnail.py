import sys
import os

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import pyperclip


class ThumbnailWidget(QWidget):

    def __init__(self, widget_name, widget_path, css_data, custom_widget, info_dict, width, height):
        super(ThumbnailWidget, self).__init__()

        # self.setFixedSize(width, height)
        self._info_dict = info_dict
        self._css_data = css_data
        self._widget_name = widget_name
        self._widget_path = widget_path

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        # --------------------
        self.thumbnail_and_buttons_layout = QHBoxLayout()
        self.thumbnail_and_buttons_layout.setContentsMargins(0,0,0,0)
        

        # self.preview_label = QLabel("Preview")
        # self.preview_label.setFixedSize(width, height)
        # self.preview_label.setAlignment(Qt.AlignCenter)
        # self.preview_label.setStyleSheet("background-color: rgb(30,30,30)")

        # self.thumbnail_and_buttons_layout.addWidget(self.preview_label)
        self.thumbnail_and_buttons_layout.addWidget(custom_widget)

        # --------------------
        # self.corner_buttons_layout = QVBoxLayout()
        # self.corner_buttons_layout.setAlignment(Qt.AlignTop)

        # self.button = QPushButton("1")
        # self.button.setFixedWidth(20)
        # self.button.hide()
        # self.button.clicked.connect(self.triggered_placeholder_fn)
        # self.corner_buttons_layout.addWidget(self.button)

        # self.button2 = QPushButton("2")
        # self.button2.setFixedWidth(20)
        # self.button2.hide()
        # self.button2.clicked.connect(self.triggered_placeholder_fn)
        # self.corner_buttons_layout.addWidget(self.button2)

        # self.button3 = QPushButton("3")
        # self.button3.setFixedWidth(20)
        # self.button3.hide()
        # self.button3.clicked.connect(self.triggered_placeholder_fn)
        # self.corner_buttons_layout.addWidget(self.button3)

        # self.thumbnail_and_buttons_layout.addLayout(self.corner_buttons_layout)
        
        # --------------------
        self.bottom_layout = QHBoxLayout()

        self.title_label = QLabel(widget_name)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.hide()
        self.bottom_layout.addWidget(self.title_label)  

        self.copy_css_button = QPushButton("Copy CSS")
        self.copy_css_button.setFixedWidth(65)
        self.copy_css_button.hide()
        self.copy_css_button.clicked.connect(self.clicked_copy_css)
        self.bottom_layout.addWidget(self.copy_css_button)
        
        # --------------------
        self.main_layout.addLayout(self.thumbnail_and_buttons_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)

        self.setMouseTracking(True)
        self.enterEvent = self.enter_event
        self.leaveEvent = self.exit_event

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_thumbnailwidget_context_menu)


    def enter_event(self, event):
        self.title_label.show()
        self.copy_css_button.show()
        # self.button.show()
        # self.button2.show()
        # self.button3.show()

    def exit_event(self, event):
        self.title_label.hide()
        self.copy_css_button.hide()
        # self.button.hide()
        # self.button2.hide()
        # self.button3.hide()

    def show_thumbnailwidget_context_menu(self, pos):
        context_menu = QMenu(self)

        # open in explorer
        open_in_explorer_action = QAction("Open In Explorer", self)
        open_in_explorer_action.triggered.connect(self.triggered_open_in_explorer)
        context_menu.addAction(open_in_explorer_action)

        # copy full path
        copy_full_path_action = QAction("Copy Full Path (dir)", self)
        copy_full_path_action.triggered.connect(self.triggered_copy_full_path)
        context_menu.addAction(copy_full_path_action)

        context_menu.addSeparator()

        # copy mov path
        copy_mov_path_action = QAction("Copy CSS File Path", self)
        copy_mov_path_action.triggered.connect(lambda: self.triggered_copy_format_path("mov"))
        context_menu.addAction(copy_mov_path_action)

        # copy exr path
        copy_exr_path_action = QAction("Copy Widget Path", self)
        copy_exr_path_action.triggered.connect(lambda: self.triggered_copy_format_path("exr"))
        context_menu.addAction(copy_exr_path_action)

        # Info
        info_action = QAction("Info", self)
        info_action.triggered.connect(self.triggered_info)
        context_menu.addAction(info_action)

        context_menu.exec_(self.sender().mapToGlobal(pos))



    # ---------------------------------------------------------------------------
    def triggered_open_in_explorer(self):
        # os.startfile("path_to_element")
        print("opened explorer")

    def triggered_copy_full_path(self):
        print("copied full path")

    def triggered_copy_format_path(self, format):
        print("copied:", format)

    def clicked_copy_css(self):
        """
        """
        print("clicked copy css")
        pyperclip.copy(self._css_data)

        
    def triggered_remove_from_favourites(self):
        print("removed from favourites")

    def triggered_add_to_group(self):
        print("added to group")

    def triggered_rename(self):
        print("renamed")

    def triggered_delete(self):
        print("deleted")

    def triggered_import(self):
        print("imported")
    
    def triggered_upload_to_cloud(self):
        print("uploaded to cloud")
    
    def triggered_update_frame_padding(self):
        print("updated frame padding")

    def triggered_info(self):
        # print("detailed info/metadata")
        print("thumbnail size =", self.size())

    def triggered_placeholder_fn(self):
        print("triggered placeholder_fn")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ThumbnailWidget(320, 180)
    window.show()
    sys.exit(app.exec_())