import textwrap
from pathlib import Path


def create_child_folders():
    child_list = ["Images", "Videos", "Audio", "Documents",
                  "Archives", "Code", "Executables", "Other"]
    default_path = None
    print("""Below is a list of operating systems.
1. Windows
2. macOS
3. Linux""")
    operating_system = input(
        "Enter a number from 1 to 3 to choose the operating system that you are currently using: ").strip()
    while operating_system not in ("1", "2", "3"):
        operating_system = input(
            "Invalid number. Please try again. Enter a number from 1 to 3: ").strip()
    print("\nThank you for choosing your operating system.\n")
    if operating_system == "1":
        print(textwrap.fill(
            "To start sorting, enter the path of the folder you want to organize.", 80))
        print()
        print(textwrap.fill("Open File Explorer, navigate to the folder, then click the path bar at the top. Copy the full path, and paste it when prompted. Alternatively, open Terminal and drag the folder into the window to show the full path.", 80))
        print()
    elif operating_system == "2":
        print(textwrap.fill(
            "To start sorting, enter the path of the folder you want to organize.", 80))
        print()
        print(textwrap.fill("Open Finder, find the folder, then right-click and choose \"Get Info.\" Copy the full path from the \"Where\" section, and paste it when prompted. Alternatively, open Terminal and drag the folder into the window to show the full path.", 80))
        print()
    else:
        print(textwrap.fill(
            "To start sorting, enter the path of the folder you want to organize.", 80))
        print()
        print(textwrap.fill("Open your file manager (e.g. Nautilus), find the folder, then right-click and choose \"Properties.\" Copy the full path, and paste it when prompted. Alternatively, open Terminal and drag the folder into the window to show the full path.", 80))
        print()
    for i in range(3, 0, -1):
        parent_path_input = input(
            f"Enter folder path ({i} attempts remaining): ").replace("\\", "/").strip()
        parent_path = Path(parent_path_input)
        if parent_path.exists() and parent_path.is_dir():
            print()
            break
        elif i != 1:
            print(f"Invalid folder path. Please try again.", end=" ")
        else:
            print(
                "\nInvalid path entered 3 times. Defaulting to current working directory.", end=" ")
            default_path = Path.cwd()
    for folder in child_list:
        try:
            child_folder_path = default_path / folder if default_path else parent_path / folder
            child_folder_path.mkdir(exist_ok=True)
        except Exception as error:
            print(f"An error occurred: {error}")
            break
    else:
        print("Folders created successfully.")


def list_files():
    pass


def categorize_file():
    pass


def move_file():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
