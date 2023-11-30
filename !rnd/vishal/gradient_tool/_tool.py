import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QColorDialog, QComboBox,QHBoxLayout,QLineEdit
from PySide2.QtGui import QLinearGradient, QRadialGradient,QColor
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

        self.change_gradient_button = QPushButton('Linear/ Radial')
        self.change_gradient_button.clicked.connect(self.change_gradient)
        self.layout.addWidget(self.change_gradient_button)

        self.color_buttons = []
        self.color_buttons.append(QPushButton('Select Color 1'))
        self.color_buttons.append(QPushButton('Select Color 2'))
        for btn in self.color_buttons:
            btn.clicked.connect(self.choose_color)
            self.layout.addWidget(btn)

        self.color_line_edits = []
        for i in range(len(self.color_buttons)):
            layout = QHBoxLayout()
            color_button = self.color_buttons[i]
            color_button.clicked.connect(self.choose_color)
            layout.addWidget(color_button)
            color_line_edit = QLineEdit()
            color_line_edit.setFixedWidth(70)  # Adjust the width as needed
            color_line_edit.textChanged.connect(self.change_color_from_hex)
            layout.addWidget(color_line_edit)
            self.color_line_edits.append(color_line_edit)
            self.layout.addLayout(layout)
        angles = list(range(0, 361, 45))  # Angles from 0 to 360 with 45-degree increment
        self.angle_combo_box = QComboBox()
        for angle in angles:
            self.angle_combo_box.addItem(str(angle))
        self.angle_combo_box.setCurrentIndex(2)
        self.angle_combo_box.currentIndexChanged.connect(self.rotate_gradient)

        angle_layout = QHBoxLayout()
        angle_layout.addWidget(QLabel("Rotation"))
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
        angle = int(self.sender().itemText(index))
        if angle == 0:
            self.gradient= f"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 45:
            self.gradient= f"qlineargradient(spread:pad,x1:0, y1:1, x2:1, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 90:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 135:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:1, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 180:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:0, x2:0, y2:1, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 225:
            self.gradient = f"qlineargradient(spread:pad,x1:1, y1:0, x2:0, y2:1, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 270:
            self.gradient = f"qlineargradient(spread:pad,x1:1, y1:0, x2:0, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle == 315:
            self.gradient = f"qlineargradient(spread:pad,x1:1, y1:1, x2:0, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        if angle ==360:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:1, x2:0, y2:0, stop:0 {self.colors[0]}, stop:1 {self.colors[1]});"
        self.update_gradient_label()
    def choose_color(self, color_index):
        color_dialog = QColorDialog(self)
        current_color = QColor(self.colors[color_index])
        color_dialog.setCurrentColor(current_color)

        if color_dialog.exec_():
            selected_color = color_dialog.selectedColor().name()
            self.colors[color_index] = selected_color

            # Update the color button text and line edit text with the selected color
            self.color_buttons[color_index].setStyleSheet(f"background-color: {selected_color}; color: {selected_color};")
            self.color_line_edits[color_index].setText(selected_color)

            self.generate_gradient()
            self.update_gradient_label()

    def change_color_from_hex(self):
        line_edit = self.sender()
        index = self.color_line_edits.index(line_edit)
        hex_color = line_edit.text()
        if self.is_valid_hex_color(hex_color):
            self.colors[index] = hex_color
            self.generate_gradient()
            self.update_gradient_label()
    def is_valid_hex_color(self, color):
        return len(color) == 7 and color[0] == '#' and all(c in '0123456789abcdefABCDEF' for c in color[1:])
def run_app():
    app = QApplication(sys.argv)
    window = GradientGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
