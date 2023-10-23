import sys
from PySide2.QtCore import Qt, QStringListModel
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView

app = QApplication(sys.argv)

# Create a simple data model
data = ["Alice", "Bob", "Charlie", "David", "Eve"]
model = QStringListModel(data)

# Create a QMainWindow
window = QMainWindow()
window.setGeometry(100, 100, 600, 400)
window.setWindowTitle("Styled QTableView Example")

# Create a QTableView and set the data model
table_view = QTableView(window)
table_view.setModel(model)

# Define a stylesheet with sub-controls
stylesheet = """
QTableView {
    background-color: yellow;
    selection-background-color: green;
    selection-color: red;
}

QTableView::item {
    border: 1px solid darkgray;
    padding: 5px;
    font-size: 16px;
}

QTableView::item:selected {
    background-color: darkblue;
    color: white;
}

QTableView::item:hover {
    background-color: lightblue;
}

QHeaderView::section {
    background-color: lightgray;
    border: 1px solid darkgray;
    padding: 5px;
}

"""

# Apply the stylesheet to the QTableView
table_view.setStyleSheet(stylesheet)

window.setCentralWidget(table_view)
window.show()
sys.exit(app.exec_())
