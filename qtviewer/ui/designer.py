import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.utils import read_yaml

designer_config_file_path = os.path.join(os.path.dirname(__file__), "cfg", "designer.yaml")

widget_types = ["QPushButton", "QRadioButton", "QComboBox", "QLineEdit", "QProgressBar", "QToolTip", "QGroupBox"]
class DesignerAppWidget(QWidget):
        def __init__(self):
                super(DesignerAppWidget, self).__init__()
                
                designer_data = read_yaml(designer_config_file_path)
                self.designer_data = designer_data
                
                all_developers = []
                all_sequence_codes = []
                
                for dev in designer_data["developers"]:
                        all_developers.append(dev["name"])
                        all_sequence_codes.append(dev["sequence_codes"])
                                
                self.all_developers = all_developers
                self.all_sequence_codes = []
                
                for seq in all_sequence_codes:
                        for code in seq:
                                self.all_sequence_codes.append(code)
                                
                print(self.all_sequence_codes)
                
                self.main_layout = QVBoxLayout()
                self.setLayout(self.main_layout)
                
                self.load_create_groupbox = QGroupBox()
                self.load_create_groupbox.setMaximumHeight(50)
                self.load_create_groupbox_layout = QHBoxLayout()
                self.load_create_groupbox.setLayout(self.load_create_groupbox_layout)
                
                self.load_widget_label = QLabel('Load Widget: ')
                self.load_create_groupbox_layout.addWidget(self.load_widget_label)
                
                self.load_sequence_combo = QComboBox()
                self.load_sequence_combo.addItem("Select a sequence")
                self.load_sequence_combo.addItems(self.all_sequence_codes)
                self.load_create_groupbox_layout.addWidget(self.load_sequence_combo)
                
                self.load_number_combo = QComboBox()
                self.load_number_combo.setEnabled(False)
                self.load_create_groupbox_layout.addWidget(self.load_number_combo)
                
                self.load_button = QPushButton('Load')
                self.load_create_groupbox_layout.addWidget(self.load_button)
                
                self.load_create_groupbox_layout.addSpacing(60)
                
                self.create_widget_label = QLabel('Create New Widget from Template: ')
                self.load_create_groupbox_layout.addWidget(self.create_widget_label)
                
                self.create_widget_type_combo = QComboBox()
                self.create_widget_type_combo.addItems(widget_types)
                self.load_create_groupbox_layout.addWidget(self.create_widget_type_combo)
                
                self.create_widget_dev_combo = QComboBox()
                self.create_widget_dev_combo.addItem("Select developer")
                self.create_widget_dev_combo.addItems(all_developers)
                self.create_widget_dev_combo.currentIndexChanged.connect(self.update_sequence_label)
                self.load_create_groupbox_layout.addWidget(self.create_widget_dev_combo)
                
                self.create_widget_sequence_combo = QComboBox()
                self.create_widget_sequence_combo.setEnabled(False)
                self.load_create_groupbox_layout.addWidget(self.create_widget_sequence_combo)
                
                self.create_widget_button = QPushButton('Create')        
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
                
                self.css_edit = QTextEdit()
                self.css_edit.setMaximumWidth(700)
                self.css_layout.addWidget(self.css_edit)
                
                self.python_layout = QVBoxLayout()
                self.designer_layout.addLayout(self.python_layout)
                
                self.python_run_layout = QHBoxLayout()
                self.python_layout.addLayout(self.python_run_layout)
                
                self.python_label = QLabel('Python')
                self.python_run_layout.addWidget(self.python_label)
                
                self.python_run_button = QPushButton('Run')
                self.python_run_layout.addWidget(self.python_run_button)
                
                self.python_save_button = QPushButton('Save')
                self.python_run_layout.addWidget(self.python_save_button)
                
                self.python_edit = QTextEdit()
                self.python_edit.setMaximumWidth(700)
                self.python_layout.addWidget(self.python_edit)
                
                self.preview_layout = QVBoxLayout()
                self.preview_layout.setAlignment(Qt.AlignTop)
                self.designer_layout.addLayout(self.preview_layout)
                
                self.preview_label = QLabel('Preview')
                self.preview_layout.addWidget(self.preview_label)
        
        def update_sequence_label(self, index, seq_combo_box):
                if index > 0:  # Skip the placeholder item
                        selected_developer = self.all_developers[index - 1]  # Adjust index to skip the placeholder
                        sequence_codes = [dev["sequence_codes"] for dev in self.designer_data["developers"] if dev["name"] == selected_developer]
        
                        if sequence_codes:
                                sequence_codes = sequence_codes[0]
                                self.create_widget_sequence_combo.setEnabled(True)
                                self.create_widget_sequence_combo.clear()
                                self.create_widget_sequence_combo.addItems(sequence_codes)
                        else:
                                self.create_widget_sequence_combo.clear()
                                self.create_widget_sequence_combo.setEnabled(False)
                else:
                        self.create_widget_sequence_combo.clear()
                        self.create_widget_sequence_combo.setEnabled(False)
