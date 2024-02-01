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

print(designer_data["developers"][0]["sequence_codes"])

all_sequence_codes = []

for dev in designer_data["developers"]:
        for codes in dev["sequence_codes"]:
                all_sequence_codes.append(codes)

print(all_sequence_codes)