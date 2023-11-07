from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QComboBox, QListWidget, QListWidgetItem, QHBoxLayout, QMenu
from PySide2.QtCore import Qt, Signal
import os
import sys
import importlib.util

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
        self.view_all.clicked.connect(self.populate_all_widgets)
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
        # getting folder names dynamically from the WIDGETS directory
        developer_tags = [folder for folder in os.listdir(self.widgets_path) if os.path.isdir(os.path.join(self.widgets_path, folder))]
        self.combobox.addItems(developer_tags)

    def populate_listWidget(self):
        widgetFolders = self.get_widgetFolders()  

        self.list_widget.clear()  # Clears existing items

        for folder_name in widgetFolders:
            custom_widget = self.create_customWidget(self.combobox.currentText(), folder_name)
            list_item = QListWidgetItem()
            list_item.setSizeHint(custom_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_widget)

    def load_widgetUI(self, ui_filepath):
        def action():
            widgetUI_file = os.path.splitext(os.path.basename(ui_filepath))[0]

            try:
                spec = importlib.util.spec_from_file_location(widgetUI_file, ui_filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                ui_class = getattr(module, widgetUI_file)
                ui_instance = ui_class()

                while self.contents_layout.count():
                    item = self.contents_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)

                self.contents_layout.addWidget(ui_instance)

            except Exception as e:
                print(f"Error: {e}")

        return action

    def get_widgetFolders(self, selected_devTag=None):
        if selected_devTag is None:
            selected_devTag = self.combobox.currentText()

        devDir_path = os.path.join(self.widgets_path, selected_devTag)

        folder_names = [f for f in os.listdir(devDir_path) if os.path.isdir(os.path.join(devDir_path, f))]

        return folder_names

    def create_customWidget(self, developer_tag, folder_name):
        customWidget_layout = QHBoxLayout()

        folder_button = QPushButton(folder_name)
        folder_button.setFlat(True)
        folder_button.setStyleSheet("text-align: left;")
        customWidget_layout.addWidget(folder_button)
        folder_button.clicked.connect(
            self.load_widgetUI(os.path.join(self.widgets_path, developer_tag, folder_name, "widget", "CustomWidget.py"))
        )

        status_button = QPushButton("None")
        status_button.setFlat(True)
        status_button.setStyleSheet("text-align: left;")
        customWidget_layout.addWidget(status_button)

        status_button.setContextMenuPolicy(Qt.CustomContextMenu)
        status_button.customContextMenuRequested.connect(lambda event, folder=folder_name, button=status_button: self.status_menu(event, folder, button))

        custom_widget = QWidget()
        custom_widget.setLayout(customWidget_layout)
        return custom_widget

    def status_menu(self, pos, folder, button):
        menu = QMenu(self)

        menu.addAction("wip", lambda: self.set_status(folder, button, "wip"))
        menu.addAction("submitted", lambda: self.set_status(folder, button, "submitted"))
        menu.addAction("review", lambda: self.set_status(folder, button, "review"))
        menu.addAction("approved", lambda: self.set_status(folder, button, "approved"))

        menu.exec_(button.mapToGlobal(pos))

    def set_status(self, folder, button, status):
        print(f"Setting status of {folder} to {status}")
        button.setText(f"{status}")

    def populate_all_widgets(self):
        self.list_widget.clear()

        all_folders = []
        for developer_tag in os.listdir(self.widgets_path):
            developer_path = os.path.join(self.widgets_path, developer_tag)
            if os.path.isdir(developer_path):
                all_folders.extend([os.path.join(developer_tag, folder) for folder in os.listdir(developer_path) if os.path.isdir(os.path.join(developer_path, folder))])

        for folder_name in all_folders:
            developer_tag, folder = os.path.split(folder_name)
            custom_widget = self.create_customWidget(developer_tag, folder)
            list_item = QListWidgetItem()
            list_item.setSizeHint(custom_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_widget)

def main():
    app = QApplication([])
    main_window = dviewer()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
