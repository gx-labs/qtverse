from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
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

    def __init__(self, name, path, status_color):
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
        self.status_label.setStyleSheet(f"color: {status_color};")
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
        self.viewer.setFixedSize(340, 800)
        self.main_layout.addWidget(self.viewer)
        self.viewer_layout = QVBoxLayout(self.viewer)

        # groupbox 
        self.groupbox =QGroupBox()
        self.viewer_layout.addWidget(self.groupbox, alignment=Qt.AlignLeft)  
       
        # ALL and Developer buttons 
        self.groupbox_layout = QHBoxLayout(self.groupbox)
        self.all_button = QPushButton("ALL")
        self.groupbox_layout.addWidget(self.all_button)
        self.all_button.clicked.connect(lambda: self.update_list_widget("ALL", self.current_status))

        self.esh_button = QPushButton("ESH")
        self.groupbox_layout.addWidget(self.esh_button)
        self.esh_button.clicked.connect(lambda: self.update_list_widget("ESH", self.current_status))

        self.prt_button = QPushButton("PRT")
        self.groupbox_layout.addWidget(self.prt_button)
        self.prt_button.clicked.connect(lambda: self.update_list_widget("PRT", self.current_status))

        self.sam_button = QPushButton("SAM")
        self.groupbox_layout.addWidget(self.sam_button)
        self.sam_button.clicked.connect(lambda: self.update_list_widget("SAM", self.current_status))

        self.shb_button = QPushButton("SHB")
        self.groupbox_layout.addWidget(self.shb_button)
        self.shb_button.clicked.connect(lambda: self.update_list_widget("SHB", self.current_status))

        # status buttons
        self.statusButton_layout = QHBoxLayout()
        self.viewer_layout.addLayout(self.statusButton_layout)

        self.wip = QPushButton("wip")
        self.wip.setFlat(True)
        self.wip.setFont(QFont("Arial", 11, QFont.Bold))
        self.wip.setStyleSheet("color: rgb(50, 193, 255 );") 
        self.statusButton_layout.addWidget(self.wip)
        self.wip.clicked.connect(lambda: self.update_list_widget(self.current_developer, "wip"))
        
        self.submitted = QPushButton("submitted")
        self.submitted.setFlat(True)
        self.submitted.setFont(QFont("Arial", 11, QFont.Bold))
        self.submitted.setStyleSheet("color: rgb(255, 191, 10 );") 
        self.statusButton_layout.addWidget(self.submitted)
        self.submitted.clicked.connect(lambda: self.update_list_widget(self.current_developer, "submitted"))
        
        self.review = QPushButton("review")
        self.review.setFlat(True)
        self.review.setFont(QFont("Arial", 11, QFont.Bold))
        self.review.setStyleSheet("color: rgb(255, 0, 127 );") 
        self.statusButton_layout.addWidget(self.review)
        self.review.clicked.connect(lambda: self.update_list_widget(self.current_developer, "review"))
        
        self.approved = QPushButton("approved")
        self.approved.setFlat(True)
        self.approved.setFont(QFont("Arial", 11, QFont.Bold))
        self.approved.setStyleSheet("color: rgb(0, 168, 107 );") 
        self.statusButton_layout.addWidget(self.approved)
        self.approved.clicked.connect(lambda: self.update_list_widget(self.current_developer, "approved"))

        # list widget
        self.list_widget = QListWidget()
        self.list_widget.setFixedSize(325, 800)
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

        # Initialize current developer and status
        self.current_developer = "ALL"
        self.current_status = "ALL"

        # Populate the QListWidget with folders based on the initial state (ALL)
        self.update_list_widget(self.current_developer, self.current_status)

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

    def update_list_widget(self, developer, status):
        # Store the currently selected developer and status
        self.current_developer = developer
        self.current_status = status

        # Clear the list widget
        self.list_widget.clear()

        # Define color mapping for statuses
        status_color_map = {
            "wip": "rgb(50, 193, 255)",
            "submitted": "rgb(255, 191, 10)",
            "review": "rgb(255, 0, 127)",
            "approved": "rgb(0, 168, 107)"
        }

        # Repopulate the list widget with widgets that match the selected developer and status
        dev_folders = self.get_developer_folders()
        for dev_folder in dev_folders:
            if self.current_developer == "ALL" or self.current_developer == dev_folder:
                widget_folders = self.get_widget_folders(dev_folder)
                for folder_name, folder_path in widget_folders.items():
                    # Read status from info.yaml
                    info_yaml_file_path = os.path.join(folder_path, "info.yaml")
                    if os.path.exists(info_yaml_file_path):
                        with open(info_yaml_file_path, 'r') as file:
                            info_data = yaml.safe_load(file)

                        folder_status = info_data.get('status')

                        # Check if the folder matches the selected status or status is "ALL"
                        if self.current_status == "ALL" or self.current_status == folder_status:
                            # Set the appropriate status color or default to black
                            status_color = status_color_map.get(folder_status, "black")

                            custom_widget = CustomWidget(folder_name, folder_path, status_color)
                            list_item = QListWidgetItem()
                            list_item.setSizeHint(custom_widget.sizeHint())
                            self.list_widget.addItem(list_item)
                            self.list_widget.setItemWidget(list_item, custom_widget)


    def on_item_clicked(self, item):
        if isinstance(item, QListWidgetItem):
            widget_item = self.list_widget.itemWidget(item)
            if widget_item:
                self.load_widget_UI(widget_item.folder_path)

    def load_widget_UI(self, folder_path):
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
