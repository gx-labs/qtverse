import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QColorDialog, QComboBox, QHBoxLayout
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

        self.color_comboboxes = []
        self.color_comboboxes.append(QComboBox())
        self.color_comboboxes.append(QComboBox())

        for i, combobox in enumerate(self.color_comboboxes):
            combobox.setEditable(True)
            combobox.setPlaceholderText(f'Select Color {i+1}')
            combobox.currentIndexChanged.connect(self.update_colors)
            self.layout.addWidget(combobox)

        angles = list(range(0, 361, 45))  # Angles from 0 to 360 with 45-degree increment
        self.angle_combo_box = QComboBox()
        for angle in angles:
            self.angle_combo_box.addItem(str(angle))
        self.angle_combo_box.setCurrentIndex(0)
        self.angle_combo_box.currentIndexChanged.connect(self.rotate_gradient)

        angle_layout = QHBoxLayout()
        angle_layout.addWidget(QLabel("Angle"))
        angle_layout.addWidget(self.angle_combo_box)
        angle_layout.setSpacing(0)
        angle_layout.setAlignment(Qt.AlignLeft)

        self.layout.addLayout(angle_layout)

        self.gradient_type = 'linear'
        self.colors = ['#FF0000', '#0000FF']  # Initial colors in hex format
        self.rotation_angle = 0
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

    def update_colors(self):
        for i, combobox in enumerate(self.color_comboboxes):
            self.colors[i] = combobox.currentText()
        self.generate_gradient()
        self.update_gradient_label()

    def rotate_gradient(self, index):
        angle = int(self.angle_combo_box.itemText(index))
        self.rotation_angle = angle
        self.update_gradient_label()

def run_app():
    app = QApplication(sys.argv)
    window = GradientGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
