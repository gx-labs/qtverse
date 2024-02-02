import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.utils import read_yaml
from ui.utils import qt_icon
from ui.utils import read_python
from ui.utils import read_css

designer_config_file_path = os.path.join(os.path.dirname(__file__), "cfg", "designer.yaml")

class DesignerAppWidget(QWidget):
    def __init__(self):
        super(DesignerAppWidget, self).__init__()
                
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.abspath(os.path.join(self.current_dir, '..', '..'))
        self.widgets_src_dir = os.path.join(self.project_dir, "qtverse", "widgets", "src", "WIDGETS")
                
        designer_config = read_yaml(designer_config_file_path)
        self.designer_config = designer_config
                                
        self.all_developers = designer_config["developers"].keys()
        # Get all sequence codes by iterating through sequence codes(list) for each developer in yaml
        self.all_sequence_codes = []
        for codes in designer_config["developers"].values():
            for code in codes:
                self.all_sequence_codes.append(code)
                
        widget_types = designer_config["widgets"]["default_widgets"]
                
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
                
        self.load_create_groupbox = QGroupBox()
        self.load_create_groupbox.setMaximumHeight(50)
        self.load_create_groupbox_layout = QHBoxLayout()
        self.load_create_groupbox.setLayout(self.load_create_groupbox_layout)
                
        self.load_widget_label = QLabel('Load Widget ')
        self.load_create_groupbox_layout.addWidget(self.load_widget_label)
                
        self.load_sequence_combo = QComboBox()
        self.load_sequence_combo.addItem("Select a sequence")
        self.load_sequence_combo.addItems(list(self.all_sequence_codes))
        self.load_sequence_combo.currentIndexChanged.connect(self.update_load_sequence_number)
        self.load_create_groupbox_layout.addWidget(self.load_sequence_combo)
                
        self.load_number_combo = QComboBox()
        self.load_number_combo.setEnabled(False)
        self.load_create_groupbox_layout.addWidget(self.load_number_combo)
                
        self.load_button = QPushButton("Load")
        self.load_button.setIcon(QIcon(qt_icon("load.png")))
        self.load_button.pressed.connect(self.load_selected_widget)
        self.load_create_groupbox_layout.addWidget(self.load_button)
            
        self.load_create_groupbox_layout.addStretch(1)
                
        self.create_widget_label = QLabel('Create Widget ')
        self.load_create_groupbox_layout.addWidget(self.create_widget_label)
                
        self.create_widget_dev_combo = QComboBox()
        self.create_widget_dev_combo.addItem("Select developer")
        self.create_widget_dev_combo.addItems(self.all_developers)
        self.create_widget_dev_combo.currentIndexChanged.connect(self.update_sequence_label)
        self.load_create_groupbox_layout.addWidget(self.create_widget_dev_combo)
                
        self.create_widget_sequence_combo = QComboBox()
        self.create_widget_sequence_combo.setEnabled(False)
        self.load_create_groupbox_layout.addWidget(self.create_widget_sequence_combo)
            
        self.create_widget_type_combo = QComboBox()
        self.create_widget_type_combo.addItems(widget_types)
        self.load_create_groupbox_layout.addWidget(self.create_widget_type_combo)
                
        self.create_widget_button = QPushButton("Create")        
        self.create_widget_button.setIcon(QIcon(qt_icon("create.png")))  
        self.create_widget_button.pressed.connect(self.create_new_widget_from_template)          
        self.load_create_groupbox_layout.addWidget(self.create_widget_button)
                
        self.main_layout.addWidget(self.load_create_groupbox)
            
        self.designer_groupbox = QGroupBox()
        self.main_layout.addWidget(self.designer_groupbox)
                
        self.designer_layout = QHBoxLayout()
        self.designer_groupbox.setLayout(self.designer_layout)
                
        self.css_layout = QVBoxLayout()
        self.designer_layout.addLayout(self.css_layout)
            
        self.css_label = QLabel('CSS')
        self.css_layout.addWidget(self.css_label)
        
        self.css_layout.addSpacing(10)
        
        self.css_filepath = QLabel("Filepath: ")
        self.css_layout.addWidget(self.css_filepath)
                
        self.css_edit = QTextEdit()
        self.css_edit.setMaximumWidth(700)
        self.css_edit.setFontPointSize(11)
        self.css_layout.addWidget(self.css_edit)
                
        self.python_layout = QVBoxLayout()
        self.designer_layout.addLayout(self.python_layout)
                
        self.python_run_layout = QHBoxLayout()
        self.python_layout.addLayout(self.python_run_layout)
            
        self.python_label = QLabel('Python')
        self.python_run_layout.addWidget(self.python_label)
            
        self.python_run_button = QPushButton("Run")
        self.python_run_button.setIcon(QIcon(qt_icon("run.png")))
        self.python_run_button.pressed.connect(self.run_widget_from_editor)
        self.python_run_layout.addWidget(self.python_run_button)
                
        self.python_save_button = QPushButton("Save")
        self.python_save_button.setIcon(QIcon(qt_icon("save.png")))
        self.python_save_button.pressed.connect(self.save_widget)
        self.python_run_layout.addWidget(self.python_save_button)
        
        self.python_filepath = QLabel("Filepath: ")
        self.python_layout.addWidget(self.python_filepath)
                
        self.python_edit = QTextEdit()
        self.python_edit.setMaximumWidth(700)
        self.python_edit.setFontPointSize(11)
        self.python_layout.addWidget(self.python_edit)
                
        self.preview_layout = QVBoxLayout()
        self.preview_layout.setAlignment(Qt.AlignTop)
        self.designer_layout.addLayout(self.preview_layout)
                
        self.preview_label = QLabel('Preview')
        self.preview_layout.addWidget(self.preview_label)
        
    def update_sequence_label(self, index):
        # Skip the placeholder item
        if index > 0:  
            sequence_codes = self.designer_config["developers"][self.create_widget_dev_combo.currentText()]
            if sequence_codes:
                self.create_widget_sequence_combo.setEnabled(True)
                self.create_widget_sequence_combo.clear()
                self.create_widget_sequence_combo.addItems(sequence_codes)
            else:
                self.create_widget_sequence_combo.clear()
                self.create_widget_sequence_combo.setEnabled(False)
        else:
            self.create_widget_sequence_combo.clear()
            self.create_widget_sequence_combo.setEnabled(False)
                        
    def update_load_sequence_number(self, index):
        # Skip placeholder
        if index > 0:
            sequence = self.all_sequence_codes[index - 1]
            sequence_dir = os.path.join(self.widgets_src_dir, sequence)
            widgets_list = os.listdir(sequence_dir)
            
            if widgets_list:
                self.load_number_combo.setEnabled(True)
                self.load_number_combo.clear()
                self.load_number_combo.addItems(widgets_list)
            else:
                self.load_number_combo.clear()
                self.load_number_combo.setEnabled(False)
        else:
            self.load_number_combo.clear()
            self.load_number_combo.setEnabled(False)
            
    def load_selected_widget(self):
        print("Loading selected widget...")
        if self.load_sequence_combo.currentIndex() != 0:
            selected_widget_dir = os.path.join(self.widgets_src_dir, self.load_sequence_combo.currentText())
            selected_widget_seq_dir = os.path.join(selected_widget_dir, f"{self.load_number_combo.currentText()}\widget")
            
            python_data = read_python(selected_widget_seq_dir)
            self.python_edit.setText(python_data)
            self.python_filepath.setText(f"{selected_widget_seq_dir}\CustomWidget.py")
            
            css_data = read_css(selected_widget_seq_dir)
            self.css_edit.setText(css_data)
            self.css_filepath.setText(f"{selected_widget_seq_dir}\style.css")
        
    def create_new_widget_from_template(self):
        print(f"Creating new {self.create_widget_type_combo.currentText()} widget...")
        
    def run_widget_from_editor(self):
        print("Refreshing widget...")
        
    def save_widget(self):
        print("Saving widget...")
                        