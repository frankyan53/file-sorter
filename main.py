from cli import get_parent_folder_path
from logic import create_child_folders, move_files, unsort_files, delete_empty_folders


def main():
    parent_folder_path = get_parent_folder_path()
    if create_child_folders(parent_folder_path):
        print("Folders created successfully. Organizing files now...\n")
    else:
        print("Encountered error when creating folders. Exiting.")
        return
    source_files_list, report_dict, renamed_files_list, is_successful, move_files_errors_list = move_files(
        parent_folder_path)
    if not is_successful and move_files_errors_list:
        print(
            f"Failed to move any files. Encountered {len(move_files_errors_list)} error{"s" if len(move_files_errors_list) != 1 else ""}. See \"move_files_errors.json\" for more details.")
    elif is_successful and move_files_errors_list:
        print(
            f"Moved some files. Encountered {len(move_files_errors_list)} error{"s" if len(move_files_errors_list) != 1 else ""}. See \"move_files_errors.json\" for more details.")
    else:
        print("Files moved successfully.")
    if not source_files_list:
        print("No files available to sort.")
    else:
        print(f"{"Sort Report":=^40}")
        for child_folder, files_moved in report_dict.items():
            if files_moved > 0:
                print(
                    f"{files_moved} file{"s" if files_moved != 1 else ""} moved into {child_folder}.")
    for file in renamed_files_list:
        print(
            f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")
    renamed_files_list, is_successful, unsort_files_errors_list = unsort_files(
        parent_folder_path)
    if not is_successful and unsort_files_errors_list:
        print(
            f"Failed to unsort any files. Encountered {len(unsort_files_errors_list)} error{"s" if len(unsort_files_errors_list) != 1 else ""}. See \"unsort_files_errors.json\" for more details.")
    elif is_successful and unsort_files_errors_list:
        print(
            f"Moved some files. Encountered {len(unsort_files_errors_list)} error{"s" if len(unsort_files_errors_list) != 1 else ""}. See \"unsort_files_errors.json\" for more details.")
    else:
        print("Unsorted files successfully.")
    for file in renamed_files_list:
        print(
            f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")
    is_successful, delete_empty_folders_errors_list = delete_empty_folders(
        parent_folder_path)
    if not is_successful and delete_empty_folders_errors_list:
        print(
            f"Failed to delete any folders. Encountered {len(delete_empty_folders_errors_list)} error{"s" if len(delete_empty_folders_errors_list) != 1 else ""}. See \"delete_empty_folders_errors.json\" for more details.")
    elif is_successful and unsort_files_errors_list:
        print(
            f"Deleted some folders. Encountered {len(delete_empty_folders_errors_list)} error{"s" if len(delete_empty_folders_errors_list) != 1 else ""}. See \"delete_empty_folders_errors.json\" for more details.")
    else:
        print("Folders deleted successfully.")


if __name__ == "__main__":
    main()
