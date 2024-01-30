import os
import sys
import yaml
import importlib.util
from pprint import pprint

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui.utils import read_yaml
from ui.widgets.clickable_label import ClickableLabel

from ui.widgets.flow_layout import FlowLayout
from ui.widgets.thumbnail import ThumbnailWidget



STATUS_COLOR_MAP = {
    "wip": "rgb(18, 46, 204)",
    "submitted": "rgb(219, 166, 20)",
    "review": "rgb(255, 0, 127)",
    "approved": "rgb(0, 168, 107)"
}

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

widgets_src_dir = os.path.join(project_dir, "qtverse", "widgets", "src", "WIDGETS")
config_file_path = os.path.join(os.path.dirname(__file__), "cfg", "settings.yaml")


class ThumbnailViewerWidget(QWidget):

    def __init__(self):
        super(ThumbnailViewerWidget, self).__init__()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # ------------------------------
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll_area_layout = FlowLayout()
        self.scroll_area_layout.setAlignment(Qt.AlignTop)

        self.scroll_area_qwidget = QWidget()
        self.scroll_area_qwidget.setLayout(self.scroll_area_layout)

        # add custom scroll layout in QScrollArea widget
        self.scroll_area.setWidget(self.scroll_area_qwidget)

        self.main_layout.addWidget(self.scroll_area)

        # self.populateThumbnails()
        

    def populateThumbnails(self):

        while self.scroll_area_layout.count():
            item = self.scroll_area_layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        for i in range(1, 20):
            self.thumbnail_widget = ThumbnailWidget(width = 200, height = 100)
            self.scroll_area_layout.addWidget(self.thumbnail_widget)

# Custom List Widget Class Start
    # Removed
