from cli import get_parent_folder_path
from logic import create_child_folders, move_files


def main():
    parent_folder_path = get_parent_folder_path()
    if create_child_folders(parent_folder_path):
        print("Folders created successfully. Organizing files now...\n")
    else:
        print("Encountered error when creating folders. Exiting.")
        return
    report_dict = move_files(parent_folder_path)[0]
    for child_folder, files_moved in report_dict.items():
        if files_moved > 0:
            print(f"{"Sort Report":=^40}")
            print(
                f"{files_moved} file{"s" if files_moved != 1 else ""} moved into {child_folder}.")


if __name__ == "__main__":
    main()
