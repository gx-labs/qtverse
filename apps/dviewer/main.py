from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import importlib.util 
import yaml

class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, text='', parent=None):
        super(ClickableLabel, self).__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super(ClickableLabel, self).mousePressEvent(event)

class CustomWidget(QWidget):
    folderClicked = Signal(str)

    def __init__(self, name, path):
        super().__init__()

        self.folder_path = path

        self.main_layout = QHBoxLayout(self)

        # Foldername label
        self.foldername_label = ClickableLabel(name)
        self.main_layout.addWidget(self.foldername_label)

        # Category label
        self.category_label = QLabel()
        self.main_layout.addWidget(self.category_label)

        # Status label
        self.status_label = QLabel()
        self.main_layout.addWidget(self.status_label)

        # Add context menu to the custom widget
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # get status of Custom Widget from info.yaml                                
        info_yaml_file_path = os.path.join(self.folder_path, "info.yaml")                        
        if os.path.exists(info_yaml_file_path):
            with open(info_yaml_file_path, 'r') as file:
                info_data = yaml.safe_load(file)

            category = info_data.get('category')
            status = info_data.get('status')

            self.category_label.setText(f"{category}")
            self.status_label.setText(f"{status}")

    def show_context_menu(self, position):
        menu = QMenu(self)

        # Create actions for the context menu
        wip_action = QAction("wip", self)
        submitted_action = QAction("submitted", self)
        review_action = QAction("review", self)
        approved_action = QAction("approved", self)

        # Connect actions to update info.yaml and the displayed status label
        wip_action.triggered.connect(lambda: self.update_yaml("wip"))
        submitted_action.triggered.connect(lambda: self.update_yaml("submitted"))
        review_action.triggered.connect(lambda: self.update_yaml("review"))
        approved_action.triggered.connect(lambda: self.update_yaml("approved"))

        # Add actions to the menu
        menu.addAction(wip_action)
        menu.addAction(submitted_action)
        menu.addAction(review_action)
        menu.addAction(approved_action)

        # Show the context menu
        menu.exec_(self.mapToGlobal(position))

    def update_yaml(self, new_status):
        info_yaml_file_path = os.path.join(self.folder_path, "info.yaml")
        if os.path.exists(info_yaml_file_path):
            with open(info_yaml_file_path, 'r') as file:
                info_data = yaml.safe_load(file)

            # Update the status in the info data
            info_data['status'] = new_status

            # Write the updated info data back to the info.yaml file
            with open(info_yaml_file_path, 'w') as file:
                yaml.dump(info_data, file)

            # Update the displayed status label
            self.status_label.setText(f"{new_status}")

