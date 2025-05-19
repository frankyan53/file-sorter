import shutil
from pathlib import Path
from utils import load_json, write_json, append_rename_dict, append_error_dict, get_unique_path


def create_folders(parent_folder_path):
    is_successful = False
    create_folders_errors = []
    child_folders = load_json("child_folders.json")
    for folder in child_folders:
        child_folder_path = parent_folder_path / folder
        try:
            child_folder_path.mkdir(exist_ok=True)
            is_successful = True
        except Exception as error:
            append_error_dict(create_folders_errors,
                              parent_folder_path, "creating folders", error)
    return is_successful, create_folders_errors


def sort_files(parent_folder_path):
    has_source_files = False
    folder_extensions = load_json("folder_extensions.json")
    report = {
        child_folder: 0 for child_folder in folder_extensions}
    renamed_files = []
    is_successful = False
    sort_errors = []
    try:
        parent_files = parent_folder_path.iterdir()
    except Exception as error:
        append_error_dict(sort_errors, parent_folder_path,
                          "iterating through folder", error)
        return has_source_files, report, renamed_files, is_successful, sort_errors
    for source_file_path in parent_files:
        if source_file_path.is_dir():
            continue
        has_source_files = True
        for folder, extensions in folder_extensions.items():
            if source_file_path.suffix in extensions:
                child_folder = folder
                destination_file_path = (
                    source_file_path.parent / child_folder / source_file_path.name)
                break
        else:
            child_folder = "Other"
            destination_file_path = (
                source_file_path.parent / child_folder / source_file_path.name)
        renamed_destination_file_path = get_unique_path(destination_file_path)
        try:
            shutil.move(source_file_path, renamed_destination_file_path)
            is_successful = True
            append_rename_dict(
                renamed_files, destination_file_path, renamed_destination_file_path)
            report[child_folder] += 1
        except Exception as error:
            append_error_dict(sort_errors,
                              source_file_path, "moving file", error)
    write_json("sort_errors.json", sort_errors)
    return has_source_files, report, renamed_files, is_successful, sort_errors


def unsort_files(parent_folder_path):
    renamed_files = []
    is_successful = False
    unsort_errors = []
    child_folders = load_json("child_folders.json")
    for folder in child_folders:
        child_folder_path = parent_folder_path / folder
        if child_folder_path.exists():
            try:
                destination_files = child_folder_path.iterdir()
            except Exception as error:
                append_error_dict(
                    unsort_errors, parent_folder_path, "iterating through folder", error)
                continue
            for destination_file_path in destination_files:
                original_source_file_path = parent_folder_path / destination_file_path.name
                renamed_source_file_path = get_unique_path(
                    original_source_file_path)
                try:
                    shutil.move(destination_file_path,
                                renamed_source_file_path)
                    is_successful = True
                except Exception as error:
                    append_error_dict(
                        unsort_errors, destination_file_path, "moving file", error)
                    continue
                append_rename_dict(
                    renamed_files, original_source_file_path, renamed_source_file_path)
            try:
                child_folder_path.rmdir()
            except Exception as error:
                append_error_dict(unsort_errors,
                                  child_folder_path, "deleting folder", error)
        else:
            continue
    write_json("unsort_errors.json", unsort_errors)
    return renamed_files, is_successful, unsort_errors


def delete_empty_folders(parent_folder_path):
    is_successful = False
    delete_errors = []
    child_folders = load_json("child_folders.json")
    for folder in child_folders:
        child_folder_path = parent_folder_path / folder
        try:
            destination_files = child_folder_path.iterdir()
        except Exception as error:
            append_error_dict(
                delete_errors, child_folder_path, "iterating through folder", error)
            continue
        if not list(destination_files):
            try:
                child_folder_path.rmdir()
                is_successful = True
            except Exception as error:
                append_error_dict(delete_errors,
                                  child_folder_path, "deleting folder", error)
    write_json("delete_errors.json", delete_errors)
    return is_successful, delete_errors
