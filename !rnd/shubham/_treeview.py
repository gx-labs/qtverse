import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

class TreeViewDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TreeView Styling Demo")
        self.setGeometry(100, 100, 600, 400)

        self.tree_view = QTreeWidget(self)
        self.tree_view.setGeometry(10, 10, 580, 380)

        self.tree_view.setHeaderLabels(["Item Name", "Description"])

        root_item = QTreeWidgetItem(self.tree_view, ["Root Item", "This is the root item"])
        child_item1 = QTreeWidgetItem(root_item, ["Child Item 1", "This is a child item"])
        child_item2 = QTreeWidgetItem(root_item, ["Child Item 2", "Another child item"])
        sub_child_item = QTreeWidgetItem(child_item1, ["Sub Child Item", "A sub-item"])

        style_sheet = """
            QTreeView {
                background-color: #f0f0f0;
                border: 2px solid #999999;
            }

            QTreeView::item {
                color: #333333;
                padding: 5px;
                border: 1px solid transparent;
            }

            QTreeView::item:selected {
                background-color: #3399ff;
                color: #ffffff;
            }

            QTreeView::item:hover {
                background-color: #cccccc;
            }
        """
        self.tree_view.setStyleSheet(style_sheet)

def main():
    app = QApplication(sys.argv)
    window = TreeViewDemo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
