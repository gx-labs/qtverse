import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
from PySide2.QtCore import Qt
import yaml
import os

class DeveloperApp(QWidget):
        def __init__(self):
                super().__init__()

                self.init_ui()

        def init_ui(self):
                layout = QVBoxLayout()
                
                script_directory = os.path.dirname(os.path.realpath(__file__))
                yaml_path = os.path.join(script_directory, 'cfg.yaml')

                # Read YAML file
                try:
                        with open(yaml_path, 'r') as file:
                                data = yaml.safe_load(file)
                                developers = data.get('developers', [])
                                names = [dev['name'] for dev in developers]
                                sequence_codes = {dev['name']: dev['sequence_codes'] for dev in developers}
                except (FileNotFoundError, yaml.YAMLError) as e:
                        print(f"Error reading YAML file: {e}")
                        names = []
                        sequence_codes = {}

                # Create combo boxes for developer and sequence
                developer_combo_box = QComboBox()
                developer_combo_box.addItem("Select a developer") # Placeholder
                developer_combo_box.addItems(names)
                developer_combo_box.currentIndexChanged.connect(self.update_sequence_label)

                sequence_combo_box = QComboBox()
                sequence_combo_box.setEnabled(False)

                layout.addWidget(developer_combo_box)
                layout.addWidget(sequence_combo_box)

                self.setLayout(layout)
                self.setWindowTitle('yaml Test')
                self.show()

                self.names = names
                self.sequence_codes = sequence_codes
                self.sequence_combo_box = sequence_combo_box

        def update_sequence_label(self, index):
                if index > 0:  # Skip the placeholder item
                        selected_developer = self.names[index - 1]  # Adjust index to skip the placeholder
                        sequence_codes = self.sequence_codes.get(selected_developer, [])
                        self.sequence_combo_box.setEnabled(True)
                        self.sequence_combo_box.clear()
                        self.sequence_combo_box.addItems(sequence_codes)
                else:
                        self.sequence_combo_box.clear()
                        self.sequence_combo_box.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeveloperApp()
    sys.exit(app.exec_())
