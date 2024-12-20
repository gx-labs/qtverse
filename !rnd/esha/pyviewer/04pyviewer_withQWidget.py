import os
import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QHBoxLayout, QWidget
import importlib.util

class pyviewer(QWidget):
    def __init__(self):
        super().__init__()

        # main layout
        self.setWindowTitle('pyviewer')
        self.setFixedSize(1200,800)
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # tree widget
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setFixedSize(250,800)
        main_layout.addWidget(self.tree_widget)
        self.tree_widget.setHeaderLabels(['pyviewer'])
        self.tree_widget.itemDoubleClicked.connect(self.on_itemDoubleClicked)

        # content widget to display UI instances
        self.content_widget = QWidget(self)
        main_layout.addWidget(self.content_widget)
        self.content_layout = QHBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        self.root_path = 'qtverse\widgets\src\WIDGETS'
        self.item_actions = {}   # storing actions associated with tree items

        self.tree_items(self.root_path, self.tree_widget)

    def tree_items(self, path, parent):   # recursively populating the tree widget with items
        for entry in os.listdir(path):   # loops over entries in the current directory
            entry_path = os.path.join(path, entry)

            if os.path.isdir(entry_path) and not entry.endswith("__pycache__"): # creates parent item and calls tree_items recursively for the subdirectory
                parentItem = QTreeWidgetItem(parent)
                parentItem.setText(0, entry)
                self.tree_items(entry_path, parentItem)

            elif entry.endswith('.py'): # creates a child item
                child = QTreeWidgetItem(parent)
                child.setText(0, entry)
                self.item_actions[entry] = self.action_function(entry, path) # associates action with the child item

    def action_function(self, filename, parent_path):    
        def action():
            class_name = os.path.splitext(filename)[0] # extracting the class name 
            module_path = os.path.join(parent_path, f'{class_name.lower()}.py') # constructing the module path 

            try:
                spec = importlib.util.spec_from_file_location(class_name, module_path)
                module = importlib.util.module_from_spec(spec)  # creates an empty module
                spec.loader.exec_module(module) # executes the module 

                ui_class = getattr(module, class_name)
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
        filename = item.text(0)
        action = self.item_actions.get(filename)
        if action:
            action()

def main():
    app = QApplication([])
    main_window = pyviewer()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
