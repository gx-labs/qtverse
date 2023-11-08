import sys
import PySide2
from PySide2 import QtCore
from PySide2.QtWidgets import (
    QMainWindow,
    QApplication,
    QListWidgetItem,
    QLabel,
    QAction,
    QPushButton,
    QCheckBox,
    QComboBox,
    QFrame,
    QSlider,
    QVBoxLayout,
    QListWidget,
    QHBoxLayout,
    QMenuBar,
    QWidget,
    QGroupBox,
    QLineEdit,
    QRadioButton,
    QGridLayout,
    QComboBox,
    QMenu
)
from PySide2.QtCore import Qt,QSize
#from PyQt5 import QtGui, QtWidgets
from PySide2.QtGui import QDoubleValidator 
from PySide2.QtCore import Qt

class customUI(QMainWindow):
    
    def __init__(self):
        super(customUI, self).__init__()

        self.setWindowTitle("FumeFX Tool")
        self.resize(50, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        menubar = self.menuBar()
        help_menu = menubar.addMenu("Help")

        # Create a group 
        group_box = QGroupBox("FFM Auto Sim")

        main_layout.addWidget(group_box)

        group_layout = QVBoxLayout()
        group_box.setLayout(group_layout)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        checkbox1 = QCheckBox("_DefaultSim")
        checkbox2 = QCheckBox("_WaveletSim")
        checkbox3 = QCheckBox("_PostProcessing")
        checkbox4 = QCheckBox("_ViewPort Preview")

        # Add checkboxes to the QHBoxLayouts
        hbox1.addWidget(checkbox1)
        hbox1.addWidget(checkbox2)
        hbox2.addWidget(checkbox3)
        hbox2.addWidget(checkbox4)

        group_layout.addLayout(hbox1)
        group_layout.addLayout(hbox2)

        group_box2 = QGroupBox("ViewPort Preview Parameters")

        main_layout.addWidget(group_box2)

        group_layout2 = QVBoxLayout()
        group_box2.setLayout(group_layout2)

        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        radiobutton1 = QRadioButton("Active Time Segment")
        label1 = QLabel("Frame:1-To-120")
        hbox3.addWidget(radiobutton1)
        hbox3.addWidget(label1)

        radiobutton2 = QRadioButton("Time Rannge:")
        line1 = QLineEdit("")
        line2 = QLineEdit("")
        label2 = QLabel("To:")
        hbox4.addWidget(radiobutton2)
        hbox4.addWidget(line1)
        hbox4.addWidget(label2)
        hbox4.addWidget(line2)

        group_layout2.addLayout(hbox3)
        group_layout2.addLayout(hbox4)

        divider_line = QFrame()
        divider_line.setFrameShape(QFrame.HLine)
        divider_line.setFrameShadow(QFrame.Sunken)
        group_layout2.addWidget(divider_line)    

        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        radiobutton3 = QRadioButton("Viewport Size")
        label3 = QLabel("Every Nth Frame:")
        line3 = QLineEdit("")

        hbox5.addWidget(radiobutton3)
        hbox5.addWidget(label3)
        hbox5.addWidget(line3)

        radiobutton4 = QRadioButton("Image Size:")
        label4 = QLabel("W:")
        label5 = QLabel("H:")
        line4 = QLineEdit("")
        line5 = QLineEdit("")
        label2 = QLabel("To:")
        hbox6.addWidget(radiobutton4)
        hbox6.addWidget(label4)
        hbox6.addWidget(line4)
        hbox6.addWidget(label5)
        hbox6.addWidget(line5)


        group_layout2.addLayout(hbox5)
        group_layout2.addLayout(hbox6)

        divider_line2 = QFrame()
        divider_line2.setFrameShape(QFrame.HLine)
        divider_line2.setFrameShadow(QFrame.Sunken)
        group_layout2.addWidget(divider_line2)    

        hbox7 = QHBoxLayout()
        hbox8 = QHBoxLayout()

        label6 = QLabel("Format")
        combo1=QComboBox()
        combo1.addItems(["-Select", "1#", "2"])
        label7 = QLabel("Encoding")
        combo2=QComboBox()
        combo2.addItems(["None", "1#", "2"])

        hbox7.addWidget(label6)
        hbox7.addWidget(combo1)
        hbox7.addWidget(label7)
        hbox7.addWidget(combo2)

        label6 = QLabel("Quality")
        line6 = QLineEdit("")
        slider = QSlider(Qt.Horizontal, self)
        slider.setRange(0,1000)
        hbox8.addWidget(label6)
        hbox8.addWidget(line6)
        hbox8.addWidget(slider)

        group_layout2.addLayout(hbox7)
        group_layout2.addLayout(hbox8)

        divider_line3 = QFrame()
        divider_line3.setFrameShape(QFrame.HLine)
        divider_line3.setFrameShadow(QFrame.Sunken)
        group_layout2.addWidget(divider_line3) 

        hbox9 = QHBoxLayout()

        checkbox5 = QCheckBox("GPU Viewport")
        label4 = QLabel("Preview Type:")
        radiobutton5 = QRadioButton("Combined")
        radiobutton6 = QRadioButton("Separate")
       

        hbox9.addWidget(checkbox5)
        hbox9.addWidget(label4)
        hbox9.addWidget(radiobutton5)
        hbox9.addWidget(radiobutton6)

        group_layout2.addLayout(hbox9)  
        
        divider_line3 = QFrame()
        divider_line3.setFrameShape(QFrame.HLine)
        divider_line3.setFrameShadow(QFrame.Sunken)
        group_layout2.addWidget(divider_line3) 

        hbox10 = QHBoxLayout()

        checkbox6 = QCheckBox("Save to File")
        push1 = QPushButton("Browse...")
        hbox10.addWidget(checkbox6)
        hbox10.addWidget(push1)
        group_layout2.addLayout(hbox10)

        group_box3 = QGroupBox("Render Setup")

        main_layout.addWidget(group_box3)

        group_layout3 = QVBoxLayout()
        group_box3.setLayout(group_layout3)

        hbox11 = QHBoxLayout()
        checkbox7 = QCheckBox("_Render")
        push2 = QPushButton("Render Settings")
        hbox11.addWidget(checkbox7)
        hbox11.addWidget(push2)
        group_layout3.addLayout(hbox11)

        divider_line4 = QFrame()
        divider_line4.setFrameShape(QFrame.HLine)
        divider_line4.setFrameShadow(QFrame.Sunken)
        group_layout3.addWidget(divider_line4) 

        hbox12 = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()

        label8 = QLabel("Select Conatiners")
        label9 = QLabel("Ctrl + Select multiple")
        list = QListWidget()
        list.addItems([("fumeFXShape2"),("fumeFXShape3")])
        push3 = QPushButton("Refresh Selection")
        push4 = QPushButton("Run Auto Sim")
        push4.setStyleSheet(''' 
 font-size: 18px;
  letter-spacing: 2px;
  text-transform: uppercase;
  display: inline-block;
  text-align: center;
  font-weight: bold;
  padding: 0.7em 2em;
  border: 3px solid #FF0072;
  border-radius: 2px;
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.1);
  color: #FF0072;
  text-decoration: none;
  transition: 0.3s ease all;
  z-index: 1;
''')

        vbox1.addWidget(label8)
        vbox1.addWidget(list)

        vbox2.addWidget(label9)
        vbox2.addWidget(push3)
        vbox2.addWidget(push4)


        hbox12.addLayout(vbox1)
        hbox12.addLayout(vbox2)
        label10 = QLabel("FFX Simulation Not started")
        label10.setStyleSheet("background-color : lightblue")

        group_layout3.addLayout(hbox12)
        group_layout3.addWidget(label10)

app = QApplication(sys.argv)

w = customUI()
w.show()

app.exec_()
        
        
