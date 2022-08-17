import json
import os
import CreateDirectories
import ValidateJsonFile


def view_json():
    ValidateJsonFile.is_dir_empty()
    for file in os.listdir(CreateDirectories.import_path):
        if file.endswith(".json"):
            os.system("CLS")
            print(f'There are {len(os.listdir(CreateDirectories.import_path))} JSON files in the directory.')
            print(f'\nViewing {file}\n')
            x = os.path.join(CreateDirectories.import_path, file)
            with open(x, 'r') as f:
                data = json.load(f)
                pretty_data = json.dumps(data, indent=4)
            print(pretty_data)
            os.system("pause")
