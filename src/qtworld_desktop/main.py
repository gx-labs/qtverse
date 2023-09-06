import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

CUR_FILE_DIR = os.path.dirname(__file__)


class QtWorldMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Qt World - Desktop")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setMinimumSize(1280, 720)
        # self.resize(1280, 720)
        # self.showMaximized()

        self.current_directory = os.path.dirname(__file__)
        print("current dir:", os.path.dirname(self.current_directory))
        
        # MENU BAR
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------

        menubar = QMenuBar(self)
        menubar_layout = QHBoxLayout()

        # 'reva menu
        reva_menu = QMenu("Qt World", self)
        
        reva_menu.addAction("Clean Favorites")
        reva_menu.addSeparator()
        reva_menu.addAction("Preferences")
        reva_menu.addSeparator()
        reva_menu.addAction("Settings")
        reva_menu.addAction("Quit")
        


        # 'Windows' menu
        windows_menu = QMenu("Windows", self)

        menuiteam_sidebar = QAction("Sidebar", self)
        menuiteam_sidebar.setCheckable(True)
        menuitem_properties = QAction("Properties", self)
        menuitem_properties.setCheckable(True)
        menuitem_viewer = QAction("Viewer", self)
        menuitem_viewer.setCheckable(True)

        windows_menu.addAction(menuiteam_sidebar)
        windows_menu.addAction(menuitem_properties)
        windows_menu.addAction(menuitem_viewer)

        # 'Help' menu
        help_menu = QMenu("Help", self)

        # for user help
        help_menu.addAction("Keyboard Shortcuts")
        help_menu.addSeparator()
        # logs
        logs_submenu = help_menu.addMenu("View Logs")
        logs_submenu.addAction("View Activity Logs")
        logs_submenu.addAction("Open Logs Folder")
        help_menu.addSeparator()
        # app
        help_menu.addAction("About QtWorld")
        help_menu.addAction("Release Notes")
        help_menu.addAction("Support Documentation")
        help_menu.addAction("Online Documentation")
        help_menu.addAction("Check For Software Updates")
        help_menu.addSeparator()
        help_menu.addAction("Contact Support")
        help_menu.addAction("Submit Feedback")
        help_menu.addAction("Report Issue")

        # 'ADMIN' Label 
        self.admin_label = QLabel("ADMIN")

        self.admin_label_opacity = QGraphicsOpacityEffect(self)
        self.admin_label_opacity.setOpacity(0.5)
        self.admin_label.setGraphicsEffect(self.admin_label_opacity)

        #### ----- ADD menu's in menubar
        menubar.addMenu(reva_menu)
        menubar.addMenu(windows_menu)
        menubar.addMenu(help_menu)

        menubar_layout.addWidget(menubar)
        menubar_layout.addWidget(self.admin_label)        
        menubar_layout.addSpacing(20)


        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------

        # main layout
        # ---------------------------------------------------------------------------

        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.addLayout(menubar_layout)
        main_layout.setContentsMargins(5, 0, 5, 0)
        self.setLayout(main_layout)

        self.showMaximized()




# execution block
# ======================================================================================================================================================
# ======================================================================================================================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Set Fusion palette
    #-----------------------------------------------------
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(53, 53, 53))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    
    app.setPalette(palette)
    app.setStyle("Fusion")                      # Set Fusion style
    # app.setStyleSheet(reva_style("app_dark.css"))
    
    window = QtWorldMainWindow()
    window.show()

    sys.exit(app.exec_())