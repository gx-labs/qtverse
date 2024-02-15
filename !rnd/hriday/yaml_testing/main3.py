import os
import sys
import yaml

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def read_yaml(filepath):
    info_yaml_file_path = filepath
    if os.path.exists(info_yaml_file_path):
        with open(info_yaml_file_path, 'r') as file:
            info_data = yaml.safe_load(file)
        return info_data
    return None

designer_config_file_path = os.path.join(os.path.dirname(__file__), "cfg.yaml")

designer_data = read_yaml(designer_config_file_path)

# print(designer_data["developers"].keys())
# print(designer_data["developers"].values())
# print(designer_data["widgets"]["default_widgets"])

all_developers = designer_data["developers"].keys()

print(all_developers[0])