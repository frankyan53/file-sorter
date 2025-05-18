import json
import shutil
from pathlib import Path


def get_unique_path(original_destination_file_path):
    counter = 1
    renamed_destination_file_path = original_destination_file_path
    while renamed_destination_file_path.exists():
        renamed_destination_file_path = original_destination_file_path.with_stem(
            f"{original_destination_file_path.stem}_{counter}")
        counter += 1
    return renamed_destination_file_path


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
    renamed_files_list = []
    with open("child_folder_extensions.json") as file:
        child_folder_extensions_dict = json.load(file)
    report_dict = {
        child_folder: 0 for child_folder in child_folder_extensions_dict}
    source_files_list = []
    move_files_errors = []
    try:
        parent_files_gen = parent_folder_path.iterdir()
    except Exception as error:
        move_files_errors.append({"directory": str(parent_folder_path),
                                  "operation": "iterating through folder", "error": str(error)})
        return source_files_list, report_dict, renamed_files_list, errors
    for source_file_path in parent_files_gen:
        if source_file_path.is_dir():
            continue
        source_files_list.append(source_file_path)
        for child_folder, child_folder_extensions in child_folder_extensions_dict.items():
            if source_file_path.suffix in child_folder_extensions:
                child_folder_name = child_folder
                original_destination_file_path = (
                    source_file_path.parent / child_folder_name / source_file_path.name)
                break
        else:
            child_folder_name = "Other"
            original_destination_file_path = (
                source_file_path.parent / child_folder_name / source_file_path.name)
        try:
            renamed_destination_file_path = get_unique_path(
                original_destination_file_path)
        except Exception as error:
            move_files_errors.append({"directory": str(
                original_destination_file_path), "operation": "renaming file", "error": str(error)})
            continue
        try:
            shutil.move(source_file_path, renamed_destination_file_path)
            if original_destination_file_path != renamed_destination_file_path:
                renamed_files_list.append(
                    {"original": original_destination_file_path.name, "renamed": renamed_destination_file_path.name})
            report_dict[child_folder_name] += 1
        except Exception as error:
            move_files_errors.append({"source_directory": str(source_file_path), "destination_directory":
                                      str(renamed_destination_file_path), "operation": "moving file", "error": str(error)})
    with open("move_files_errors.json", "w") as file:
        json.dump(move_files_errors, file, indent=4)
    return source_files_list, report_dict, renamed_files_list, move_files_errors


def unsort_files(parent_folder_path):
    renamed_files_list = []
    unsort_files_errors = []
    with open("child_folders.json") as file:
        child_folders_list = json.load(file)
    for folder in child_folders_list:
        child_folder_path = parent_folder_path / folder
        if child_folder_path.exists():
            try:
                child_files_gen = child_folder_path.iterdir()
            except Exception as error:
                unsort_files_errors.append({"directory": str(
                    parent_folder_path), "operation": "iterating through folder", "error": str(error)})
                return renamed_files_list, unsort_files_errors
            for destination_file_path in child_files_gen:
                original_source_file_path = parent_folder_path / destination_file_path.name
                try:
                    renamed_source_file_path = get_unique_path(
                        original_source_file_path)
                except Exception as error:
                    unsort_files_errors.append(
                        {"directory": str(original_source_file_path), "operation": "renaming file", "error": str(error)})
                    continue
                try:
                    shutil.move(destination_file_path,
                                renamed_source_file_path)
                except Exception as error:
                    unsort_files_errors.append({"source_directory": str(destination_file_path), "destination_directory": str(
                        renamed_source_file_path), "operation": "moving file", "error": str(error)})
                    continue
                if original_source_file_path != renamed_source_file_path:
                    renamed_files_list.append(
                        {"original": original_source_file_path.name, "renamed": renamed_source_file_path.name})
            try:
                child_folder_path.rmdir()
            except Exception as error:
                unsort_files_errors.append({"directory": str(
                    child_folder_path), "operation": "deleting folder", "error": str(error)})
        else:
            continue
    with open("unsort_files_errors.json", "w") as file:
        json.dump(unsort_files_errors, file, indent=4)
    return renamed_files_list, unsort_files_errors
