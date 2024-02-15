import os
import sys
import shutil
import importlib.util

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.general_utils import read_yaml
from ui.general_utils import qt_icon
from ui.general_utils import read_python
from ui.general_utils import read_css

designer_config_file_path = os.path.join(os.path.dirname(__file__), "cfg", "designer.yaml")

class DesignerAppWidget(QWidget):
    def __init__(self):
        super(DesignerAppWidget, self).__init__()
        
        # Set variables for various paths        
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.abspath(os.path.join(self.current_dir, '..', '..'))
        self.widgets_src_dir = os.path.join(self.project_dir, "qtverse", "widgets", "src", "WIDGETS")
        self.widgets_dev_dir = os.path.join(self.project_dir, "qtverse", "widgets", "src", "WIDGETS_DEV")
        self.templates_dir = os.path.join(self.current_dir, "templates")
        
        # Store config in variable
        self.designer_config = read_yaml(designer_config_file_path)
                                
        # Store all developer names                                
        self.all_developers = self.designer_config["developers"].keys()
        
        # Get all sequence codes by iterating through sequence codes(list) for each developer in yaml
        self.all_sequence_codes = os.listdir(self.widgets_src_dir)
        try:
            self.all_sequence_codes.remove(".gitkeep")
        except ValueError:
            pass
                
        # Read default widget types from disk
        self.default_widget_types_list = os.listdir(os.path.join(self.templates_dir, "WIDGETS"))
        
        # Create WIDGETS_DEV folder if it doesnt exist
        if not os.path.exists(self.widgets_dev_dir):
            os.mkdir(self.widgets_dev_dir)
        # Create sequence folders in WIDGET_DEV based on sequences is WIDGETS folder
        for seq in self.all_sequence_codes:
            dev_sequences = os.listdir(self.widgets_dev_dir)
            if seq not in dev_sequences:
                os.mkdir(os.path.join(self.widgets_dev_dir, seq))
        
        # Store list of develop widget sequences in var        
        self.all_develop_sequence_codes = os.listdir(self.widgets_dev_dir)
        try:
            self.all_develop_sequence_codes.remove(".gitkeep")
        except ValueError:
            pass
        
        # --------------------------------------------------
        self.master_layout = QVBoxLayout()

        # Create frame for load and create section
        self.load_create_section_frame = QFrame()
        self.load_create_section_frame.setFrameShape(QFrame.StyledPanel)
        self.load_create_section_frame.setMaximumHeight(55)
        self.load_create_section_frame.setStyleSheet("QFrame{border: 1px solid lightgrey; border-radius: 2px} QLabel{border: none}")

        self.load_create_section_layout = QHBoxLayout(self.load_create_section_frame)
                
        # Load section label
        self.load_widget_label = QLabel('Load Widget ')
        
        # select dev or complete widgets
        self.load_complete_or_dev_widgets_cb = QComboBox()
        self.load_complete_or_dev_widgets_cb.addItem("Select Widgets Group")
        self.load_complete_or_dev_widgets_cb.addItem("Completed Widgets")
        self.load_complete_or_dev_widgets_cb.addItem("Development Widgets")
        self.load_complete_or_dev_widgets_cb.currentIndexChanged.connect(self.index_changed_update_load_widget_seq)
        
        # Select widget sequence cb
        self.load_widget_sequence_combo = QComboBox()
        self.load_widget_sequence_combo.addItem("Select a sequence")
        self.load_widget_sequence_combo.setEnabled(False)
        self.load_widget_sequence_combo.currentIndexChanged.connect(self.index_changed_update_load_widget_numbers)
                
        # Selec widget number cb
        self.load_widget_number_combo = QComboBox()
        self.load_widget_number_combo.setMinimumWidth(75)
        self.load_widget_number_combo.setEnabled(False)
        
        # Load button
        self.load_button = QPushButton("Load")
        self.load_button.setEnabled(False)
        self.load_button.setIcon(QIcon(qt_icon("load.png")))
        self.load_button.clicked.connect(self.clicked_load_selected_widget)
        
        # Reset button
        self.reset_button = QPushButton()
        self.reset_button.setIcon(QIcon(qt_icon("reset.png")))
        self.reset_button.clicked.connect(self.clicked_reset_widget_selection)

        # Create section label        
        self.create_widget_label = QLabel('Create Widget ')

        # Developer name cb
        self.create_widget_dev_combo = QComboBox()
        self.create_widget_dev_combo.setEnabled(False)
        self.create_widget_dev_combo.addItem("Select developer")
        self.create_widget_dev_combo.addItems(self.all_developers)
        self.create_widget_dev_combo.currentIndexChanged.connect(self.index_changed_update_dev_sequence_combo)
                
        # Widget sequence cb
        self.create_widget_sequence_combo = QComboBox()
        self.create_widget_sequence_combo.setEnabled(False)
        self.create_widget_sequence_combo.addItem("Select a sequence")
        self.create_widget_sequence_combo.addItems(self.all_sequence_codes)
            
        # Widget type cb
        self.create_widget_type_combo = QComboBox()
        self.create_widget_type_combo.setEnabled(False)
        self.create_widget_type_combo.addItems(self.default_widget_types_list)
                
        # Create button
        self.create_widget_button = QPushButton("Create")     
        self.create_widget_button.setEnabled(False)     
        self.create_widget_button.setIcon(QIcon(qt_icon("create.png")))  
        self.create_widget_button.clicked.connect(self.clicked_create_new_widget_from_template)          
        
        # Add widgets to load create section layout
        self.load_create_section_layout.addWidget(self.load_widget_label)
        self.load_create_section_layout.addWidget(self.load_complete_or_dev_widgets_cb)
        self.load_create_section_layout.addWidget(self.load_widget_sequence_combo)
        self.load_create_section_layout.addWidget(self.load_widget_number_combo)
        self.load_create_section_layout.addWidget(self.load_button)
        self.load_create_section_layout.addWidget(self.reset_button)
        self.load_create_section_layout.addStretch(1)
        self.load_create_section_layout.addWidget(self.create_widget_label)
        self.load_create_section_layout.addWidget(self.create_widget_dev_combo)
        self.load_create_section_layout.addWidget(self.create_widget_sequence_combo)
        self.load_create_section_layout.addWidget(self.create_widget_type_combo)
        self.load_create_section_layout.addWidget(self.create_widget_button)

        # --------------------------------------------------   
        # --------------------------------------------------   
        # --------------------------------------------------   
                
        # Create frame for edit and preview section
        self.css_py_preview_section_frame = QFrame()
        self.css_py_preview_section_frame.setFrameShape(QFrame.StyledPanel)
        self.css_py_preview_section_frame.setStyleSheet("QFrame{border: 1px solid lightgrey; border-radius: 2px} QLabel{border: none} QSplitter{border: none} QTextEdit{border: 1px solid lightgrey; border-radius: 1px}")
        
        # Horizontal layout for edit and preview section (designer section)   
        self.designer_section_layout = QHBoxLayout(self.css_py_preview_section_frame)
                
        # --------------------------------------------------   
        # --------------------------------------------------   
        
        self.css_section_layout = QVBoxLayout()
            
        # CSS section label
        self.css_section_label = QLabel('CSS')
        
        # CSS filepath label
        self.css_filepath_display_label = QLabel()
                
        # CSS editor 
        self.css_text_editor = QTextEdit()
        self.css_text_editor.setFontPointSize(11)
                
        # Add widgets to css section layout
        self.css_section_layout.addWidget(self.css_section_label)
        self.css_section_layout.addWidget(self.css_filepath_display_label)
        self.css_section_layout.addWidget(self.css_text_editor)
        
        # -------------------------------------------------- 
        # -------------------------------------------------- 
        
        # Vertical layout for python section
        self.python_section_layout = QVBoxLayout()
        
        # Horizontal layout for python section label and run, save buttons
        self.python_label_button_layout = QHBoxLayout()
            
        # Python section label
        self.python_section_label = QLabel('Python')
            
        # Run button
        self.python_run_button = QPushButton()
        self.python_run_button.setIcon(QIcon(qt_icon("run.png")))
        self.python_run_button.clicked.connect(self.clicked_run_widget_from_editor)
                
        # Save button
        self.python_save_button = QPushButton()
        self.python_save_button.setIcon(QIcon(qt_icon("save.png")))
        self.python_save_button.clicked.connect(self.clicked_save_widget)
        
        # Python filepath label
        self.python_filepath_display_label = QLabel()
                
        # Python editor
        self.python_text_editor = QTextEdit()
        self.python_text_editor.setFontPointSize(11)
        
        
        # Add layout and widgets to python section layout
        self.python_label_button_layout.addWidget(self.python_section_label)
        self.python_label_button_layout.addStretch(1)
        self.python_label_button_layout.addWidget(self.python_run_button)
        self.python_label_button_layout.addWidget(self.python_save_button)
        
        self.python_section_layout.addLayout(self.python_label_button_layout)
        self.python_section_layout.addWidget(self.python_filepath_display_label)
        self.python_section_layout.addWidget(self.python_text_editor)
        
        # Horizontal layout for css and python sections
        self.css_python_edit_layout = QHBoxLayout()
        self.css_python_edit_layout.addLayout(self.css_section_layout)
        self.css_python_edit_layout.addLayout(self.python_section_layout)
                
        # --------------------------------------------------   
        # --------------------------------------------------   
        
        # preview section
        self.widget_preview_layout = QVBoxLayout()
        self.widget_preview_layout.setAlignment(Qt.AlignTop)
                
        # section label
        self.preview_section_label = QLabel('Preview')
        # self.preview_section_label1 = QLabel('Preview')
        
        # adding widget to preview layout
        self.widget_preview_layout.addWidget(self.preview_section_label, alignment=Qt.AlignTop)
        # self.widget_preview_layout.addStretch()
        # self.widget_preview_layout.addWidget(self.preview_section_label1, alignment=Qt.AlignTop)
        
        # --------------------------------------------------   
        # --------------------------------------------------   
        
        self.designer_section_splitter = QSplitter()
        
        # Add empty widgets to splitter
        self.designer_section_splitter.addWidget(QWidget())
        self.designer_section_splitter.addWidget(QWidget())
        
        self.designer_section_splitter.setCollapsible(0, False)
        self.designer_section_splitter.setCollapsible(1, False)
        
        # Sets editor and preview layouts to widgets in splitter
        self.designer_section_splitter.widget(0).setLayout(self.css_python_edit_layout)
        self.designer_section_splitter.widget(1).setLayout(self.widget_preview_layout)
        
        self.designer_section_splitter.setSizes([QSizePolicy.Expanding, QSizePolicy.Fixed])
        
        # Size restrictions for splitter
        self.designer_section_splitter.widget(1).setMinimumWidth(250)
        self.designer_section_splitter.widget(1).setMaximumWidth(450)
        
        # Add splitter to designer section layout
        self.designer_section_layout.addWidget(self.designer_section_splitter)
        
        # --------------------------------------------------   

        # Set master layout
        self.setLayout(self.master_layout)
        self.master_layout.addWidget(self.load_create_section_frame)
        self.master_layout.addWidget(self.css_py_preview_section_frame)
        
    def index_changed_update_dev_sequence_combo(self, index):
        '''
        Enables and updates items in developer sequence cb in create widget section based on selected developer
        For example:
        selected developer      |       Developer sequences
        ------------------------|--------------------------
        Esha                    |       ESH
        Hriday                  |       HJH
        Preetish                |       PRT
        Sambhav                 |       SAM
        Shubham                 |       SHB
        Vishal                  |       VIS
        '''
        # Skip the placeholder item (Select a developer)
        if index != 0:  
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
            
    def index_changed_update_load_widget_seq(self, index):
        '''
        Handles the logic of previewing individual completed widgets or creating new widgets in the WIDGETS_DEV folder. 
        '''
        
        self.load_widget_sequence_combo.setEnabled(True)
        
        # If Completed Widgets is selected
        if index == 1:
            self.load_button.setEnabled(True)
            self.load_widget_sequence_combo.clear()
            self.load_widget_sequence_combo.addItem("Select a sequence")
            self.load_widget_sequence_combo.addItems(self.all_sequence_codes)
            self.create_widget_sequence_combo.setCurrentIndex(0)
            self.create_widget_sequence_combo.setEnabled(False)
            self.create_widget_type_combo.setCurrentIndex(0)
            self.create_widget_type_combo.setEnabled(False)
            self.create_widget_button.setEnabled(False)
        # If Develop Widgets is selected
        elif index == 2:
            self.load_button.setEnabled(True)
            self.load_widget_sequence_combo.clear()
            self.load_widget_sequence_combo.addItem("Select a sequence")
            self.load_widget_sequence_combo.addItems(self.all_develop_sequence_codes)
            self.create_widget_sequence_combo.setEnabled(True)
            self.create_widget_type_combo.setEnabled(True)
            self.create_widget_button.setEnabled(True)
        else:
            self.load_button.setEnabled(False)
            self.load_widget_sequence_combo.setCurrentIndex(0)
            self.load_widget_sequence_combo.setEnabled(False)
            self.create_widget_sequence_combo.setCurrentIndex(0)
            self.create_widget_sequence_combo.setEnabled(False)
            self.create_widget_type_combo.setCurrentIndex(0)
            self.create_widget_type_combo.setEnabled(False)
            self.create_widget_button.setEnabled(False)
            

                        
    def index_changed_update_load_widget_numbers(self, index):
        '''
        Enables and updates the widget numbers cb in the load widget section depending on the selection made
        in the sequence selection cb
        For example:
        Selected Sequence       |       Widgets
        ------------------------|-----------------------
        ESH                     |       ESH_001, ESH_002, ESH_003, ESH_004
        HJH                     |       HJH_001, HJH_002, HJH_003, HJH_004
        '''
        # Skip the placeholder item (Select a sequence)
        if index > 0:
            # set correct path (WIDGETS or WIDGETS_DEV based on cb selection)
            if self.load_complete_or_dev_widgets_cb.currentIndex() == 1:
                sequence = self.all_sequence_codes[index - 1]
                sequence_dir = os.path.join(self.widgets_src_dir, sequence)
                widgets_list = os.listdir(sequence_dir)
            elif self.load_complete_or_dev_widgets_cb.currentIndex() == 2:
                sequence = self.all_develop_sequence_codes[index - 1]
                sequence_dir = os.path.join(self.widgets_dev_dir, sequence)
                widgets_list = os.listdir(sequence_dir)
            
            if widgets_list:
                self.load_widget_number_combo.setEnabled(True)
                self.load_widget_number_combo.clear()
                self.load_widget_number_combo.addItems(widgets_list)
            else:
                self.load_widget_number_combo.clear()
                self.load_widget_number_combo.setEnabled(False)
        else:
            self.load_widget_number_combo.clear()
            self.load_widget_number_combo.setEnabled(False)
            
    def clicked_load_selected_widget(self):
        '''
        Called when load button is clicked or when a new widget is created from temaplate.
        Sets path variables based on selection in cb and loads css and py files to display in the editor
        and displays the filepaths in the respective labels
        '''
        print("Loading selected widget...")
        
        # Clears previously displayed preview widget if any
        self.clear_preview_widget()
        
        # Checks if the selected cb item is the first(placehodler) item
        if self.load_widget_sequence_combo.currentIndex() != 0:
            print(f"load seq combo: {self.load_widget_sequence_combo.currentIndex()}")
            
            # Sets path variables (WIDGETS or WIDGETS_DEV) based on cb selection
            if self.load_complete_or_dev_widgets_cb.currentIndex() == 1:
                selected_widget_dir = os.path.join(self.widgets_src_dir, self.load_widget_sequence_combo.currentText())
                selected_widget_seq_dir = os.path.join(selected_widget_dir, self.load_widget_number_combo.currentText(), "widget")
            elif self.load_complete_or_dev_widgets_cb.currentIndex() == 2:
                selected_widget_dir = os.path.join(self.widgets_dev_dir, self.load_widget_sequence_combo.currentText())
                selected_widget_seq_dir = os.path.join(selected_widget_dir, self.load_widget_number_combo.currentText(), "widget")
                
            
            # Sets py data in a var. Display py in textedit and filepath in label
            python_data = read_python(selected_widget_seq_dir)
            self.python_text_editor.setText(python_data)
            self.python_filepath_display_label.setText(f"{selected_widget_seq_dir}\CustomWidget.py")
            
            # Sets css data in a var. Display css in textedit and filepath in label
            css_data = read_css(selected_widget_seq_dir)
            self.css_text_editor.setText(css_data)
            self.css_filepath_display_label.setText(f"{selected_widget_seq_dir}\style.css")
            
            self.display_widget_preview()
        
        # If item selected is the placeholder, clear the fields    
        else:
            self.python_text_editor.setText("")
            self.python_filepath_display_label.setText("")
            
            self.css_text_editor.setText("")
            self.css_filepath_display_label.setText("")
            
    def clear_preview_widget(self):
        '''
        Deletes the preview widget when new widget is loaded or reset button is clicked. Handles error
        if no preview widget is present.
        '''
        try:
            self.preview_widget.deleteLater()
        except (AttributeError, RuntimeError):
            pass
            
    def clicked_reset_widget_selection(self):
        '''
        Called when reset button is pressed. Resets load cb, py and css editors and filepath labels
        clears the widget from the preview section.
        '''
        print("Reset selection")

        self.load_widget_sequence_combo.setCurrentIndex(0)
        
        self.css_filepath_display_label.setText("")
        self.css_text_editor.setText("")
        
        self.python_filepath_display_label.setText("")
        self.python_text_editor.setText("")

        self.clear_preview_widget()
        
    def clicked_create_new_widget_from_template(self):
        '''
        Called when create button is clicked. Checks disk for existing widgets in a sequence. Gets the next number in
        the sequence and makes a copy of the selected template widget into the correct sequence folder with the correct
        sequence number.
        '''
        
        if self.create_widget_sequence_combo.currentIndex() != 0:
            # Call function to reset and clear any previous widget/selection
            self.clicked_reset_widget_selection()
            
            print(f"Creating new {self.create_widget_type_combo.currentText()} widget...")
            
            # Build file path based on selected sequence
            selected_sequence_path = os.path.join(self.widgets_dev_dir, self.create_widget_sequence_combo.currentText())
            
            # Check if the selected sequence exists on disk
            if not os.path.exists(selected_sequence_path):
                # Create a dialog box if selected sequence doesnt exist on disk
                sequence_err_dialog = CustomDialog(self)
                if sequence_err_dialog.exec_():
                    # If "OK" is selected in dialog box, new directory is created and cb is updated
                    os.mkdir(os.path.join(self.widgets_src_dir, self.create_widget_sequence_combo.currentText()))
                    self.update_load_widget_seq_cb()
                    self.index_changed_update_load_widget_numbers(self.load_widget_number_combo.currentIndex())   
                else:
                    print("Cancel!")
                    

            # Calculate the next widget number in a sequence & assign new directory path to var
            completed_widgets_path = os.path.join(self.widgets_src_dir, self.create_widget_sequence_combo.currentText())

            try:
                if not os.listdir(selected_sequence_path):
                    last_widget_in_sequence = os.listdir(completed_widgets_path)[-1]
                else:
                    last_widget_in_sequence = os.listdir(selected_sequence_path)[-1]
                    
                last_widget_number = int(last_widget_in_sequence[-3:])
                new_widget_number = str(last_widget_number + 1).zfill(3)
            except IndexError:
                new_widget_number = "001"
                pass
            
            new_widget_directory = os.path.join(selected_sequence_path, f"{self.create_widget_sequence_combo.currentText()}_{new_widget_number}")

            # Get selected default widget and assign correct template path to var
            selected_default_widget_template = self.create_widget_type_combo.currentText()
            selected_default_widget_template_directory = os.path.join(self.templates_dir, "WIDGETS", selected_default_widget_template)
            
            # Make a copy of template widget in new directory
            shutil.copytree(selected_default_widget_template_directory, new_widget_directory)
            
            # Set correct sequence in load section sequence cb
            sequence_combo_index = self.load_widget_sequence_combo.findText(self.create_widget_sequence_combo.currentText())
            self.load_widget_sequence_combo.setCurrentIndex(sequence_combo_index)
            
            # Set correct widget number in load section widget number cb
            widget_number_combo_index = self.load_widget_number_combo.findText(f"{self.create_widget_sequence_combo.currentText()}_{new_widget_number}")
            self.load_widget_number_combo.setCurrentIndex(widget_number_combo_index)
            
            # Call function to load new widget
            self.clicked_load_selected_widget()
        
    def clicked_save_widget(self):
        '''
        Called when save button is clicked. Writes contents of text edit boxes to the correct file.
        '''
        print("Saving widget...")
        
        # Write content of py textedit box to correct py file
        python_file = open(self.python_filepath_display_label.text(), "w")
        python_file.write(self.python_text_editor.toPlainText())
        python_file.close()
        
        # Write content of css textedit box to correct css file       
        css_file = open(self.css_filepath_display_label.text(), "w")
        css_file.write(self.css_text_editor.toPlainText())
        css_file.close()
        
    def clicked_run_widget_from_editor(self):
        '''
        Called when run button is clicked. First saves the css and py to the correct file and reloads the widget in
        preview window.
        '''
        print("Refreshing widget...")
        self.clear_preview_widget()
        self.clicked_save_widget()
        self.display_widget_preview()
        
    def _import_widget_as_module(self, widget_filename, widget_py_path):
        '''
        Creates an instance of the selected widget to be able to display in the preview window
        '''
        spec = importlib.util.spec_from_file_location(widget_filename, widget_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        ui_class = getattr(module, widget_filename)
        ui_instance = ui_class()
        self.custom_widget_class = widget_filename

        return ui_instance
        
    def display_widget_preview(self):
        '''
        Displays the widget instance in the preview window
        '''
        widget_py_path = self.python_filepath_display_label.text()

        try:        
            self.preview_widget = self._import_widget_as_module(widget_filename="CustomWidget", 
                                                            widget_py_path=widget_py_path)
        except FileNotFoundError as err:
            selected_widget = self.load_widget_number_combo.currentText()
            button = QMessageBox.warning(self, "File Not Found!", f"{str(err)}\n\nWidget {selected_widget} is missing!")
            if button == QMessageBox.Ok:
                print("Abort!")
            self.clicked_reset_widget_selection()
            return

        self.widget_preview_layout.addWidget(self.preview_widget)
        
    def update_load_widget_seq_cb(self):
        '''
        Updates the load widget sequence combo box
        '''
        self.all_sequence_codes = os.listdir(self.widgets_src_dir)
        try:
            self.all_sequence_codes.remove(".gitkeep")
        except ValueError:
            pass
        self.load_widget_sequence_combo.clear()
        self.load_widget_sequence_combo.addItem("Select a sequence")
        self.load_widget_sequence_combo.addItems(self.all_sequence_codes)
        


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Sequence Not Found!")

        dialog_buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(dialog_buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        
        dialog_message = QLabel(f"Could not find sequence \"{parent.create_widget_sequence_combo.currentText()}\" for {parent.create_widget_dev_combo.currentText()}.\nWould you like to create one?")
        
        self.layout.addWidget(dialog_message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        
                        