import os
import sys
import time
import importlib.util
from pprint import pprint

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui.general_utils import read_yaml
from ui.general_utils import qt_icon

from ui.widgets.custom.clickable_label import ClickableLabel
from ui.widgets.custom.flow_layout import FlowLayout
from ui.widgets.custom.thumbnail import ThumbnailWidget


# STATUS_COLOR_MAP = {
#     "wip": "rgb(18, 46, 204)",
#     "submitted": "rgb(219, 166, 20)",
#     "review": "rgb(255, 0, 127)",
#     "approved": "rgb(0, 168, 107)"
# }

WIDGET_STATUS_LIST = ["WiP", "Submitted", "Review", "Approved"]

# setup path variables
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
widget_templates_dir = os.path.join(project_dir, "qtDesktop", "ui", "templates", "WIDGETS")

all_widgets_src_dir = os.path.join(project_dir, "qtverse", "widgets", "src", "WIDGETS")
arch_widgets_src_dir = os.path.join(project_dir, "qtverse", "widgets", "src", "WIDGETS_ARC")
dev_widgets_src_dir = os.path.join(project_dir, "qtverse", "widgets", "src", "WIDGETS_DEV")

config_file_path = os.path.join(os.path.dirname(__file__), "cfg", "cfg.yaml")

config_data = read_yaml(config_file_path)
all_developers = config_data["developers"].keys()

