from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QComboBox, QVBoxLayout, QWidget, QPushButton

class comboBoxWidget(QWidget):
    def __init__(self, parent=None):
        super(comboBoxWidget, self).__init__(parent)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Wip", "Submitted"])

        layout = QVBoxLayout(self)
        layout.addWidget(self.comboBox)
        layout.setContentsMargins(0, 0, 0, 0)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setHeaderLabels(["Widget Name", "Status"])

        
        self.addSampleData()

        # psu buttons
        self.allButton = QPushButton("All", self)
        self.wipButton = QPushButton("Wip", self)
        self.submittedButton = QPushButton("Submitted", self)

        # Connect buttons to filter functions
        self.allButton.clicked.connect(self.showAllItems)
        self.wipButton.clicked.connect(self.showWipItems)
        self.submittedButton.clicked.connect(self.showSubmittedItems)

        # Set up the layout
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.allButton)
        buttonLayout.addWidget(self.wipButton)
        buttonLayout.addWidget(self.submittedButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self.treeWidget)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def addSampleData(self):
        
        items = [("Widget1", "Wip"),
                 ("Widget2", "Submitted"),
                 ("Widget3", "Wip"),
                 ("Widget4", "Submitted")]

        for item in items:
            widgetItem = QTreeWidgetItem(self.treeWidget, item)
           
            comboWidget = comboBoxWidget()
            comboWidget.comboBox.setCurrentText(item[1])

            self.treeWidget.setItemWidget(widgetItem, 1, comboWidget)

    def showAllItems(self):
        for i in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(i)
            item.setHidden(False)

    def showWipItems(self):
        self.filterItems("Wip")

    def showSubmittedItems(self):
        self.filterItems("Submitted")

    def filterItems(self, status):
        for i in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(i)
            comboWidget = self.treeWidget.itemWidget(item, 1)

            # Get the status of the current item
            currentStatus = comboWidget.comboBox.currentText()

            # Check if the item should be visible based on the selected status
            if status == "All" or status == currentStatus:
                item.setHidden(False)
            else:
                item.setHidden(True)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


