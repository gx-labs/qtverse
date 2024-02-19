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
    # print(resolved_icon_directory)
    return resolved_icon_directory

def read_python(filepath):
    widget_python_filepath = filepath
    if os.path.exists(widget_python_filepath):
        try:
            with open(f"{widget_python_filepath}\CustomWidget.py", 'r') as f:
                python_data = f.read()
            return python_data
        except FileNotFoundError:
            print(f"{widget_python_filepath} seems to be empty.")
            pass
    return None

def read_css(filepath):
    widget_css_filepath = filepath
    if os.path.exists(widget_css_filepath):
        try:
            with open(f"{widget_css_filepath}\style.css", 'r') as f:
                css_data = f.read()
            return css_data
        except FileNotFoundError:
            print(f"{widget_css_filepath} seems to be empty.")
            pass
    return None