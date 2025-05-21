import config.defaults as defaults
import json
from pathlib import Path


def initialize_json(file_path, data):
    if not Path(file_path).exists():
        write_json(file_path, data)


def initialize_all_json():
    initialize_json("child_folders.json", defaults.child_folders)
    initialize_json("folder_extensions.json", defaults.folder_extensions)
    initialize_json("create_errors.json", None)
    initialize_json("sort_errors.json", None)
    initialize_json("unsort_errors.json", None)
    initialize_json("delete_errors.json", None)


def load_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def get_unique_path(original_file_path):
    counter = 1
    renamed_file_path = original_file_path
    while renamed_file_path.exists():
        renamed_file_path = original_file_path.with_stem(
            f"{original_file_path.stem}_{counter}")
        counter += 1
    return renamed_file_path


def append_rename_dict(renamed_files_list, original_file_path, renamed_file_path):
    if original_file_path != renamed_file_path:
        renamed_files_list.append(
            {"original": original_file_path.name, "renamed": renamed_file_path.name})


def append_error_dict(errors_list, directory, operation, error):
    errors_list.append({"directory": str(directory),
                       "operation": operation, "error": str(error)})
