"""
auto population of data in tree widget 
"""
import os
import sys
import importlib
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

class pyviewer(QWidget):
    def __init__(self):
        super().__init__()

        # main layout
        self.setWindowTitle('pyviewer')
        self.setFixedSize(1000, 800)
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # tree widget
        self.tree_widget = QTreeWidget(self)
        main_layout.addWidget(self.tree_widget)
        self.tree_widget.setHeaderLabels([''])
        self.tree_widget.itemClicked.connect(self.on_itemClicked)

        self.root_path = 'C:\\pyviewer'
        self.item_actions = {}

        self.tree_items()

    def tree_items(self):
        for parentItem, subItem, filenames in os.walk(self.root_path):
            parent = QTreeWidgetItem(self.tree_widget)
            parent.setText(0, os.path.basename(parentItem))
            for filename in filenames:
                if filename.endswith('.py'):
                    child = QTreeWidgetItem(parent)
                    child.setText(0, filename)
                    self.item_actions[filename] = self.create_action_function(filename, parentItem)

    def create_action_function(self, filename, parentItem):
        def action():
            class_name = os.path.splitext(filename)[0]
            module_path = f'pyviewer.{parentItem}.{class_name.lower()}'
            module = importlib.import_module(module_path)
            ui_class = getattr(module, class_name)
            ui_instance = ui_class()
            ui_instance.show()

        return action

    def on_itemClicked(self, item, column):
        filename = os.path.basename(item.text(0))
        action = self.item_actions.get(filename)
        if action:
            action()

def main():
    app = QApplication([])
    main = pyviewer()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()