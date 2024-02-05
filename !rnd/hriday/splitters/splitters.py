import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
 
class Window(QMainWindow):
 
    def __init__(self, parent=None):
 
        super(Window, self).__init__(parent)
        self.UI()
 
    def UI(self):
 
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
 
        self.statusBar().showMessage("Ready")
 
        page1 = FirstWidget(self)
        page1.visualize_btn.clicked.connect(self.P_2)
        self.central_widget.addWidget(page1)        
 
        self.setGeometry(10, 10, 800, 500)    #All three methods have been inherited from the QWidget class.
        self.showMaximized()
        self.setWindowTitle('PTV')
        self.setWindowIcon(QIcon('tuc_logo.png'))
 
    def P_2(self):
 
        page2 = VisualizeWidget(self)
        self.central_widget.addWidget(page2)
        self.central_widget.setCurrentWidget(page2)
 
 
class FirstWidget(QWidget):
 
    def __init__(self, parent=None):
        super(FirstWidget, self).__init__(parent)
        self.buttons()
 
    def buttons(self):
 
        self.btn2 = QPushButton("Visualize")
        self.buttonsLayout = QVBoxLayout() 
        self.buttonsLayout.addWidget(self.btn2)
        self.visualize_btn = self.btn2        
        self.setLayout(self.buttonsLayout)
 
 
class VisualizeWidget(QWidget):
 
    def __init__(self, parent=None):
        super(VisualizeWidget, self).__init__(parent)
 
 
        self.dirmodel = QFileSystemModel()        
        self.dirmodel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)    # Don't show files, just folders
 
        self.folder_view = QTreeView(parent=self);
        self.folder_view.setModel(self.dirmodel)
        self.folder_view.clicked[QModelIndex].connect(self.clicked)
 
        self.now_layout = QVBoxLayout()
        self.now_layout.addWidget(self.folder_view)
 
        #self.setLayout(self.now_layout)
 
        #HERE is where I'm trying to add the layout to the widget. 
        self.left_widget = QWidget()
        self.left_widget.setLayout(self.now_layout)            
 
 
    def set_path(self):
        self.dirmodel.setRootPath("")
 
    def clicked(self, index):
        index = self.selectionModel.currentIndex()
        dir_path = self.dirmodel.filePath(index)
 
        self.filemodel.setRootPath(dir_path)
        self.file_view.setRootIndex(self.filemodel.index(dir_path))          
 
def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()
 
if __name__ == '__main__':
    sys.exit(main())