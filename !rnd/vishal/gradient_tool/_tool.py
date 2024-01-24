import sys
from PySide2.QtWidgets import  QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QColorDialog, QComboBox,QHBoxLayout,QLineEdit,QSlider,QPlainTextEdit,QMessageBox
from PySide2.QtGui import QColor,QIcon,QGuiApplication
from PySide2.QtCore import Qt,QTimer

class GradientGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Gradient Generator')

        self.centralWidget= QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout= QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.gradient_label= QLabel()
        self.gradient_label.setFixedHeight(80)
        self.layout.addWidget(self.gradient_label)

        self.change_gradient_button= QPushButton('Linear/ Radial')
        self.change_gradient_button.clicked.connect(self.change_gradient)
        self.layout.addWidget(self.change_gradient_button)
        
        self.color_layout_1 = QHBoxLayout()
        self.layout.addLayout(self.color_layout_1)
        color1_label = QLabel("Color 1:")
        self.color_layout_1.addWidget(color1_label)

        self.select_color_button1= QPushButton()
        self.select_color_button1.clicked.connect(self.select_color1)
        self.select_color_button1.setFixedWidth(100)
        self.select_color_button1.setStyleSheet(f"background-color: #ff0000; color: #ff0000;")
        self.color_layout_1.addWidget(self.select_color_button1)


        self.line_edit1 = QLineEdit()
        self.line_edit1.setFixedWidth(110)
        self.line_edit1.setText("#ff0000")
        self.line_edit1.textChanged.connect(self.change_color_from_hex_button1)
        self.color_layout_1.addWidget(self.line_edit1)
        
        self.color_layout_2 = QHBoxLayout()
        self.layout.addLayout(self.color_layout_2)
        color1_label = QLabel("Color 2:")
        self.color_layout_2.addWidget(color1_label)

        self.select_color_button2= QPushButton()
        self.select_color_button2.setFixedWidth(100)
        self.select_color_button2.setStyleSheet(f"background-color:#0000ff; color: #0000ff;")
        self.select_color_button2.clicked.connect(self.select_color2)
        self.color_layout_2.addWidget(self.select_color_button2)

        self.line_edit2 = QLineEdit()
        self.line_edit2.setFixedWidth(110)
        self.line_edit2.setText("#0000ff")
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

        self.rotate_left_button = QPushButton()
        self.rotate_left_button.setIcon(QIcon("!rnd/vishal/img/left-arrow.png"))
        self.rotate_left_button.clicked.connect(self.rotate_left)
        angle_layout.addWidget(self.rotate_left_button)

        self.rotate_right_button = QPushButton()
        self.rotate_right_button.setIcon(QIcon("!rnd/vishal/img/right-arrow.png"))
        self.rotate_right_button.clicked.connect(self.rotate_right)
        angle_layout.addWidget(self.rotate_right_button)

        self.gradient_type='linear'
        self.colors= ['#FF0000', '#0000FF']
        self.stops = [0 , 1]
        self.A= 0
        self.B= 0
        self.C= 1
        self.D=0
        self.generate_gradient()
        self.update_gradient_label()

        stop1_label = QLabel("Stop 1")
        self.stop1_slider = QSlider(Qt.Horizontal)
        self.stop1_slider.setRange(0, 99)
        self.stop1_slider.setValue(0)
        self.stop1_slider.valueChanged.connect(self.update_stop_0)
        self.color_layout_1.addWidget(stop1_label)
        self.color_layout_1.addWidget(self.stop1_slider)
        

        stop2_label = QLabel("Stop 2")
        self.stop2_slider = QSlider(Qt.Horizontal)
        self.stop2_slider.setRange(0, 100)
        self.stop2_slider.setValue(100)
        self.stop2_slider.valueChanged.connect(self.update_stop_1)
        self.color_layout_2.addWidget(stop2_label)
        self.color_layout_2.addWidget(self.stop2_slider)
       

        self.code_text_edit = QPlainTextEdit()
        self.code_text_edit.setFixedHeight(80)
        self.code_text_edit.setReadOnly(True)
        self.layout.addWidget(self.code_text_edit)

        copy_code_button = QPushButton('Copy Code')
        copy_code_button.clicked.connect(self.copy_code_to_clipboard)
        self.layout.addWidget(copy_code_button)
        
        self.soft_prompt_label = QLabel()
        self.layout.addWidget(self.soft_prompt_label)

        self.print_gradient()

    def generate_gradient(self):
        if self.gradient_type == 'linear':
             self.gradient = f"qlineargradient(spread:pad , x1:{self.A}, y1:{self.B}, x2:{self.C}, y2:{self.D}, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
             
        else:
            self.gradient = f"qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:{self.stops[0]} {self.colors[0]}, stop:{self.stops[1]} {self.colors[1]});"
        
    def print_gradient(self):
        self.code_text_edit.setPlainText(self.gradient)

    def update_gradient_label(self):
        style_sheet = f"background: {self.gradient};"
        
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
            self.A= 1
            self.B= 1
            self.C= 1
            self.D=0
        if angle == 45:
            self.A= 0
            self.B= 1
            self.C= 1
            self.D=0
        if angle == 90:
            self.A= 0
            self.B= 0
            self.C= 1
            self.D= 0
        if angle == 135:
            self.A= 0
            self.B= 0
            self.C= 1
            self.D= 1
        if angle == 180:
            self.A= 0
            self.B= 0
            self.C= 0
            self.D= 1
        if angle == 225:
            self.A= 1
            self.B= 0
            self.C= 0
            self.D= 1 
        if angle == 270:
            self.A= 1
            self.B= 0
            self.C= 0
            self.D= 0
        if angle == 315:
            self.A= 1
            self.B= 1
            self.C= 0
            self.D= 0
        if angle ==360:
            self.A= 0
            self.B= 1
            self.C= 0
            self.D=0
            
        self.generate_gradient()
        self.update_gradient_label()

        
    def update_stop_0(self,value):
         self.stops[0]= value/100
         self.generate_gradient()
         self.update_gradient_label()

    def update_stop_1(self,value):
         self.stops[1]= value/100
         self.generate_gradient()
         self.update_gradient_label()

    def rotate_left(self):
        current_index = self.angle_combo_box.currentIndex()
        if current_index > 0:
            self.angle_combo_box.setCurrentIndex(current_index - 1)

    def rotate_right(self):
        current_index = self.angle_combo_box.currentIndex()
        if current_index < self.angle_combo_box.count() - 1:
            self.angle_combo_box.setCurrentIndex(current_index + 1)
    
    def copy_code_to_clipboard(self):
        # Copy the code to the clipboard
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.gradient)

        # Show a soft prompt indicating that the code has been copied
        self.show_soft_prompt("Code copied to clipboard")

    def show_soft_prompt(self, message, duration=2000):
        self.soft_prompt_label.setText(message)
        self.soft_prompt_label.show()

        # Use a QTimer to hide the soft prompt after the specified duration
        timer = QTimer(self)
        timer.singleShot(duration, self.soft_prompt_label.hide)


    def connect_signals(self):
        self.change_gradient_button.clicked.connect(self.update_gradient)
        self.select_color_button1.clicked.connect(self.update_gradient)
        self.select_color_button2.clicked.connect(self.update_gradient)
        self.stop1_slider.valueChanged.connect(self.update_gradient)
        self.stop2_slider.valueChanged.connect(self.update_gradient)
        self.angle_combo_box.currentIndexChanged.connect(self.update_gradient)
        self.rotate_left_button.clicked.connect(self.update_gradient)
        self.rotate_right_button.clicked.connect(self.update_gradient)

    def update_gradient(self):
        self.generate_gradient()
        self.update_gradient_label()
        self.print_gradient()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradientGenerator()
    window.connect_signals()
    window.show()
    sys.exit(app.exec_())                                                                      