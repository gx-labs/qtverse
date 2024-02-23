from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QListWidget, QScrollArea
from PySide2.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Lazy Loading Example")
        self.layout = QVBoxLayout(self)

        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to contain the list
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        # Create a QListWidget to display widgets
        self.list_widget = QListWidget()
        self.scroll_layout.addWidget(self.list_widget)

        # Add the scroll widget to the scroll area
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)

        # Connect scroll area signals
        self.scroll_area.verticalScrollBar().valueChanged.connect(self.scroll_event)

        # Simulate initial loading
        self.lazy_load_widgets()

    def lazy_load_widgets(self):
        # Simulate loading 10 widgets at a time
        for i in range(10):
            widget_text = f"Widget {self.list_widget.count() + 1}"
            self.list_widget.addItem(widget_text)

    def scroll_event(self):
        # Check if the scrollbar is at the bottom
        scrollbar = self.scroll_area.verticalScrollBar()
        if scrollbar.value() == scrollbar.maximum():
            self.lazy_load_widgets()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
