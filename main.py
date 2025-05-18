from cli import get_parent_folder_path
from logic import create_child_folders, move_files


def main():
    parent_folder_path = get_parent_folder_path()
    if create_child_folders(parent_folder_path):
        print("Folders created successfully. Organizing files now...\n")
    else:
        print("Encountered error when creating folders. Exiting.")
        return
    source_files, report_dict, renamed_files_list = move_files(
        parent_folder_path)
    if not source_files:
        print("No files to sort.")
    for child_folder, files_moved in report_dict.items():
        if files_moved > 0:
            print(f"{"Sort Report":=^40}")
            print(
                f"{files_moved} file{"s" if files_moved != 1 else ""} moved into {child_folder}.")
    for file in renamed_files_list:
        print(
            f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")


if __name__ == "__main__":
    main()
