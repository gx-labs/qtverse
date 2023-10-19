import sys
import os
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QHBoxLayout, QWidget, QTabWidget, QVBoxLayout

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from uis.psutilManager.psutilManager import psutilManager
from uis.signupPage.signupPage import signupPage
from uis.snippets.tabs import tabs
from uis.snippets.stackedWidget import stackedWidget


class pyviewer(QWidget):
    def __init__(self):
        super().__init__()
       
        # main layout
        self.setWindowTitle('pyviewer')
        self.setFixedSize(1000,800)
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)
        
        # tree widget
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.columnCount()
        main_layout.addWidget(self.tree_widget)
        self.tree_widget.setHeaderLabels(['pyviewer'])
        self.tree_widget.itemClicked.connect(self.on_itemClicked)
        
        #psutil
        psutil_item = QTreeWidgetItem(self.tree_widget)
        psutil_item.setText(0, 'psutilManager')
        psutil_subitem = QTreeWidgetItem(psutil_item)
        psutil_subitem.setText(0, 'psutilManager.py')

        #signup page item
        signup_item = QTreeWidgetItem(self.tree_widget)
        signup_item.setText(0, 'signupPage')        
        signup_subitem = QTreeWidgetItem(signup_item)
        signup_subitem.setText(0, 'signupPage.py')

        #practice item        
        snippets_item=QTreeWidgetItem(self.tree_widget)
        snippets_item.setText(0,'snippets')
        
        tabs_subitem=QTreeWidgetItem(snippets_item)
        tabs_subitem.setText(0,'tabs.py')

        stacked_subitem=QTreeWidgetItem(snippets_item)
        stacked_subitem.setText(0,'stackedWidget.py')

    def on_psutilManager(self):
        self.psutilUi=psutilManager()
        self.psutilUi.show()
                        
    def on_signupPage(self):
        self.signupUi=signupPage()
        self.signupUi.show()

    def on_tabs(self):
        self.tabsUi=tabs()
        self.tabsUi.show()

    def on_stackedWidget(self):
        self.stackedWidgetUi=stackedWidget()
        self.stackedWidgetUi.show()

    def on_itemClicked(self,item,cloumn):
        if item.text(0) == 'psutilManager.py':
            self.on_psutilManager()
            
        elif item.text(0) == 'signupPage.py':
            self.on_signupPage()
        elif item.text(0) == 'tabs.py':
            self.on_tabs()     
        elif item.text(0) == 'stackedWidget.py':
            self.on_stackedWidget()

def main():
    app = QApplication([])
    main = pyviewer()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()

