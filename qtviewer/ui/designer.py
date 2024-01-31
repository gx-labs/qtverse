import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DesignerAppWidget(QWidget):
    def __init__(self):
        super(DesignerAppWidget, self).__init__()
        
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.load_create_groupbox = QGroupBox()
        self.load_create_groupbox.setMaximumHeight(50)
        self.load_create_groupbox_layout = QHBoxLayout()
        self.load_create_groupbox.setLayout(self.load_create_groupbox_layout)
        
        self.load_widget_label = QLabel('Load Widget: ')
        self.load_create_groupbox_layout.addWidget(self.load_widget_label)
        
        self.load_sequence_combo = QComboBox()
        self.load_create_groupbox_layout.addWidget(self.load_sequence_combo)
        
        self.load_number_combo = QComboBox()
        self.load_create_groupbox_layout.addWidget(self.load_number_combo)
        
        self.load_button = QPushButton('Load')
        self.load_create_groupbox_layout.addWidget(self.load_button)
        
        self.load_create_groupbox_layout.addSpacing(60)
        
        self.create_widget_label = QLabel('Create New Widget from Template: ')
        self.load_create_groupbox_layout.addWidget(self.create_widget_label)
        
        self.create_widget_type_combo = QComboBox()
        self.load_create_groupbox_layout.addWidget(self.create_widget_type_combo)
        
        self.create_widget_dev_combo = QComboBox()
        self.load_create_groupbox_layout.addWidget(self.create_widget_dev_combo)
        
        self.create_widget_sequence_combo = QComboBox()
        self.load_create_groupbox_layout.addWidget(self.create_widget_sequence_combo)
        
        self.create_widget_button = QPushButton('Create')        
        self.load_create_groupbox_layout.addWidget(self.create_widget_button)
        
        self.main_layout.addWidget(self.load_create_groupbox)
        
        self.designer_groupbox = QGroupBox()
        self.main_layout.addWidget(self.designer_groupbox)
        
        self.designer_layout = QHBoxLayout()
        self.designer_groupbox.setLayout(self.designer_layout)
        
        self.css_groupbox = QGroupBox()
        self.designer_layout.addWidget(self.css_groupbox)
        
        self.css_layout = QVBoxLayout()
        self.css_groupbox.setLayout(self.css_layout)
        
        self.css_label = QLabel('CSS')
        self.css_layout.addWidget(self.css_label)
        
        self.css_edit = QTextEdit()
        self.css_layout.addWidget(self.css_edit)
        
        self.python_groupbox = QGroupBox()
        self.designer_layout.addWidget(self.python_groupbox)
        
        self.python_layout = QVBoxLayout()
        self.python_groupbox.setLayout(self.python_layout)
        
        self.python_run_layout = QHBoxLayout()
        self.python_layout.addLayout(self.python_run_layout)
        
        self.python_label = QLabel('Python')
        self.python_run_layout.addWidget(self.python_label)
        
        self.python_run_button = QPushButton('Run')
        self.python_run_layout.addWidget(self.python_run_button)
        
        self.python_save_button = QPushButton('Save')
        self.python_run_layout.addWidget(self.python_save_button)
        
        self.python_edit = QTextEdit()
        self.python_layout.addWidget(self.python_edit)
        
        self.preview_groupbox = QGroupBox()
        self.preview_groupbox.setMaximumWidth(500)
        self.preview_groupbox.setMinimumWidth(300)
        self.designer_layout.addWidget(self.preview_groupbox)
        
        self.preview_layout = QVBoxLayout()
        self.preview_groupbox.setLayout(self.preview_layout)
        self.preview_layout.setAlignment(Qt.AlignTop)
        
        self.preview_label = QLabel('Preview')
        self.preview_layout.addWidget(self.preview_label)
        
        