# Custom List Widget Class End
class DeveloperViewerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.vertical_layout = QVBoxLayout()

        # Dev and Status Button Filters Start
            # Removed
        # Dev and Status Button Filters End

        self.thumbnail_layout = QHBoxLayout()
        self.thumbnail_widget = ThumbnailViewerWidget()
        # self.thumbnail_widget.setStyleSheet("margin:5px; border:1px solid rgb(0, 255, 0); ")
        self.thumbnail_layout.addWidget(self.thumbnail_widget)

        self.archive_layout = QHBoxLayout()
        self.archive_widget = ThumbnailViewerWidget()
        # self.thumbnail_widget.setStyleSheet("margin:5px; border:1px solid rgb(0, 255, 0); ")
        self.archive_layout.addWidget(self.archive_widget)

        # -----------------------
        # Viewer Tab's  ( Thumbnail View - Archive View ) TABS
        viewer_tab_widget = QTabWidget()
        
        tab_1 = QWidget()
        tab_2 = QWidget()

        # tab1_layout = QHBoxLayout()
        # tab2_layout = QHBoxLayout()

        tab_1.setLayout(self.thumbnail_layout)
        tab_2.setLayout(self.archive_layout)

        viewer_tab_widget.addTab(tab_1, "All Widgets")
        viewer_tab_widget.addTab(tab_2, "Archived Widgets")

        self.vertical_layout.addWidget(viewer_tab_widget)

        ##

        self.setLayout(self.vertical_layout)
        self.showMaximized()
        
        # Populate the QListWidget with folders based on the initial state (ALL)
        # self.filter_by_developer("ALL")

        self.populate_widgets()

    def _get_developer_folders(self):
        """
        dev_folders : ['ESH', 'PRT', 'SHB', 'SMB']
        """
        dev_folders = []
        for entry in os.scandir(widgets_src_dir):
            if entry.is_dir():
                dev_folders.append(entry.name)

        return dev_folders

    def _get_widget_folders_for_dev(self, dev_folder):
        """
        returns a dict :
        {dev_folder : widget_folder_path}

        example:
        {'ESH_001': 'e:\\HDD\\Partition2\\programming\\_code\\repos_C\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_001', 
        'ESH_002': 'e:\\HDD\\Partition2\\programming\\_code\\repos_C\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_002', 
        'ESH_003': 'e:\\HDD\\Partition2\\programming\\_code\\repos_C\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_003', 
        'ESH_004': 'e:\\HDD\\Partition2\\programming\\_code\\repos_C\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_004'}
        """
        widget_folders = {}
        dev_folder_path = os.path.join(widgets_src_dir, dev_folder)

        if os.path.exists(dev_folder_path):
            for folder_name in os.listdir(dev_folder_path):
                folder_path = os.path.join(dev_folder_path, folder_name)

                if os.path.isdir(folder_path):
                    widget_folders[folder_name] = folder_path

        return widget_folders

    def _import_ui_as_module(self, widget_filename, widget_py_path):
        spec = importlib.util.spec_from_file_location(widget_filename, widget_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        ui_class = getattr(module, widget_filename)
        ui_instance = ui_class()

        return ui_instance

    def populate_widgets(self):

        # populalte_listView()
        # populate_thumbnailView()
        all_widgets = {}

        all_dev_folders = self._get_developer_folders()
        for each_dev_folder in all_dev_folders:
            all_dev_widget = self._get_widget_folders_for_dev(each_dev_folder)
            all_widgets[each_dev_folder] = all_dev_widget
        
        print(all_widgets)
        # print("------------------------")

        all_widgets_dict = {}
        for each_dev_tuple in all_widgets.items():
            # pprint(each_dev_tuple, each_dev_tuple[0] , each_dev_tuple[1])
            for each_widget in each_dev_tuple[1].items():
                each_widget_list = (list(each_widget))
                all_widgets_dict[each_widget_list[0]] = each_widget_list[1]
        
        pprint(all_widgets_dict)

        for each_widget in all_widgets_dict.items():
            each_widget_name = each_widget[0]
            each_widget_path = each_widget[1]

            widget_py_path = os.path.join(each_widget_path, "widget", "CustomWidget.py")
            
            info_filepath = os.path.join(each_widget_path, "info.yaml")
            info_dict = read_yaml(filepath=info_filepath)

            css_filepath = os.path.join(each_widget_path, "widget", "style.css")
            with open(css_filepath) as file:
                css_data = file.read().replace('\n',' ')
            
            if os.path.exists(widget_py_path):
                imported_widget = self._import_ui_as_module("CustomWidget", widget_py_path)
                print(imported_widget)

                self.custom_thumbnail_widget = ThumbnailWidget(
                    widget_name=each_widget_name,
                    widget_path=each_widget_path,
                    css_data=css_data,
                    custom_widget=imported_widget, 
                    info_dict=info_dict,
                    width=200, 
                    height=100
                    )
                
                self.thumbnail_widget.scroll_area_layout.addWidget(self.custom_thumbnail_widget)



    def filter_by_developer(self, developer):
        # Store the currently selected developer
        self.current_developer = developer

        # Clear the list widget
        self.list_widget.clear()

        # Repopulate the list widget with widgets that match the selected developer
        dev_folders = self._get_developer_folders()
        for dev_folder in dev_folders:
            if self.current_developer == "ALL" or self.current_developer == dev_folder:
                widget_folders = self._get_widget_folders_for_dev(dev_folder)
                for folder_name, folder_path in widget_folders.items():
                    # Read status from info.yaml
                    info_yaml_file_path = os.path.join(folder_path, "info.yaml")
                    info_data = read_yaml(info_yaml_file_path)

                    folder_status = info_data.get('status')
                    status_color = STATUS_COLOR_MAP.get(folder_status, "black")  # Get the color based on status, default to black if not found

                    custom_widget = CustomListWidgetItem(folder_name, folder_path, status_color)
                    list_item = QListWidgetItem()
                    list_item.setSizeHint(custom_widget.sizeHint())
                    self.list_widget.addItem(list_item)
                    self.list_widget.setItemWidget(list_item, custom_widget)

    def filter_by_status(self, status):
        # Store the currently selected status
        self.current_status = status

        # Clear the list widget
        self.list_widget.clear()

        # Repopulate the list widget with widgets that match the selected status
        dev_folders = self._get_developer_folders()
        for dev_folder in dev_folders:
            widget_folders = self._get_widget_folders_for_dev(dev_folder)
            for folder_name, folder_path in widget_folders.items():
                # Read status from info.yaml
                info_yaml_file_path = os.path.join(folder_path, "info.yaml")
                info_data = read_yaml(info_yaml_file_path)

                folder_status = info_data.get('status')

                if self.current_status == "ALL" or self.current_status == folder_status:
                    status_color = STATUS_COLOR_MAP.get(folder_status, "black")  # Get the color based on status, default to black if not found
                    custom_widget = CustomListWidgetItem(folder_name, folder_path, status_color)
                    list_item = QListWidgetItem()
                    list_item.setSizeHint(custom_widget.sizeHint())
                    self.list_widget.addItem(list_item)
                    self.list_widget.setItemWidget(list_item, custom_widget)

    def on_item_clicked(self, item):
        
        config_dict = read_yaml(config_file_path)
        widget_foldername = config_dict.get("widget_foldername")
        widget_filename = config_dict.get("widget_filename")

        if isinstance(item, QListWidgetItem):
            widget_item = self.list_widget.itemWidget(item)
            print(f"widget item: {widget_item}")

            if widget_item:
                widget_py_path = os.path.join(widget_item.folder_path, widget_foldername, (widget_filename + ".py"))
            
                if os.path.exists(widget_py_path):
                    try:
                        ui_instance = self._import_ui_as_module(widget_filename, widget_py_path)
                    except Exception as e:
                        print(f"Error: {e}")
                    
                    # display widget
                    while self.contents_layout.count():
                        item = self.contents_layout.takeAt(0)
                        widget = item.widget()

                        if widget:
                            widget.setParent(None)

                    self.contents_layout.addWidget(ui_instance)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DeveloperViewerWidget()
    main_window.show()
    app.exec_()
