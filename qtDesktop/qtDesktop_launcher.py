import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# from ui.temp import Temp
from ui.preview import PreviewAppWidget
from ui.themes import ThemesAppWidget
from ui.designer import DesignerAppWidget

CUR_FILE_DIR = os.path.dirname(__file__)

os.environ["QT_ICON_PATH"] = os.path.join(CUR_FILE_DIR, "ui\icons")

class QtWorldMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("qtVerse")
        
        # MENU BAR
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------

        menubar = QMenuBar(self)
        menubar_layout = QHBoxLayout()

        # 'menu
        qtverse_menu = QMenu("Qt Verse", self)
        
        qtverse_menu.addAction("Clean Favorites")
        qtverse_menu.addSeparator()
        qtverse_menu.addAction("Preferences")
        qtverse_menu.addSeparator()
        qtverse_menu.addAction("Settings")
        qtverse_menu.addAction("Quit")

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

        #### ----- ADD menu's in menubar
        menubar.addMenu(qtverse_menu)
        menubar.addMenu(windows_menu)
        menubar.addMenu(help_menu)

        menubar_layout.addWidget(menubar)
        menubar_layout.addSpacing(20)

        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------

        central_layout = QHBoxLayout()

        # sidebar_widget = QListWidget()

        # preview_widget = QListWidget()


        tab_widget = QTabWidget()

        tab1_layout = QHBoxLayout()
        tab1_layout.addWidget(PreviewAppWidget())

        # tab2_layout = QHBoxLayout()
        # tab2_layout.addWidget(Temp())

        tab3_layout = QHBoxLayout()
        tab3_layout.addWidget(ThemesAppWidget())

        tab4_layout = QHBoxLayout()
        tab4_layout.addWidget(DesignerAppWidget())
        
        tab_1 = QWidget()
        tab_1.setLayout(tab1_layout)

        # tab_2 = QWidget()
        # tab_2.setLayout(tab2_layout)

        tab_3 = QWidget()
        tab_3.setLayout(tab3_layout)

        tab_4 = QWidget()
        tab_4.setLayout(tab4_layout)

        tab_widget.addTab(tab_1, "Preview Widget")
        # tab_widget.addTab(tab_2, "qtverse Desktop")
        tab_widget.addTab(tab_3, "Themes")
        tab_widget.addTab(tab_4, "Design Widget")
        # tab_widget.setCurrentIndex(3)

        central_layout.addWidget(tab_widget)


        # central_layout.addWidget(sidebar_widget)
        # central_layout.addWidget(preview_widget)

        

        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------

        # main layout
        # ---------------------------------------------------------------------------

        main_layout = QVBoxLayout()
        main_layout.addLayout(menubar_layout)
        main_layout.addLayout(central_layout)
        main_layout.setContentsMargins(5, 0, 5, 0)
        self.setLayout(main_layout)

        self.showMaximized()

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
    
    # app.setPalette(palette)
    # app.setStyle("Fusion")                      # Set Fusion style
    # app.setStyleSheet(reva_style("app_dark.css"))
    
    window = QtWorldMainWindow()
    window.show()

    sys.exit(app.exec_())