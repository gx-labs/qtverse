import os
import sys
import shutil
import importlib.util

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.utils import read_yaml
from ui.utils import qt_icon
from ui.utils import read_python
from ui.utils import read_css

from ui.widgets.thumbnail import ThumbnailWidget

designer_config_file_path = os.path.join(os.path.dirname(__file__), "cfg", "designer.yaml")

class DesignerAppWidget(QWidget):
    def __init__(self):
        super(DesignerAppWidget, self).__init__()
                
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.abspath(os.path.join(self.current_dir, '..', '..'))
        self.widgets_src_dir = os.path.join(self.project_dir, "qtverse", "widgets", "src", "WIDGETS")
        self.templates_dir = os.path.join(self.current_dir, "templates")
                
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
            
        self.reset_button = QPushButton("Reset")
        self.reset_button.setIcon(QIcon(qt_icon("reset.png")))
        self.reset_button.pressed.connect(self.reset_widget)
        self.load_create_groupbox_layout.addWidget(self.reset_button)
        
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
        # self.designer_layout.addLayout(self.css_layout)
            
        self.css_label = QLabel('CSS')
        self.css_layout.addWidget(self.css_label)
        
        self.css_layout.addSpacing(10)
        
        self.css_filepath = QLabel("Filepath: ")
        self.css_layout.addWidget(self.css_filepath)
                
        self.css_edit = QTextEdit()
        self.css_edit.setFontPointSize(11)
        self.css_layout.addWidget(self.css_edit)
                
        self.python_layout = QVBoxLayout()
        # self.designer_layout.addLayout(self.python_layout)
                
        self.python_run_layout = QHBoxLayout()
        self.python_layout.addLayout(self.python_run_layout)
            
        self.python_label = QLabel('Python')
        self.python_run_layout.addWidget(self.python_label)
        
        self.python_run_layout.addStretch(1)
            
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
        self.python_edit.setFontPointSize(11)
        self.python_layout.addWidget(self.python_edit)
        
        self.css_python_layout = QHBoxLayout()
        self.css_python_layout.addLayout(self.css_layout)
        self.css_python_layout.addLayout(self.python_layout)
                
        self.preview_layout = QVBoxLayout()
        # self.preview_layout.setAlignment(Qt.AlignTop)
                
        self.preview_label = QLabel('Preview')
        self.preview_layout.addWidget(self.preview_label, alignment=Qt.AlignTop)
        
        self.preview_widget = QWidget()
        self.preview_layout.addWidget(self.preview_widget)
        
        self.css_python_splitter = QSplitter()
        
        self.css_python_splitter.addWidget(QWidget())
        self.css_python_splitter.addWidget(QWidget())
        
        self.css_python_splitter.setCollapsible(0, False)
        self.css_python_splitter.setCollapsible(1, False)
        
        self.css_python_splitter.widget(0).setLayout(self.css_python_layout)
        self.css_python_splitter.widget(1).setLayout(self.preview_layout)
        
        self.css_python_splitter.setSizes([QSizePolicy.Expanding, QSizePolicy.Fixed])
        
        self.css_python_splitter.widget(1).setMinimumWidth(250)
        self.css_python_splitter.widget(1).setMaximumWidth(450)
        
        self.designer_layout.addWidget(self.css_python_splitter)
        
        
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
        print(f"update sequence: {index}")
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
            print(f"load seq combo: {self.load_sequence_combo.currentIndex()}")
            selected_widget_dir = os.path.join(self.widgets_src_dir, self.load_sequence_combo.currentText())
            selected_widget_seq_dir = os.path.join(selected_widget_dir, f"{self.load_number_combo.currentText()}\widget")
            
            python_data = read_python(selected_widget_seq_dir)
            self.python_edit.setText(python_data)
            self.python_filepath.setText(f"{selected_widget_seq_dir}\CustomWidget.py")
            
            css_data = read_css(selected_widget_seq_dir)
            self.css_edit.setText(css_data)
            self.css_filepath.setText(f"{selected_widget_seq_dir}\style.css")
            
            self.display_widget_preview()
            
        else:
            self.python_edit.setText("")
            self.python_filepath.setText("Filepath: ")
            
            self.css_edit.setText("")
            self.css_filepath.setText("Filepath: ")
            
    def reset_widget(self):
        print("Reset selection")
        self.load_sequence_combo.setCurrentIndex(0)
        
        self.css_filepath.setText("Filepath: ")
        self.css_edit.setText("")
        
        self.python_filepath.setText("Filepath: ")
        self.python_edit.setText("")
        
        item = self.preview_layout.takeAt(1)
        widget = item.widget()
        if widget:
            widget.deleteLater()
        
    def create_new_widget_from_template(self):
        
        self.reset_widget()
        
        print(f"Creating new {self.create_widget_type_combo.currentText()} widget...")
        selected_sequence = os.path.join(self.widgets_src_dir, self.create_widget_sequence_combo.currentText())

        new_sequence_number = str(len(os.listdir(selected_sequence)) + 1).zfill(3)
        new_widget_directory = os.path.join(selected_sequence, f"{self.create_widget_sequence_combo.currentText()}_{new_sequence_number}")
        
        selected_template = self.create_widget_type_combo.currentText()
        selected_template_directory = os.path.join(self.templates_dir, "WIDGETS", selected_template)
        
        shutil.copytree(selected_template_directory, new_widget_directory)
        
        sequence_index = self.load_sequence_combo.findText(self.create_widget_sequence_combo.currentText())
        self.load_sequence_combo.setCurrentIndex(sequence_index)
        
        number_index = self.load_number_combo.findText(f"{self.create_widget_sequence_combo.currentText()}_{new_sequence_number}")
        self.load_number_combo.setCurrentIndex(number_index)
        
        self.load_selected_widget()
        
    def save_widget(self):
        print("Saving widget...")
        python_file = open(self.python_filepath.text(), "w")
        python_file.write(self.python_edit.toPlainText())
        python_file.close()
        
        css_file = open(self.css_filepath.text(), "w")
        css_file.write(self.css_edit.toPlainText())
        css_file.close()
        
    def run_widget_from_editor(self):
        print("Refreshing widget...")
        self.save_widget()
        self.display_widget_preview()
        
    def _import_ui_as_module(self, widget_filename, widget_py_path):
        spec = importlib.util.spec_from_file_location(widget_filename, widget_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        ui_class = getattr(module, widget_filename)
        ui_instance = ui_class()

        return ui_instance
        
    def display_widget_preview(self):
        
        widget_py_path = self.python_filepath.text()
        
        css_filepath = self.css_filepath.text()
        with open(css_filepath) as file:
            css_data = file.read()
            
        imported_widget = self._import_ui_as_module("CustomWidget", widget_py_path)
        
        self.custom_thumbnail_widget = ThumbnailWidget(
                    widget_name=self.load_sequence_combo.currentText(),
                    widget_path=self.python_label,
                    css_data=css_data,
                    custom_widget=imported_widget, 
                    info_dict={},
                    width=200, 
                    height=100
                    )
        
        while self.preview_layout.count() > 1:
            item = self.preview_layout.takeAt(1)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
        self.preview_layout.addWidget(self.custom_thumbnail_widget, alignment=Qt.AlignCenter)
        
                        