class Worker(QObject):
    
    error = Signal(str)
    complete = Signal(dict)
    
    @Slot(str, list)
    def get_widget_objects_dict(self, widgets_src_dir, widgets_list):
        dict = {}
        for widget_name in widgets_list:
            widget_seq_name = str(widget_name[:3])
            each_widget_path = os.path.join(widgets_src_dir, widget_seq_name, widget_name)

            widget_py_path = os.path.join(each_widget_path, "widget", "CustomWidget.py")
                            
            info_filepath = os.path.join(each_widget_path, "info.yaml")
            info_dict = read_yaml(filepath=info_filepath)

            css_filepath = os.path.join(each_widget_path, "widget", "style.css")
                        
            # Catch FileNotFoundError and prevent app from crashing
            try:
                with open(css_filepath) as file:
                    css_data = file.read().replace('\n',' ')
            except FileNotFoundError:
                self.error.emit(f"{each_widget_path} seems to be empty.")
                pass
                           
            if os.path.exists(widget_py_path):
                imported_widget = self._import_ui_as_module("CustomWidget", widget_py_path)

                self.custom_thumbnail_widget = ThumbnailWidget(
                    widget_name=widget_name,
                    widget_path=each_widget_path,
                    css_data=css_data,
                    custom_widget=imported_widget, 
                    info_dict=info_dict,
                    width=200, 
                    height=100)
                                
                dict.update({str(widget_name) : self.custom_thumbnail_widget})
            else:
                self.error.emit("Error!")
                
        self.complete.emit(dict)
        self.killTimer(0)
    
    def _import_ui_as_module(self, widget_filename, widget_py_path):
        spec = importlib.util.spec_from_file_location(widget_filename, widget_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        ui_class = getattr(module, widget_filename)
        ui_instance = ui_class()

        return ui_instance
    
class ThumbnailViewerWidget(QWidget):
    '''
    This class is the scroll area where all the widgets are populated. Each tab (all, archive and dev) have their own instance
    of this class
    '''
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

class PreviewAppWidget(QWidget):
    load_dev_widget_objects = Signal(str, list)
    load_arch_widget_objects = Signal(str, list)
    load_all_widget_objects = Signal(str, list)
    def __init__(self):
        super().__init__()
        
        self.widget_load_start_index = 0
        self.widget_load_end_index = 99
    
        # vars for storing dict of widgets according to seq
        self.all_widgets_dict = self._get_widgets_dict(all_widgets_src_dir)
        self.arch_widgets_dict = self._get_widgets_dict(arch_widgets_src_dir)
        self.dev_widgets_dict = self._get_widgets_dict(dev_widgets_src_dir)
        
        # vars for storing lists of widgets
        self.all_widgets_list = self._flatten_dict_to_list(self.all_widgets_dict)
        self.arch_widgets_list = self._flatten_dict_to_list(self.arch_widgets_dict)
        self.dev_widgets_list = self._flatten_dict_to_list(self.dev_widgets_dict)

        # ------------------------------------------------------
        
        self.master_vbox = QVBoxLayout()
        
        # layout for all the filter options
        self.filters_hbox = QHBoxLayout()
        
        # button to load all widgets
        self.all_widgets_button = QPushButton("All")
        self.all_widgets_button.setEnabled(False)
        self.all_widgets_button.clicked.connect(self.clicked_show_all_widgets)
        
        # labels to show count of all, archived and dev widgets
        self.count_labels_font = QFont()
        self.count_labels_font.setBold(True)
        self.count_labels_font.setPointSize(10)

        self.all_widgets_count_label = QLabel(f"All Widgets:\n  {len(self.all_widgets_list)}")
        self.all_widgets_count_label.setFont(self.count_labels_font)
        self.all_widgets_count_label.setStyleSheet("color: red")
        
        self.arch_widgets_count_label = QLabel(f"Arch. Widgets:\n   {len(self.arch_widgets_list)}")
        self.arch_widgets_count_label.setFont(self.count_labels_font)
        self.arch_widgets_count_label.setStyleSheet("color: red")
        
        self.dev_widgets_count_label = QLabel(f"Dev Widgets:\n  {len(self.dev_widgets_list)}")
        self.dev_widgets_count_label.setFont(self.count_labels_font)
        self.dev_widgets_count_label.setStyleSheet("color: red")
        
        # group widgets by
        self.group_widget_vbox = QVBoxLayout()
        self.group_widget_label = QLabel("Group By")
        
        self.group_widget_cb = QComboBox()
        self.group_widget_cb.addItem("Select Grouping Type")
        self.group_widget_cb.addItem("Widget Type")
        self.group_widget_cb.addItem("Developer")
        self.group_widget_cb.addItem("Status")
        
        self.group_widget_cb.currentIndexChanged.connect(self.index_changed_group_widget_cb)
        
        self.group_widget_vbox.addWidget(self.group_widget_label)
        self.group_widget_vbox.addWidget(self.group_widget_cb)
        
        # sort widgets by
        self.sort_widget_vbox = QVBoxLayout()
        self.sort_widget_label = QLabel("Sort By")
        
        self.sort_widget_cb = QComboBox()
        self.sort_widget_cb.addItem("Select Sorting Type")
        self.sort_widget_cb.addItem("Widget Type")
        self.sort_widget_cb.addItem("Developer")
        self.sort_widget_cb.addItem("Status")
        
        self.sort_widget_cb.currentIndexChanged.connect(self.index_changed_sort_widget_cb)
        
        self.sort_widget_vbox.addWidget(self.sort_widget_label)
        self.sort_widget_vbox.addWidget(self.sort_widget_cb)
        
        # filter by widget type section
        self.widget_type_vbox = QVBoxLayout()
        self.widget_type_label = QLabel("Filter by Widget Type")
        
        self.all_widget_types = os.listdir(widget_templates_dir)
        self.widget_type_cb = QComboBox()
        self.widget_type_cb.addItem("Select Widget Type")
        self.widget_type_cb.addItems(self.all_widget_types)
        
        self.widget_type_vbox.addWidget(self.widget_type_label)
        self.widget_type_vbox.addWidget(self.widget_type_cb)
        
        # filter by developer section
        self.developer_vbox = QVBoxLayout()
        self.developer_label = QLabel("Filter by Developer")
        
        self.developer_cb = QComboBox()
        self.developer_cb.addItem("Select Developer")
        self.developer_cb.addItems(all_developers)
        
        self.developer_cb.currentIndexChanged.connect(self.index_changed_developer_cb)
        
        self.developer_vbox.addWidget(self.developer_label)
        self.developer_vbox.addWidget(self.developer_cb)
        
        # filter by status section
        self.status_vbox = QVBoxLayout()
        self.status_label = QLabel("Filter by Status")
        
        self.status_cb = QComboBox()
        self.status_cb.addItem("Select Status")
        self.status_cb.addItems(WIDGET_STATUS_LIST)
        
        self.status_cb.currentIndexChanged.connect(self.index_changed_status_cb)
        
        self.status_vbox.addWidget(self.status_label)
        self.status_vbox.addWidget(self.status_cb)
        
        # search widgets line edit
        self.widget_search_box = QLineEdit("Search")
        
        # reset filters button
        self.reset_filters_button = QPushButton()
        self.reset_filters_button.setIcon(QIcon(qt_icon("reset.png")))
        self.reset_filters_button.clicked.connect(self.clicked_reset_filters)
        
        # load/apply filters button
        self.load_button = QPushButton("Load")
        self.load_button.clicked.connect(self.clicked_load_button)
        
        # light/dark mode switch button
        self.light_mode = True
        self.light_dark_mode_button = QPushButton()
        self.light_dark_mode_button.setIcon(QIcon(qt_icon("mode.png")))
        self.light_dark_mode_button.clicked.connect(self.clicked_light_dark_mode_switch)
        
        # add widgets to filters layout
        self.filters_hbox.addWidget(self.all_widgets_button)
        self.filters_hbox.addWidget(self.dev_widgets_count_label)
        self.filters_hbox.addWidget(self.arch_widgets_count_label)
        self.filters_hbox.addWidget(self.all_widgets_count_label)
        self.filters_hbox.addStretch()
        self.filters_hbox.addLayout(self.group_widget_vbox)
        self.filters_hbox.addLayout(self.sort_widget_vbox)
        self.filters_hbox.addLayout(self.widget_type_vbox)
        self.filters_hbox.addLayout(self.developer_vbox)
        self.filters_hbox.addLayout(self.status_vbox)
        self.filters_hbox.addStretch()
        self.filters_hbox.addWidget(self.widget_search_box)
        self.filters_hbox.addWidget(self.reset_filters_button)
        self.filters_hbox.addWidget(self.load_button)
        self.filters_hbox.addWidget(self.light_dark_mode_button)
        
        # ------------------------------------------------------
        
        # all widgets tab
        self.thumbnail_layout = QHBoxLayout()
        self.thumbnail_widget = ThumbnailViewerWidget()
        self.thumbnail_widget.scroll_area_qwidget.setStyleSheet("background-color: #e8e8e8; color: #212121")
        self.thumbnail_layout.addWidget(self.thumbnail_widget)

        # archived widgets tab
        self.archive_layout = QHBoxLayout()
        self.archive_widget = ThumbnailViewerWidget()
        self.archive_widget.scroll_area_qwidget.setStyleSheet("background-color: #e8e8e8; color: #212121")
        self.archive_layout.addWidget(self.archive_widget)

        # dev widgets tab
        self.widget_dev_layout = QHBoxLayout()
        self.widget_dev_widget = ThumbnailViewerWidget()
        self.widget_dev_widget.scroll_area_qwidget.setStyleSheet("background-color: #e8e8e8; color: #212121")
        self.widget_dev_layout.addWidget(self.widget_dev_widget)
  
        # ------------------------------------------------------
        # Viewer Tab's  ( Thumbnail View - Archive View ) TABS
        self.viewer_tab_widget = QTabWidget()
        
        tab_1 = QWidget()
        tab_2 = QWidget()
        tab_3 = QWidget()

        tab_1.setLayout(self.widget_dev_layout)
        tab_2.setLayout(self.archive_layout)
        tab_3.setLayout(self.thumbnail_layout)

        self.viewer_tab_widget.addTab(tab_1, "Dev Widgets")
        self.viewer_tab_widget.addTab(tab_2, "Archived Widgets")
        self.viewer_tab_widget.addTab(tab_3, "All Widgets")
        self.viewer_tab_widget.currentChanged.connect(self.tab_changed)

        # add widgets to master layout
        self.master_vbox.addLayout(self.filters_hbox)
        self.master_vbox.addWidget(self.viewer_tab_widget)

        self.setLayout(self.master_vbox)
        self.showMaximized()
        
        self.dev_widget_objects_dict = {}
        self.arch_widget_objects_dict = {}
        self.all_widget_objects_dict = {}
        
        self.dev_thread = QThread(self)
        self.dev_thread.start()
        self.dev_worker = Worker()
        self.dev_worker.moveToThread(self.dev_thread)
        self.load_dev_widget_objects.connect(self.dev_worker.get_widget_objects_dict)
        self.load_dev_widget_objects.emit(dev_widgets_src_dir, self.dev_widgets_list)
        self.dev_worker.complete.connect(self.dev_thread_complete)
        
        self.arch_thread = QThread(self)
        self.arch_thread.start()
        self.arch_worker = Worker()
        self.arch_worker.moveToThread(self.arch_thread)
        self.load_arch_widget_objects.connect(self.arch_worker.get_widget_objects_dict)
        self.arch_worker.complete.connect(self.arch_thread_complete)
        
        self.all_thread = QThread(self)
        self.all_thread.start()
        self.all_worker = Worker()
        self.all_worker.moveToThread(self.all_thread)
        self.load_all_widget_objects.connect(self.all_worker.get_widget_objects_dict)
        self.all_worker.complete.connect(self.all_thread_complete)
        
        
    @Slot(dict)
    def dev_thread_complete(self, obj_dict):
        self.dev_widget_objects_dict = obj_dict
        self.dev_widgets_count_label.setStyleSheet("color: green")
        self.all_widgets_button.setEnabled(True)
        print(f"Dev: {self.dev_thread.isFinished()}")
        self.dev_thread.quit()
        self.dev_thread.wait()
        self.dev_thread.terminate()
        print(f"Dev: {self.dev_thread.isFinished()}")
        
    @Slot(dict)
    def arch_thread_complete(self, obj_dict):
        self.arch_widget_objects_dict = obj_dict
        self.arch_widgets_count_label.setStyleSheet("color: green")
        self.all_widgets_button.setEnabled(True)
        print(f"Arch: {self.arch_thread.isFinished()}")
        self.arch_thread.quit()
        self.arch_thread.wait()
        self.arch_thread.terminate()
        print(f"Arch: {self.arch_thread.isFinished()}")
        
    @Slot(dict)
    def all_thread_complete(self, obj_dict):
        self.all_widget_objects_dict = obj_dict
        self.all_widgets_count_label.setStyleSheet("color: green")
        self.all_widgets_button.setEnabled(True)
        print(f"All: {self.all_thread.isFinished()}")
        self.all_thread.quit()
        self.all_thread.wait()
        self.all_thread.terminate()
        print(f"All: {self.all_thread.isFinished()}")

        
    @Slot(str)
    def _on_error(self, error):
        print(error)
        
        
    def clicked_show_all_widgets(self):
        if self.viewer_tab_widget.currentIndex() == 0:
            for widget_obj in self.dev_widget_objects_dict.values():
                self.widget_dev_widget.scroll_area_layout.addWidget(widget_obj)
        elif self.viewer_tab_widget.currentIndex() == 1:
            for widget_obj in self.arch_widget_objects_dict.values():
                self.archive_widget.scroll_area_layout.addWidget(widget_obj)
        elif self.viewer_tab_widget.currentIndex() == 2:
            for widget_obj in self.all_widget_objects_dict.values():
                self.thumbnail_widget.scroll_area_layout.addWidget(widget_obj)
        
        
    def clicked_reset_filters(self):
        print("Clicked Reset Filters")
        
    def clicked_load_button(self):
        print("Clicked Load Button")
        
    def index_changed_group_widget_cb(self):
        print("Group index changed")
        
    def index_changed_sort_widget_cb(self):
        print("Sort index changed")
        
    def index_changed_developer_cb(self):
        print("Developer index changed")
        
    def index_changed_status_cb(self):
        print("Status index changed")
        
    def tab_changed(self, index):
        if index == 0:
            self.load_dev_widget_objects.emit(dev_widgets_src_dir, self.dev_widgets_list)
        elif index == 1:
            self.load_arch_widget_objects.emit(arch_widgets_src_dir, self.arch_widgets_list)
        elif index == 2:
            self.load_all_widget_objects.emit(all_widgets_src_dir, self.all_widgets_list)
        
    def clicked_light_dark_mode_switch(self):
        '''
        Called when light/dark mode button is clicked. Switched background of scroll area of each tab between light and dark mode
        '''
        if self.light_mode:
            self.thumbnail_widget.scroll_area_qwidget.setStyleSheet("background-color: #212121; color: #e8e8e8")
            self.archive_widget.scroll_area_qwidget.setStyleSheet("background-color: #212121; color: #e8e8e8")
            self.widget_dev_widget.scroll_area_qwidget.setStyleSheet("background-color: #212121; color: #e8e8e8")
            self.light_mode = False
        else:
            self.thumbnail_widget.scroll_area_qwidget.setStyleSheet("background-color: #e8e8e8; color: #212121")
            self.archive_widget.scroll_area_qwidget.setStyleSheet("background-color: #e8e8e8; color: #212121")
            self.widget_dev_widget.scroll_area_qwidget.setStyleSheet("background-color: #e8e8e8; color: #212121")
            self.light_mode = True
    
    def _get_widgets_dict(self, widgets_src_dir):
        '''
        Returns dict of all widgets in the WIDGETS folder. For example:
        {
            ESH: [ESH_001, ESH_002, ESH_003,..........]
            HJH: [HJH_001. HJH_002, HJH_003,..........]
        }
        '''
        seq_list = os.listdir(widgets_src_dir)
        seq_list.remove(".gitkeep")
        widgets_dict = {}
        for seq in seq_list:
            widgets_in_seq = os.listdir(os.path.join(widgets_src_dir, seq))
            widgets_dict[seq] = widgets_in_seq
    
        return widgets_dict
    
    def _flatten_dict_to_list(self, dict):
        '''
        Returns list of all values from dict into a single list. For example:
        dict = {
            ESH: [ESH_001, ESH_002, ESH_003]
            HJH: [HJH_001, HJH_002, HJH_003]
        }
        
        list = [ESH_001, ESH_002, ESH_003, HJH_001, HJH_002, HJH_003]
        '''
        list = []
        for each_dict_value in dict.values():
            for value in each_dict_value:
                list.append(value)
                
        return list

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PreviewAppWidget()
    main_window.show()
    app.exec_()
