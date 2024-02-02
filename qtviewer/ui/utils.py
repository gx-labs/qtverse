import os
import sys
import yaml

def read_yaml(filepath):
    info_yaml_file_path = filepath
    if os.path.exists(info_yaml_file_path):
        with open(info_yaml_file_path, 'r') as file:
            info_data = yaml.safe_load(file)
        return info_data
    return None

def qt_icon(filename):
    icon_directory = os.getenv("QT_ICON_PATH")
    resolved_icon_directory = os.path.abspath(os.path.join(icon_directory, filename))
    print(resolved_icon_directory)
    return resolved_icon_directory