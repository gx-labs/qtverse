import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel,QColorDialog
from PySide2.QtGui import QLinearGradient, QRadialGradient
from PySide2.QtCore import Qt

class GradientGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Gradient Generator')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.gradient_label = QLabel()
        self.layout.addWidget(self.gradient_label)

        self.change_gradient_button = QPushButton('Change Gradient Type')
        self.change_gradient_button.clicked.connect(self.change_gradient)
        self.layout.addWidget(self.change_gradient_button)

        self.color_buttons = []
        self.color_buttons.append(QPushButton('Select Color 1'))
        self.color_buttons.append(QPushButton('Select Color 2'))

        for btn in self.color_buttons:
            btn.clicked.connect(self.choose_color)
            self.layout.addWidget(btn)

        self.gradient_type = 'linear'
        self.colors = ['#FF0000', '#0000FF']  # Initial colors in hex format
        self.generate_gradient()
        self.update_gradient_label()

    def generate_gradient(self):
        if self.gradient_type == 'linear':
            self.gradient = f"qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        else:
            self.gradient = f"qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"

    def update_gradient_label(self):
        style_sheet = f"background: {self.gradient};"
        self.gradient_label.setStyleSheet(style_sheet)

    def change_gradient(self):
        self.gradient_type = 'radial' if self.gradient_type == 'linear' else 'linear'
        self.generate_gradient()
        self.update_gradient_label()

    def choose_color(self):
        button = self.sender()
        color_index = self.color_buttons.index(button)
        # Open a color dialog to select a color
        color_dialog = QColorDialog.getColor()
        
        if color_dialog.isValid():
            self.colors[color_index] = color_dialog.name() 
            self.generate_gradient()
            self.update_gradient_label()

def run_app():
    app = QApplication(sys.argv)
    window = GradientGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
