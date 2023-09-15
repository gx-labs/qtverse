import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGroupBox, QSizePolicy


class CollapsibleSection(QWidget):
    def __init__(self, parent=None):
        super(CollapsibleSection, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create a group box to hold the collapsible content
        self.group_box = QGroupBox("Collapsible Section")
        self.group_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.group_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_layout)

        # Create some content for the collapsible section
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)
        self.content_layout.addWidget(QPushButton("Button 1"))
        self.content_layout.addWidget(QPushButton("Button 2"))
        self.content_layout.addWidget(QPushButton("Button 3"))

        # Initially, set the collapsible content to be hidden
        self.group_box.setHidden(True)

        # Create a button to toggle the visibility of the collapsible section
        self.toggle_button = QPushButton("Toggle Section")
        self.toggle_button.clicked.connect(self.toggle_section)

        # Add the toggle button and collapsible content to the main layout
        self.layout.addWidget(self.toggle_button)
        self.layout.addWidget(self.group_box)

    def toggle_section(self):
        # Toggle the visibility of the collapsible content
        self.group_box.setHidden(not self.group_box.isHidden())


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.collapsible_section = CollapsibleSection()
        self.layout.addWidget(self.collapsible_section)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.setWindowTitle("Collapsible Section Example")
    main_window.setGeometry(100, 100, 400, 300)
    main_window.show()
    sys.exit(app.exec_())
