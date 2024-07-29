import json
from pathlib import Path
from datetime import date


class FileHandler:

    def load(self):
        with open(self.path_to_folder / "save.json", 'r') as f:
            self.data_dict = json.load(f)

    def save(self, auto_save=True):

        if auto_save:
            with open(self.path_to_folder / "save.json", 'w') as f:
                f.write(json.dumps(self.data_dict))
        else:
            current_date = date.today()
            print(self.path_to_folder / f"save_file_{current_date.day}_{current_date.month}.json",)
            with open(self.path_to_folder / f"save_file_{current_date.day}_{current_date.month}.json", 'w') as f:
                f.write(json.dumps(self.data_dict))
            with open(self.path_to_folder / f"save.json", 'w') as f:
                f.write(json.dumps(self.data_dict))

    def __init__(self):
        self.data_dict = dict()
        if not (Path.cwd() / "savefiles").exists():
            (Path.cwd() / "savefiles").mkdir()
        self.path_to_folder = Path.cwd() / "savefiles"



#if __name__ == "__main__":

#    test_dict = {"Drinks": {"Cola": {"Quantity": 1, "Price": 5}}}

#    json_object = json.dumps(test_dict)

#    with open("savefiles/save.json", "w") as f:
#        f.write(json_object)

