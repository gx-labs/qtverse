from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
import os
import sys

class CustomWidget(QWidget):
    def __init__(self, path):
        super().__init__()
        
        # custom widget to add in the list widget
        customWidget_layout = QVBoxLayout(self)
        foldername_label = QLabel(os.path.basename(path))  
        customWidget_layout.addWidget(foldername_label)

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
        self.view_all.clicked.connect(self.list_allWidgets)  
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

        # Set the path to WIDGETS directory 
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
        self.widgets_path = os.path.join(project_dir, "qtverse", "widgets", "src", "WIDGETS")

        # Populate combobox with folder names
        self.populate_combobox()

        # Connect combobox signal to slot
        self.combobox.currentIndexChanged.connect(self.populate_listWidget)

        # Populate list widget 
        self.populate_listWidget()

    def populate_combobox(self):
        # Get the folder names dynamically from the WIDGETS directory
        developer_tags = [folder for folder in os.listdir(self.widgets_path) if os.path.isdir(os.path.join(self.widgets_path, folder))]
        self.combobox.addItems(developer_tags)

    def populate_listWidget(self):
        widgetFolders = self.get_widgetFolders()

        self.list_widget.clear()  # Clear existing items

        for folder_name in widgetFolders:
            custom_widget = CustomWidget(os.path.join(self.widgets_path, folder_name))
            list_item = QListWidgetItem()
            list_item.setSizeHint(custom_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_widget)

    def list_allWidgets(self):
        self.list_widget.clear()  # Clear existing items
        all_folders = []

        for idx in range(self.combobox.count()):
            all_folders.extend(self.get_widgetFolders(self.combobox.itemText(idx)))

        for folder_name in all_folders:
            custom_widget = CustomWidget(os.path.join(self.widgets_path, folder_name))
            list_item = QListWidgetItem()
            list_item.setSizeHint(custom_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_widget)

    def get_widgetFolders(self, selected_devTag=None):
        # Get folder names based on the combobox selection
        if selected_devTag is None:
            selected_devTag = self.combobox.currentText()

        devDir_path = os.path.join(self.widgets_path, selected_devTag)

        # Filter out non-directory items
        folder_names = [f for f in os.listdir(devDir_path) if os.path.isdir(os.path.join(devDir_path, f))]

        return folder_names

def main():
    app = QApplication([])
    main_window = dviewer()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

