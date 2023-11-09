from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QPushButton, QComboBox, QApplication, QMenu, QAction
from PySide2.QtCore import Qt, Signal
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

        # Status label
        self.status_label = QLabel()
        #TODO: set text, fetch from yaml file, if var not found set default label as None 
        self.main_layout.addWidget(self.status_label)

        # Add context menu to the custom widget
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        menu = QMenu(self)

        # Create actions for the context menu
        wip_action = QAction("wip", self)
        submitted_action = QAction("submitted", self)
        review_action = QAction("review", self)
        approved_action = QAction("approved", self)

        # Connect actions to update_status function
        wip_action.triggered.connect(lambda: self.update_status("wip"))
        submitted_action.triggered.connect(lambda: self.update_status("submitted"))
        review_action.triggered.connect(lambda: self.update_status("review"))
        approved_action.triggered.connect(lambda: self.update_status("approved"))

        # Add actions to the menu
        menu.addAction(wip_action)
        menu.addAction(submitted_action)
        menu.addAction(review_action)
        menu.addAction(approved_action)

        # Show the context menu
        menu.exec_(self.status_label.mapToGlobal(position))

    def update_status(self, status):
        self.status_label.setText(status)
      #TODO: update the status in the yaml file with the changes made in the ui 

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

        # combobox
        self.combobox = QComboBox()
        self.viewer_layout.addWidget(self.combobox, alignment=Qt.AlignLeft)

        # status buttons
        self.statusButton_layout = QHBoxLayout()
        self.viewer_layout.addLayout(self.statusButton_layout)

        self.view_all = QPushButton("ALL")
        self.statusButton_layout.addWidget(self.view_all)
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

        # Populate the QListWidget with folders
        self.populate_tree_widget()

        # Connect the signal to the slot function
        self.list_widget.itemClicked.connect(self.on_item_clicked)

    def get_developer_folders(self):
        """
           ["ESH", "PRT", "SHB", "SMB"]
        """
        dev_folders = []
        for entry in os.scandir(self.widgetsDir_path):
            if entry.is_dir():
                dev_folders.append(entry.name)
        return dev_folders

    def get_widget_folders(self, dev_folder):
        """
           {
           'ESH_001': 'c:\\PROJECTS\\PySide\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_001', 
           'ESH_002': 'c:\\PROJECTS\\PySide\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_002', 
           'ESH_003': 'c:\\PROJECTS\\PySide\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_003', 
           'ESH_004': 'c:\\PROJECTS\\PySide\\qtverse\\qtverse\\widgets\\src\\WIDGETS\\ESH\\ESH_004'
           }
        """
        widget_folders = {}

        # Get all folders in the specified main folder
        dev_folder_path = os.path.join(self.widgetsDir_path, dev_folder)
        if os.path.exists(dev_folder_path):
            for folder_name in os.listdir(dev_folder_path):
                folder_path = os.path.join(dev_folder_path, folder_name)
                if os.path.isdir(folder_path):
                    widget_folders[folder_name] = folder_path

        return widget_folders

    def populate_tree_widget(self):
        dev_folders = self.get_developer_folders()

        self.list_widget.clear()  # Clear existing items

        for dev_folder in dev_folders:
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
