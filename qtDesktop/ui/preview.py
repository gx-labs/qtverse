import os
import sys
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

class ThumbnailViewerWidget(QWidget):
    '''
    This class is the scroll area where all the widgets are populated. Each tab (all, archive and dev) have their own instance
    of this class
    '''
    def __init__(self):
        super(ThumbnailViewerWidget, self).__init__()
        
        # vars to load widgets 100 at a time (lazy loading)
        self.widget_load_start_index = 0
        self.widget_load_end_index = 99

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
    def __init__(self):
        super().__init__()
        
        # vars for storing dict of widgets according to seq
        self.all_widgets_dict = self._get_all_widgets_dict()
        self.arch_widgets_dict = self._get_arch_widgets_dict()
        self.dev_widgets_dict = self._get_dev_widgets_dict()
        
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
        self.all_widgets_button.clicked.connect(self.clicked_show_all_widgets)
        
        # labels to show count of all, archived and dev widgets
        self.count_labels_font = QFont()
        self.count_labels_font.setBold(True)
        self.count_labels_font.setPointSize(10)

        self.all_widgets_count_label = QLabel(f"All Widgets:\n  {len(self.all_widgets_list)}")
        self.all_widgets_count_label.setFont(self.count_labels_font)
        
        self.arch_widgets_count_label = QLabel(f"Arch. Widgets:\n   {len(self.arch_widgets_list)}")
        self.arch_widgets_count_label.setFont(self.count_labels_font)
        
        self.dev_widgets_count_label = QLabel(f"Dev Widgets:\n  {len(self.dev_widgets_list)}")
        self.dev_widgets_count_label.setFont(self.count_labels_font)
        
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
        self.filters_hbox.addWidget(self.all_widgets_count_label)
        self.filters_hbox.addWidget(self.arch_widgets_count_label)
        self.filters_hbox.addWidget(self.dev_widgets_count_label)
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
        self.viewer_tab_widget.currentChanged.connect(self._clear_scroll_area)
        
        tab_1 = QWidget()
        tab_2 = QWidget()
        tab_3 = QWidget()

        tab_1.setLayout(self.thumbnail_layout)
        tab_2.setLayout(self.archive_layout)
        tab_3.setLayout(self.widget_dev_layout)

        self.viewer_tab_widget.addTab(tab_1, "All Widgets")
        self.viewer_tab_widget.addTab(tab_2, "Archived Widgets")
        self.viewer_tab_widget.addTab(tab_3, "Dev Widgets")
        
        self.viewer_tab_widget.setCurrentIndex(2)

        # add widgets to master layout
        self.master_vbox.addLayout(self.filters_hbox)
        self.master_vbox.addWidget(self.viewer_tab_widget)

        self.setLayout(self.master_vbox)
        self.showMaximized()
        
        # lazy loading
        self.thumbnail_widget.scroll_area.verticalScrollBar().valueChanged.connect(self.update_widgets_to_load)
        self.archive_widget.scroll_area.verticalScrollBar().valueChanged.connect(self.update_widgets_to_load)
        self.widget_dev_widget.scroll_area.verticalScrollBar().valueChanged.connect(self.update_widgets_to_load)
        
    def clicked_show_all_widgets(self):
        print("Clicked Show All Widgets")
        
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

    def _import_ui_as_module(self, widget_filename, widget_py_path):
        spec = importlib.util.spec_from_file_location(widget_filename, widget_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        ui_class = getattr(module, widget_filename)
        ui_instance = ui_class()

        return ui_instance
    
    def _get_all_widgets_dict(self):
        '''
        Returns dict of all widgets in the WIDGETS folder. For example:
        {
            ESH: [ESH_001, ESH_002, ESH_003,..........]
            HJH: [HJH_001. HJH_002, HJH_003,..........]
        }
        '''
        all_seq_list = os.listdir(all_widgets_src_dir)
        all_seq_list.remove(".gitkeep")
        all_widgets_dict = {}
        for seq in all_seq_list:
            all_widgets_in_seq = os.listdir(os.path.join(all_widgets_src_dir, seq))
            all_widgets_dict[seq] = all_widgets_in_seq
    
        return all_widgets_dict
    
    def _get_arch_widgets_dict(self):
        '''
        Returns dict of all widgets in the WIDGETS_ARC folder. For example:
        {
            ESH: [ESH_001, ESH_002, ESH_003,..........]
            HJH: [HJH_001. HJH_002, HJH_003,..........]
        }
        '''
        arch_seq_list = os.listdir(arch_widgets_src_dir)
        arch_seq_list.remove(".gitkeep")
        arch_widgets_dict = {}
        for seq in arch_seq_list:
            arch_widgets_in_seq = os.listdir(os.path.join(arch_widgets_src_dir, seq))
            arch_widgets_dict[seq] = arch_widgets_in_seq
            
        return arch_widgets_dict
    
    def _get_dev_widgets_dict(self):
        '''
        Returns dict of all widgets in the WIDGETS_DEV folder. For example:
        {
            ESH: [ESH_001, ESH_002, ESH_003,..........]
            HJH: [HJH_001. HJH_002, HJH_003,..........]
        }
        '''
        dev_seq_list = os.listdir(dev_widgets_src_dir)
        dev_seq_list.remove(".gitkeep")
        dev_widgets_dict = {}
        for seq in dev_seq_list:
            dev_widgets_in_seq = os.listdir(os.path.join(dev_widgets_src_dir, seq))
            dev_widgets_dict[seq] = dev_widgets_in_seq
            
        return dev_widgets_dict
    
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

    def _get_widgets_list(self):
        '''
        Returns a list of all widgets depending on the tab selected (all, archived or dev)
        '''
        if (self.viewer_tab_widget.currentIndex() == 0):
            widgets_list = self.all_widgets_list
        if (self.viewer_tab_widget.currentIndex() == 1):
            widgets_list = self.arch_widgets_list
        if (self.viewer_tab_widget.currentIndex() == 2):
            widgets_list = self.dev_widgets_list

        return widgets_list
    
    def _get_widgets_path(self):
        '''
        Returns the path of the src directory of widgets based on tab selected (WIDGETS, WIDGETS_ARC or WIDGETS_DEV)
        '''
        if (self.viewer_tab_widget.currentIndex() == 0):
            widgets_path = all_widgets_src_dir
        if (self.viewer_tab_widget.currentIndex() == 1):
            widgets_path = arch_widgets_src_dir
        if (self.viewer_tab_widget.currentIndex() == 2):
            widgets_path = dev_widgets_src_dir
            
        return widgets_path
    
    def _get_widgets_tab(self):
        '''
        Returns the active tab (All, Archived or Dev)
        '''
        if (self.viewer_tab_widget.currentIndex() == 0):
            widgets_tab = self.thumbnail_widget
        elif (self.viewer_tab_widget.currentIndex() == 1):
            widgets_tab = self.archive_widget
        elif (self.viewer_tab_widget.currentIndex() == 2):
            widgets_tab = self.widget_dev_widget
            
        return widgets_tab
    
    def _clear_scroll_area(self):
        '''
        Removes all widgets populated in the scroll_area in the tab
        '''
        # resets the vars to track indices for lazy loading
        self.widget_load_start_index = 0
        self.widget_load_end_index = 99
        
        # delete each widget
        if (self.viewer_tab_widget.currentIndex() == 0):
            for i in range(self.thumbnail_widget.scroll_area_layout.count()):
                    self.thumbnail_widget.scroll_area_layout.itemAt(i).widget().deleteLater()
        elif (self.viewer_tab_widget.currentIndex() == 1):
            for i in range(self.archive_widget.scroll_area_layout.count()):
                    self.archive_widget.scroll_area_layout.itemAt(i).widget().deleteLater()
        elif (self.viewer_tab_widget.currentIndex() == 2):
            for i in range(self.widget_dev_widget.scroll_area_layout.count()):
                    self.widget_dev_widget.scroll_area_layout.itemAt(i).widget().deleteLater()
                  
        self.populate_widgets()
    
    def populate_widgets(self):
        '''
        Populates the scroll area of the tab based on which tab is selected and number of widgets.
        Implements lazy loading. Up to 100 widgets are loaded at first. If scrollbar hits its max range,
        100 more widgets are loaded.
        '''
        
        # set vars to track which widgets need to be populated (all, archived or dev)
        widgets_list = self._get_widgets_list()
        widgets_path = self._get_widgets_path()
        widgets_tab = self._get_widgets_tab()
        
        if widgets_list:
            # loop through the indices set for lazy loading (100 at a time)
            for index in range(widgets_tab.widget_load_start_index, widgets_tab.widget_load_end_index + 1):
                if(index < len(widgets_list)):
                    each_widget_name = widgets_list[index]
                    widget_seq_name = str(each_widget_name[:3])
                    each_widget_path = os.path.join(widgets_path, widget_seq_name, each_widget_name)

                    widget_py_path = os.path.join(each_widget_path, "widget", "CustomWidget.py")
                        
                    info_filepath = os.path.join(each_widget_path, "info.yaml")
                    info_dict = read_yaml(filepath=info_filepath)

                    css_filepath = os.path.join(each_widget_path, "widget", "style.css")
                    
                    # Catch FileNotFoundError and prevent app from crashing
                    try:
                        with open(css_filepath) as file:
                            css_data = file.read().replace('\n',' ')
                    except FileNotFoundError:
                        print(f"{each_widget_path} seems to be empty.")
                        pass
                        
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
                            height=100)
                            
                        widgets_tab.scroll_area_layout.addWidget(self.custom_thumbnail_widget)
                    else:
                        break
        else:
            font = QFont()
            font.setBold(True)
            font.setPointSize(20)
            no_widgets_label = QLabel("No Widgets Found")
            no_widgets_label.setFont(font)
            widgets_tab.scroll_area_layout.addWidget(no_widgets_label)

    
    def update_widgets_to_load(self):
        '''
        Updates the indices used to track which next 100 widgets to load
        '''
        
        # bool flag to check whether scrollbar has reached max value
        populate_more_widgets = False
        
        if self.viewer_tab_widget.currentIndex() == 0:
            scrollbar = self.thumbnail_widget.scroll_area.verticalScrollBar()
            if scrollbar.value() >= scrollbar.maximum():
                self.thumbnail_widget.widget_load_start_index += 100
                self.thumbnail_widget.widget_load_end_index += 100
                populate_more_widgets = True
                
        elif self.viewer_tab_widget.currentIndex() == 1:
            scrollbar = self.archive_widget.scroll_area.verticalScrollBar()
            if scrollbar.value() >= scrollbar.maximum():
                self.archive_widget.widget_load_start_index += 100
                self.archive_widget.widget_load_end_index += 100
                populate_more_widgets = True
                
        elif self.viewer_tab_widget.currentIndex() == 2:
            scrollbar = self.widget_dev_widget.scroll_area.verticalScrollBar()
            if scrollbar.value() >= scrollbar.maximum():
                self.widget_dev_widget.widget_load_start_index += 100
                self.widget_dev_widget.widget_load_end_index += 100
                populate_more_widgets = True
                
        # flag only true if scrollbar reached max value
        if populate_more_widgets:
            self.populate_widgets()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PreviewAppWidget()
    main_window.show()
    app.exec_()
