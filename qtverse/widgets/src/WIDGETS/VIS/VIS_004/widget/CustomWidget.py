from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QToolTip

class CustomTooltip(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel('This is a custom tooltip!')
        layout.addWidget(label)
        self.setLayout(layout)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a QPushButton
        button = QPushButton('Hover me!')

        # Set the tooltip for the QPushButton
        custom_tooltip = CustomTooltip(self)
        button.setToolTip('')  # Clear default tooltip
        button.installEventFilter(self)

        layout.addWidget(button)
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if event.type() == event.ToolTip:
            custom_tooltip = self.findChild(CustomTooltip)
            custom_tooltip.setGeometry(event.globalPos().x() + 10, event.globalPos().y() + 10, 200, 50)
            custom_tooltip.show()
        elif event.type() == event.ToolTipChange:
            custom_tooltip = self.findChild(CustomTooltip)
            custom_tooltip.hide()

        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication([])

    window = MyWidget()
    window.show()

    app.exec_()
