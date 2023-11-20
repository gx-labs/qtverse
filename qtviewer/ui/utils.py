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