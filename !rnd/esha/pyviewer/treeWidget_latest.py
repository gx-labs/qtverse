from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout, QComboBox, QPushButton, QHBoxLayout, QScrollArea
from PySide2.QtCore import Qt
import os
import sys
import importlib.util

class Status:
    ALL = "ALL"
    WIP = "wip"
    SUBMITTED = "submitted"
    REVIEW = "review"
    APPROVED = "approved"

class dviewer(QWidget):
    # variable to store widget status
    widget_status = {}

    def __init__(self):
        super().__init__()

        # main layout
        self.setWindowTitle('dviewer')
        self.setFixedSize(1200, 800)
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # viewer widget
        self.viewer = QWidget(self)
        self.viewer.setFixedSize(320, 800)
        main_layout.addWidget(self.viewer)
        self.viewer_layout = QVBoxLayout(self.viewer)

        # combobox
        self.combobox = QComboBox()
        self.combobox.currentIndexChanged.connect(self.update_tree_visibility)
        self.viewer_layout.addWidget(self.combobox, alignment=Qt.AlignLeft)

        # status buttons
        self.statusBtn_layout = QHBoxLayout()
        self.viewer_layout.addLayout(self.statusBtn_layout)

        self.view_all = QPushButton("ALL")
        self.statusBtn_layout.addWidget(self.view_all)
        self.wip = QPushButton("wip")
        self.statusBtn_layout.addWidget(self.wip)
        self.submitted = QPushButton("submitted")
        self.statusBtn_layout.addWidget(self.submitted)
        self.review = QPushButton("review")
        self.statusBtn_layout.addWidget(self.review)
        self.approved = QPushButton("approved")
        self.statusBtn_layout.addWidget(self.approved)

        # Connect status buttons to filter functions
        self.view_all.clicked.connect(lambda: self.filter_widgets(Status.ALL))
        self.wip.clicked.connect(lambda: self.filter_widgets(Status.WIP))
        self.submitted.clicked.connect(lambda: self.filter_widgets(Status.SUBMITTED))
        self.review.clicked.connect(lambda: self.filter_widgets(Status.REVIEW))
        self.approved.clicked.connect(lambda: self.filter_widgets(Status.APPROVED))

        # tree widget
        self.tree_scroll_area = QScrollArea(self)
        self.tree_scroll_area.setWidgetResizable(True)
        self.viewer_layout.addWidget(self.tree_scroll_area)

        self.tree_widget = QTreeWidget()
        self.tree_scroll_area.setWidget(self.tree_widget)
        self.tree_widget.setFixedSize(300, 800)
        self.tree_widget.setHeaderLabels([''])
        self.tree_widget.itemDoubleClicked.connect(self.on_itemDoubleClicked)

        # content widget to display UI instances
        self.content_widget = QWidget(self)
        main_layout.addWidget(self.content_widget)
        self.content_layout = QHBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
 
        # path to WIDGETS folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir,'..','..'))

        self.widget_path = os.path.join(project_dir,"qtverse", "widgets","src","WIDGETS")
              
        self.tree_items(self.widget_path, self.tree_widget)

        # Set all items of the tree widget to be expanded
        self.expand_all_items(self.tree_widget.invisibleRootItem())

        # Populate combobox with top-level headers
        for i in range(self.tree_widget.topLevelItemCount()):
            item = self.tree_widget.topLevelItem(i)
            header_text = item.text(0)
            self.combobox.addItem(header_text)

    def tree_items(self, path, parent, status=Status.ALL):
        for entry in os.listdir(path):
            widget_filepath = os.path.join(path, entry)

            if os.path.isdir(widget_filepath) and not entry.endswith("__pycache__"):
                parentItem = QTreeWidgetItem(parent)
                parentItem.setText(0, entry)
                self.tree_items(widget_filepath, parentItem, status)
                parentItem.setExpanded(True)

            elif entry.endswith('.py'):
                child = QTreeWidgetItem(parent)
                child.setText(0, entry)
                action = self.action_function(widget_filepath)
                child.setData(0, 1, action)
                # Set status for each widget
                dviewer.widget_status[child] = status

    def update_tree_visibility(self, index):
        selected_item_text = self.combobox.itemText(index)
        for i in range(self.tree_widget.topLevelItemCount()):
            item = self.tree_widget.topLevelItem(i)
            item.setHidden(item.text(0) != selected_item_text)

    def action_function(self, widget_filepath):
        def action():
            file_name = os.path.splitext(os.path.basename(widget_filepath))[0]

            try:
                spec = importlib.util.spec_from_file_location(file_name, widget_filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                ui_class = getattr(module, file_name)
                ui_instance = ui_class()

                while self.content_layout.count():
                    item = self.content_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)

                self.content_layout.addWidget(ui_instance)

            except Exception as e:
                print(f"Error: {e}")

        return action

    def on_itemDoubleClicked(self, item, column):
        action = item.data(0, 1)
        if action:
            action()

    def expand_all_items(self, item):
        item.setExpanded(True)
        for i in range(item.childCount()):
            child_item = item.child(i)
            self.expand_all_items(child_item)

    def filter_widgets(self, status):
        for i in range(self.tree_widget.topLevelItemCount()):
            item = self.tree_widget.topLevelItem(i)
            item_status = dviewer.widget_status.get(item, Status.ALL)

            if status == Status.ALL or item_status == status:
                item.setHidden(False)
            else:
                item.setHidden(True)

def main():
    app = QApplication([])
    main_window = dviewer()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
