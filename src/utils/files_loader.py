import json
import os

import yaml
from src.data.var import files


def file_loader(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            if file_path.endswith('.yaml') or file_path.endswith('.yml'):
                return yaml.safe_load(file)
            elif file_path.endswith('.json'):
                return json.load(file)
            else:
                raise ValueError("Unsupported file format")
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

def load_config():
    f = files['config']
    exemple_file = files['exemple_config']
    if not os.path.exists(f):
        return file_loader(exemple_file)
    else:
        return file_loader(f)