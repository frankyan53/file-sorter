import json
import shutil
from pathlib import Path


def get_unique_path(destination_file_path):
    counter = 1
    while destination_file_path.exists():
        destination_file_path = destination_file_path.with_stem(
            f"{destination_file_path.stem}_{counter}")
        counter += 1
    return destination_file_path


def create_child_folders(parent_folder_path):
    with open("child_folders.json") as file:
        child_folders_list = json.load(file)
    try:
        for folder in child_folders_list:
            child_folder_path = parent_folder_path / folder
            child_folder_path.mkdir(exist_ok=True)
        return True
    except Exception:
        return False


def move_files(parent_folder_path):
    with open("child_folder_extensions.json") as file:
        child_folder_extensions_dict = json.load(file)
    report = {
        child_folder: 0 for child_folder in child_folder_extensions_dict}
    for source_file_path in parent_folder_path.iterdir():
        if source_file_path.is_dir():
            continue
        for child_folder, child_folder_extensions in child_folder_extensions_dict.items():
            if source_file_path.suffix in child_folder_extensions:
                destination_file_path = (
                    source_file_path.parent / child_folder / source_file_path.name)
                destination_file_path = get_unique_path(destination_file_path)
                shutil.move(source_file_path, destination_file_path)
                report[child_folder] += 1
                break
        else:
            destination_file_path = source_file_path.parent / "Other" / source_file_path.name
            shutil.move(source_file_path, destination_file_path)
            report["Other"] += 1
    return report
