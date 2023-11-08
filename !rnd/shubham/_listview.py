import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget
from PySide2.QtCore import QStringListModel

class MyListViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PySide ListView Example")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

        model = QStringListModel()
        model.setStringList(items)

        list_view = QListView()
        list_view.setModel(model)

        layout.addWidget(list_view)

def main():
    app = QApplication(sys.argv)
    window = MyListViewApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyListViewApp()

    style = """
QListView {
    alternate-background-color: yellow;
}
QListView {
    show-decoration-selected: 1; /* make the selection span the entire width of the view */
}

QListView::item:alternate {
    background: #EEEEEE;
}

QListView::item:selected {
    border: 1px solid #6a6ea9;
}

QListView::item:selected:!active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #ABAFE5, stop: 1 #8588B2);
}

QListView::item:selected:active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #6a6ea9, stop: 1 #888dd9);
}

QListView::item:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);
}    """


    window.setStyleSheet(style)

    window.show()
    sys.exit(app.exec_())

