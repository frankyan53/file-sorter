from pathlib import Path


def get_parent_folder_path():
    print("Paste the full path of the folder to organize (you can drag it into this window).", end=" ")
    for i in range(3, 0, -1):
        parent_folder_path_input = input(
            f"Enter folder path ({i} attempts remaining): ").replace("\\", "/").strip()
        parent_folder_path = Path(parent_folder_path_input)
        if parent_folder_path.exists() and parent_folder_path.is_dir():
            return parent_folder_path
        if i != 1:
            print(f"Invalid folder path. Please try again.", end=" ")
        else:
            print(
                "\nInvalid path entered 3 times. Defaulting to current working directory.", end=" ")
            return Path.cwd()
