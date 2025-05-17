import textwrap
import shutil
from pathlib import Path


def get_operating_system():
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


def get_parent_folder_path():
    get_operating_system()
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


def create_child_folders(parent_folder_path):
    child_folder_list = ["3D Models", "Archives", "Audio", "Code", "Documents",
                         "Executables", "Fonts", "Images", "Other", "Spreadsheets", "Videos"]
    for folder in child_folder_list:
        try:
            child_folder_path = parent_folder_path / folder
            child_folder_path.mkdir(exist_ok=True)
        except Exception as error:
            print(f"An error occurred: {error}")
            break
    else:
        print("Folders created successfully.")


def move_files(parent_folder_path):
    child_folder_extensions_dict = {
        "3D Models": [".obj", ".fbx", ".stl", ".3ds", ".dae", ".blend", ".gltf", ".glb", ".x3d"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".cab", ".iso", ".lz", ".lzma", ".z", ".ace", ".arj", ".jar"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".alac", ".aiff", ".amr", ".mid", ".midi", ".opus", ".ra", ".pcm"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".rb", ".sh", ".json", ".xml", ".ipynb", ".php", ".go", ".rs", ".swift", ".ts", ".tsx", ".jsx", ".cs", ".vb", ".kt", ".scala", ".pl", ".lua", ".sql", ".yml", ".yaml", ".bat", ".cmd", ".ini", ".cfg"],
        "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".txt", ".rtf", ".odt", ".odp", ".ods", ".epub", ".md", ".tex", ".log", ".csv", ".pages", ".numbers", ".key", ".xps"],
        "Executables": [".exe", ".msi", ".dmg", ".pkg", ".bat", ".sh", ".app", ".deb", ".rpm", ".run", ".apk", ".bin", ".com", ".command", ".gadget"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".heic", ".ico", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".psd", ".ai", ".eps"],
        "Other": [],
        "Spreadsheets": [".xls", ".xlsx", ".ods", ".csv", ".tsv"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp", ".m4v", ".ts", ".mts", ".vob", ".rm", ".rmvb"]
    }
    for source_file_path in parent_folder_path.iterdir():
        if source_file_path.is_dir():
            continue
        for child_folder, child_folder_extensions in child_folder_extensions_dict.items():
            try:
                if source_file_path.suffix in child_folder_extensions:
                    shutil.move(source_file_path, source_file_path.parent /
                                child_folder / source_file_path.name)
                    break
            except Exception as error:
                print(f"An error occurred: {error}")
                break
        else:
            shutil.move(source_file_path, source_file_path.parent /
                        "Other" / source_file_path.name)


def main():
    parent_folder_path = get_parent_folder_path()
    create_child_folders(parent_folder_path)
    move_file(parent_folder_path)


if __name__ == "__main__":
    main()
