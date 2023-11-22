import sys
import os

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class ThumbnailWidget(QWidget):

    def __init__(self, width, height):
        super(ThumbnailWidget, self).__init__()

        self.setFixedSize(width, height)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.thumbnail_and_buttons_layout = QHBoxLayout()
        self.thumbnail_and_buttons_layout.setContentsMargins(0,0,0,0)

        self.preview_label = QLabel("Preview")
        self.preview_label.setFixedSize(width, height)
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setStyleSheet("background-color: rgb(30,30,30)")

        self.thumbnail_and_buttons_layout.addWidget(self.preview_label)


        self.corner_buttons_layout = QVBoxLayout()
        self.corner_buttons_layout.setAlignment(Qt.AlignTop)


        self.button = QPushButton("1")
        self.button.setFixedWidth(20)
        self.button.hide()
        self.button.clicked.connect(self.triggered_placeholder_fn)


        self.corner_buttons_layout.addWidget(self.button)


        self.button2 = QPushButton("2")
        self.button2.setFixedWidth(20)
        self.button2.hide()
        self.button2.clicked.connect(self.triggered_placeholder_fn)

        self.corner_buttons_layout.addWidget(self.button2)


        self.button3 = QPushButton("3")
        self.button3.setFixedWidth(20)
        self.button3.hide()
        self.button3.clicked.connect(self.triggered_placeholder_fn)


        self.corner_buttons_layout.addWidget(self.button3)


        self.thumbnail_and_buttons_layout.addLayout(self.corner_buttons_layout)
        



        self.bottom_layout = QHBoxLayout()


        self.title_label = QLabel("sequence name")
        self.title_label.setFixedWidth(width)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("background-color: rgb(23,23,23)")
        self.title_label.hide()

        self.bottom_layout.addWidget(self.title_label)  


        self.favourites_button = QPushButton("<3")
        self.favourites_button.setFixedWidth(20)
        self.favourites_button.hide()
        self.favourites_button.clicked.connect(self.triggered_add_to_favourites)


        self.bottom_layout.addWidget(self.favourites_button)
        



        self.main_layout.addLayout(self.thumbnail_and_buttons_layout)
        self.main_layout.addLayout(self.bottom_layout)
        



        self.setLayout(self.main_layout)




        self.setMouseTracking(True)
        self.enterEvent = self.enter_event
        self.leaveEvent = self.exit_event


        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_thumbnailwidget_context_menu)


    # TODO : find a better way to show and hide the name label and buttons (overlaying layouts)
    # ---------------------------------------------------------------------------
    def enter_event(self, event):
        self.title_label.show()
        self.favourites_button.show()
        self.button.show()
        self.button2.show()
        self.button3.show()




    # ---------------------------------------------------------------------------
    def exit_event(self, event):
        self.title_label.hide()
        self.favourites_button.hide()
        self.button.hide()
        self.button2.hide()
        self.button3.hide()




    # ---------------------------------------------------------------------------
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
        copy_mov_path_action = QAction("Copy MOV Path", self)
        copy_mov_path_action.triggered.connect(lambda: self.triggered_copy_format_path("mov"))
        context_menu.addAction(copy_mov_path_action)

        # copy exr path
        copy_exr_path_action = QAction("Copy EXR Path", self)
        copy_exr_path_action.triggered.connect(lambda: self.triggered_copy_format_path("exr"))
        context_menu.addAction(copy_exr_path_action)

        # copy png path
        copy_png_path_action = QAction("Copy PNG Path", self)
        copy_png_path_action.triggered.connect(lambda: self.triggered_copy_format_path("png"))
        context_menu.addAction(copy_png_path_action)

        context_menu.addSeparator()

        # add to favs
        add_to_fav_action = QAction("Add To Favourites", self)
        add_to_fav_action.triggered.connect(self.triggered_add_to_favourites)
        context_menu.addAction(add_to_fav_action)

        # remove from favs
        remove_from_fav_action = QAction("Remove From Favourites", self)
        remove_from_fav_action.triggered.connect(self.triggered_remove_from_favourites)
        context_menu.addAction(remove_from_fav_action)

        # add to group
        add_to_group_action = QAction("Add To Group", self)
        add_to_group_action.triggered.connect(self.triggered_add_to_group)
        context_menu.addAction(add_to_group_action)

        context_menu.addSeparator()

        # Rename
        rename_action = QAction("Rename", self)
        rename_action.triggered.connect(self.triggered_rename)
        context_menu.addAction(rename_action)

        # Delete
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.triggered_delete)
        context_menu.addAction(delete_action)

        # Import
        import_action = QAction("Import", self)
        import_action.triggered.connect(self.triggered_import)
        context_menu.addAction(import_action)

        context_menu.addSeparator()

        # Upload To Cloud
        upload_to_cloud_action = QAction("Upload To Cloud", self)
        upload_to_cloud_action.triggered.connect(self.triggered_upload_to_cloud)
        context_menu.addAction(upload_to_cloud_action)

        # Update Frame Padding
        update_frame_padding_action = QAction("Update Frame Padding", self)
        update_frame_padding_action.triggered.connect(self.triggered_update_frame_padding)
        context_menu.addAction(update_frame_padding_action)

        context_menu.addSeparator()

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

    def triggered_add_to_favourites(self):
        print("added to favourites")
        
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