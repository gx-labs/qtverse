import sys
from PySide2.QtWidgets import  QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QColorDialog, QComboBox,QHBoxLayout,QLineEdit,QSlider
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt

class GradientGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Gradient Generator')
        self.setGeometry(100, 100, 500, 300)

        self.centralWidget= QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout= QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.gradient_label= QLabel()
        self.layout.addWidget(self.gradient_label)

        self.change_gradient_button= QPushButton('Linear/ Radial')
        self.change_gradient_button.clicked.connect(self.change_gradient)
        self.layout.addWidget(self.change_gradient_button)
        
        self.color_layout_1 = QHBoxLayout()
        self.layout.addLayout(self.color_layout_1)
        self.select_color_button1= QPushButton('Select color 1')
        self.select_color_button1.clicked.connect(self.select_color1)
        self.color_layout_1.addWidget(self.select_color_button1)
        self.line_edit1 = QLineEdit()
        self.line_edit1.setFixedWidth(70)
        self.line_edit1.textChanged.connect(self.change_color_from_hex_button1)
        self.color_layout_1.addWidget(self.line_edit1)


        self.color_layout_2 = QHBoxLayout()
        self.layout.addLayout(self.color_layout_2)
        self.select_color_button2= QPushButton('Select color 2')
        self.select_color_button2.clicked.connect(self.select_color2)
        self.color_layout_2.addWidget(self.select_color_button2)
        self.line_edit2 = QLineEdit()
        self.line_edit2.setFixedWidth(70)
        self.line_edit2.textChanged.connect(self.change_color_from_hex_button2)
        self.color_layout_2.addWidget(self.line_edit2)

        angles = list(range(0, 361, 45))
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

        self.gradient_type='linear'
        self.colors= ['#FF0000', '#0000FF']
        self.stops = [0 , 1]
        self.generate_gradient()
        self.update_gradient_label()

        self.stop1_slider = QSlider(Qt.Horizontal)
        self.stop1_slider.setRange(0, 100)
        self.stop1_slider.setValue(0)
        self.stop1_slider.valueChanged.connect(self.update_stop_0)
        
        self.layout.addWidget(self.stop1_slider)

        self.stop2_slider = QSlider(Qt.Horizontal)
        self.stop2_slider.setRange(0, 100)
        self.stop2_slider.setValue(100)
        self.stop2_slider.valueChanged.connect(self.update_stop_1)
       
        self.layout.addWidget(self.stop2_slider)

    def generate_gradient(self):
        if self.gradient_type == 'linear':
             self.gradient = f"qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        else:
            self.gradient = f"qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"

    def update_gradient_label(self):
        style_sheet = f"background: {self.gradient};"
        print(style_sheet)
        self.gradient_label.setStyleSheet(style_sheet)

    def change_gradient(self):
        self.gradient_type = 'radial' if self.gradient_type == 'linear' else 'linear'
        self.generate_gradient()
        self.update_gradient_label() 

    def select_color1(self):
        color_dialog1 = QColorDialog(self)
        current_color1 = QColor(self.colors[0])
        color_dialog1.setCurrentColor(current_color1)

        if color_dialog1.exec_():
            selected_color1 = color_dialog1.selectedColor().name()
            self.colors[0] = selected_color1
            self.generate_gradient()
            self.update_gradient_label()
            self.select_color_button1.setStyleSheet(f"background-color: {selected_color1}; color: {selected_color1};")
            self.line_edit1.setText(selected_color1)

    def select_color2(self):
        color_dialog = QColorDialog(self)
        current_color = QColor(self.colors[1])
        color_dialog.setCurrentColor(current_color)

        if color_dialog.exec_():
            selected_color = color_dialog.selectedColor().name()
            self.colors[1] = selected_color
            print(self.colors[1])
            self.generate_gradient()
           
            self.update_gradient_label()
            x=f"background-color: {self.colors[1]}; color: {self.colors[1]};"
            self.select_color_button2.setStyleSheet(x)
            self.line_edit2.setText(selected_color)

    def change_color_from_hex_button1(self):
        hex_color1 =  self.line_edit1.text()

        if self.is_valid_hex_color(hex_color1):
            self.colors[0] = hex_color1
            self.generate_gradient()
            self.update_gradient_label() 
            self.select_color_button1.setStyleSheet(f"background-color: {hex_color1}; color: {hex_color1};")


    def change_color_from_hex_button2(self):

        hex_color2 =  self.line_edit2.text()

        if self.is_valid_hex_color(hex_color2):
            self.colors[1] = hex_color2
            self.generate_gradient()
            self.update_gradient_label()
            self.select_color_button2.setStyleSheet(f"background-color: {hex_color2}; color: {hex_color2};")


    def is_valid_hex_color(self, color):
        return len(color) == 7 and color[0] == '#' and all(c in '0123456789abcdefABCDEF' for c in color[1:])
    

    def rotate_gradient(self, index):

        angle = int(self.sender().itemText(index))

        if angle == 0:
            self.gradient= f"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 45:
            self.gradient= f"qlineargradient(spread:pad,x1:0, y1:1, x2:1, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 90:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 135:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:1, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 180:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:0, x2:0, y2:1, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 225:
            self.gradient = f"qlineargradient(spread:pad,x1:1, y1:0, x2:0, y2:1, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 270:
            self.gradient = f"qlineargradient(spread:pad,x1:1, y1:0, x2:0, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle == 315:
            self.gradient = f"qlineargradient(spread:pad,x1:1, y1:1, x2:0, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        if angle ==360:
            self.gradient = f"qlineargradient(spread:pad,x1:0, y1:1, x2:0, y2:0, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"

        self.update_gradient_label()

        
    def update_stop_0(self,value):
         self.stops[0]= value/100
         self.generate_gradient()
         self.update_gradient_label()

    def update_stop_1(self,value):
         
         self.stops[1]= value/100
         print(self.stops)
         self.generate_gradient()
         self.update_gradient_label()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradientGenerator()
    window.show()
    sys.exit(app.exec_())