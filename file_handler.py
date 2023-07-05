import json
from pathlib import Path

class FileHandler:

    def read(self):
        with open(self.path_to_folder / "save_file.json", 'r') as f:
            self.data_dict = json.load(f)

    def save(self):
        with open(self.path_to_folder / "save_file.json", 'w') as f:
            f.write(json.dumps(self.data_dict))

    def __init__(self, path_to_folder: Path):
        self.path_to_folder = path_to_folder
        self.data_dict = dict()

if __name__ == "__main__":

    test_dict = {"Drink": {"Cola": 1}}

    json_object = json.dumps(test_dict)

    with open("savefiles/save.json", "w") as f:
        f.write(json_object)