import yaml, json, os

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