class dviewer(QWidget):
    def __init__(self):
        super().__init__()

        # main layout
        self.setWindowTitle("dviewer")
        self.setFixedSize(1200, 800)
        self.main_layout = QHBoxLayout(self)
        self.setLayout(self.main_layout)

        # viewer widget
        self.viewer = QWidget(self)
        self.viewer.setFixedSize(320, 800)
        self.main_layout.addWidget(self.viewer)
        self.viewer_layout = QVBoxLayout(self.viewer)

        # groupbox 
        self.groupbox =QGroupBox()
        self.viewer_layout.addWidget(self.groupbox, alignment=Qt.AlignLeft)  
       
        # ALL and Developer buttons 
        self.groupbox_layout = QHBoxLayout(self.groupbox)
        self.all_button = QPushButton("ALL")
        self.groupbox_layout.addWidget(self.all_button)
        self.all_button.clicked.connect(lambda: self.update_list_widget("ALL"))

        self.esh_button = QPushButton("ESH")
        self.groupbox_layout.addWidget(self.esh_button)
        self.esh_button.clicked.connect(lambda: self.update_list_widget("ESH"))

        self.prt_button = QPushButton("PRT")
        self.groupbox_layout.addWidget(self.prt_button)
        self.prt_button.clicked.connect(lambda: self.update_list_widget("PRT"))

        self.sam_button = QPushButton("SAM")
        self.groupbox_layout.addWidget(self.sam_button)
        self.sam_button.clicked.connect(lambda: self.update_list_widget("SAM"))

        self.shb_button = QPushButton("SHB")
        self.groupbox_layout.addWidget(self.shb_button)
        self.shb_button.clicked.connect(lambda: self.update_list_widget("SHB"))

        # status buttons
        self.statusButton_layout = QHBoxLayout()
        self.viewer_layout.addLayout(self.statusButton_layout)

        self.wip = QPushButton("wip")
        self.statusButton_layout.addWidget(self.wip)
        self.submitted = QPushButton("submitted")
        self.statusButton_layout.addWidget(self.submitted)
        self.review = QPushButton("review")
        self.statusButton_layout.addWidget(self.review)
        self.approved = QPushButton("approved")
        self.statusButton_layout.addWidget(self.approved)

        # list widget
        self.list_widget = QListWidget()
        self.list_widget.setFixedSize(300, 800)
        self.viewer_layout.addWidget(self.list_widget)

        # content widgets to display UI instances
        self.contents_widget = QWidget(self)
        self.main_layout.addWidget(self.contents_widget)
        self.contents_layout = QVBoxLayout(self.contents_widget)
        self.contents_layout.setContentsMargins(0, 0, 0, 0)

        # Set the root path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
        self.widgetsDir_path = os.path.join(project_dir, "qtverse", "widgets", "src", "WIDGETS")

        # Populate the QListWidget with folders based on the initial state (ALL)
        self.update_list_widget("ALL")

        # Connect the signal to the slot function
        self.list_widget.itemClicked.connect(self.on_item_clicked)

    def get_developer_folders(self):
        dev_folders = []
        for entry in os.scandir(self.widgetsDir_path):
            if entry.is_dir():
                dev_folders.append(entry.name)
        return dev_folders

    def get_widget_folders(self, dev_folder):
        widget_folders = {}

        # Get all folders in the specified main folder
        dev_folder_path = os.path.join(self.widgetsDir_path, dev_folder)
        if os.path.exists(dev_folder_path):
            for folder_name in os.listdir(dev_folder_path):
                folder_path = os.path.join(dev_folder_path, folder_name)
                if os.path.isdir(folder_path):
                    widget_folders[folder_name] = folder_path

        return widget_folders

    def update_list_widget(self, developer):
        # Store the currently selected developer
        self.current_developer = developer

        # Clear the list widget
        self.list_widget.clear()

        # Repopulate the list widget with widgets that match the selected developer
        dev_folders = self.get_developer_folders()
        for dev_folder in dev_folders:
            if self.current_developer == "ALL" or self.current_developer == dev_folder:
                widget_folders = self.get_widget_folders(dev_folder)
                for folder_name, folder_path in widget_folders.items():
                    custom_widget = CustomWidget(folder_name, folder_path)
                    list_item = QListWidgetItem()
                    list_item.setSizeHint(custom_widget.sizeHint())
                    self.list_widget.addItem(list_item)
                    self.list_widget.setItemWidget(list_item, custom_widget)

    def on_item_clicked(self, item):
        if isinstance(item, QListWidgetItem):
            widget_item = self.list_widget.itemWidget(item)
            if widget_item:
                self.load_widgetUI(widget_item.folder_path)

    def load_widgetUI(self, folder_path):
        # Implementing the logic to load the UI from the CustomWidget.py file
        
        # path to config.yaml file
        config_file_path = os.path.join(os.path.dirname(__file__), "config.yaml")

        # Read configuration from config.yaml
        with open(config_file_path, "r") as config_file:
            config = yaml.safe_load(config_file)

        # Extract folder and file information from the config
        widget_foldername = config.get("widget_foldername", "widget")
        widget_filename = config.get("widget_filename", "CustomWidget.py")

         # Construct the path to the widget Python file
        widget_py_path = os.path.join(folder_path, widget_foldername, widget_filename)

        if os.path.exists(widget_py_path):
            try:
                widget_filename = os.path.splitext(os.path.basename(widget_py_path))[0]

                spec = importlib.util.spec_from_file_location(widget_filename, widget_py_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                ui_class = getattr(module, widget_filename)
                ui_instance = ui_class()

                while self.contents_layout.count():
                    item = self.contents_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)

                self.contents_layout.addWidget(ui_instance)

            except Exception as e:
                print(f"Error: {e}")

def main():
    app = QApplication([])
    main_window = dviewer()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()

