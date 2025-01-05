import os

from src.data.var import files, folders
from src.utils.files_loader import file_loader


class Creator:
    def __init__(self):
        self.create_folders(folders["config"])
        self.create_file(files["config"], file_loader(files["exemple_config"]))

    def create_folders(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        return False

    def create_file(self, path, content):
        if not os.path.exists(path):
            import json

            import yaml
            if path.endswith('.yaml') or path.endswith('.yml'):
                content = yaml.dump(content)
            elif path.endswith('.json'):
                content = json.dumps(content, indent=4)
            else:
                raise ValueError("Unsupported file format")
            with open(path, 'w') as file:
                file.write(content)
                return True
            return False