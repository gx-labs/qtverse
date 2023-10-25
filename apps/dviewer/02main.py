import os
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import importlib.util

class pyviewer(QWidget):
    def __init__(self):
        super().__init__()

        # main layout
        self.setWindowTitle('dviewer')
        self.setFixedSize(1200, 800)
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # viewer widget
        self.viewer=QWidget(self)
        self.viewer.setFixedSize(320, 800)
        main_layout.addWidget(self.viewer)
        
        self.viewer_layout=QVBoxLayout(self.viewer)

        #combobox
        self.combobox = QComboBox()
        self.combobox.addItem("ESH")
        self.combobox.addItem("PRT")
        self.combobox.addItem("SAM")
        self.combobox.addItem("SHB")
        self.viewer_layout.addWidget(self.combobox, alignment=Qt.AlignLeft)

        #status buttons
        self.statusBtn_layout=QHBoxLayout()
        self.viewer_layout.addLayout(self.statusBtn_layout)
        
        self.view_all=QPushButton("ALL")
        self.statusBtn_layout.addWidget(self.view_all)
        self.wip=QPushButton("wip")
        self.statusBtn_layout.addWidget(self.wip)
        self.submitted=QPushButton("submitted")
        self.statusBtn_layout.addWidget(self.submitted)
        self.review=QPushButton("review")
        self.statusBtn_layout.addWidget(self.review)
        self.approved=QPushButton("approved")
        self.statusBtn_layout.addWidget(self.approved)

        # tree widget
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setFixedSize(300, 800)
        self.viewer_layout.addWidget(self.tree_widget)
        self.tree_widget.setHeaderLabels([''])
        self.tree_widget.itemDoubleClicked.connect(self.on_itemDoubleClicked)
        
        # content widget to display UI instances
        self.content_widget = QWidget(self)
        main_layout.addWidget(self.content_widget)
        self.content_layout = QHBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        self.root_path = 'C:\\PROJECTS\\PySide\\qtverse\\qtverse\\widgets\\src\\WIDGETS'
        self.tree_items(self.root_path, self.tree_widget)

    def tree_items(self, path, parent): # recursively populating the tree widget with items
        for entry in os.listdir(path): # loops over entries in the current directory
            widget_filepath = os.path.join(path, entry)

            if os.path.isdir(widget_filepath) and not entry.endswith("__pycache__"): # creates parent item and calls tree_items recursively for the subdirectory
                parentItem = QTreeWidgetItem(parent)
                parentItem.setText(0, entry)
                self.tree_items(widget_filepath, parentItem)

            elif entry.endswith('.py'): #create child item
                child = QTreeWidgetItem(parent)
                child.setText(0, entry)
                action = self.action_function(widget_filepath)
                child.setData(0, 1, action)  # Storing action function as item data

    def action_function(self, widget_filepath):    
        def action():
            file_name = os.path.splitext(os.path.basename(widget_filepath))[0]  # extracting the class name 

            try:
                spec = importlib.util.spec_from_file_location(file_name, widget_filepath)
                module = importlib.util.module_from_spec(spec)  # creates an empty module
                spec.loader.exec_module(module) # executes the module 

                ui_class = getattr(module, file_name)
                ui_instance = ui_class()

                # clears the content layout and add the new ui instance
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

def main():
    app = QApplication([])
    main_window = pyviewer()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
