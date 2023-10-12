"""
auto population of data in tree widget and tried QTabWidget

"""

import sys
import os
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QHBoxLayout, QWidget, QTabWidget

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from psutilManager.psutilManager import psutilManager
from signupPage.signupPage import signupPage
from snippets.tabs import tabs
from snippets.stackedWidget import stackedWidget

class pyviewer(QWidget):
    def __init__(self):
        super().__init__()

        # main layout
        self.setWindowTitle('pyviewer')
        self.setFixedSize(1300, 800)
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # tree widget
        self.tree_widget = QTreeWidget(self)
        main_layout.addWidget(self.tree_widget)
        self.tree_widget.setHeaderLabels([''])
        self.tree_widget.itemClicked.connect(self.on_itemClicked)

        self.ui_tab = QTabWidget(self)
        main_layout.addWidget(self.ui_tab)

        self.item_actions = {
            'psutilManager.py': self.on_psutilManager,
            'signupPage.py': self.on_signupPage,
            'tabs.py': self.on_tabs,
            'stackedWidget.py': self.on_stackedWidget
        }

        self.tree_items()

    def tree_items(self):
        root_path = 'C:\\pyviewer'
        for foldername, subfolders, filenames in os.walk(root_path):
            parent = QTreeWidgetItem(self.tree_widget)
            parent.setText(0, os.path.basename(foldername))
            for filename in filenames:
                if filename.endswith('.py'):
                    child = QTreeWidgetItem(parent)
                    child.setText(0, filename)

    def execute_action(self, item_text):
        action = self.item_actions.get(item_text)
        if action:
            action()

    def on_psutilManager(self):
        self.psutilUi = psutilManager()
        self.ui_tab.addTab(self.psutilUi, 'psutilManager')

    def on_signupPage(self):
        self.signupUi = signupPage()
        self.ui_tab.addTab(self.signupUi, 'signupPage')

    def on_tabs(self):
        self.tabsUi = tabs()
        self.ui_tab.addTab(self.tabsUi, 'tabs')

    def on_stackedWidget(self):
        self.stackedWidgetUi = stackedWidget()
        self.ui_tab.addTab(self.stackedWidgetUi, 'stackedWidget')

    def on_itemClicked(self, item, column):
        filename = os.path.basename(item.text(0))
        self.execute_action(filename)

def main():
    app = QApplication([])
    main = pyviewer()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
