import shutil
from pathlib import Path


def create_child_folders(parent_folder_path):
    child_folders_list = ["3D Models", "Archives", "Audio", "Code", "Documents",
                          "Executables", "Fonts", "Images", "Other", "Spreadsheets", "Videos"]
    try:
        for folder in child_folders_list:
            child_folder_path = parent_folder_path / folder
            child_folder_path.mkdir(exist_ok=True)
        return True
    except Exception:
        return False


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
            if source_file_path.suffix in child_folder_extensions:
                shutil.move(source_file_path, source_file_path.parent /
                            child_folder / source_file_path.name)
                break
        else:
            shutil.move(source_file_path, source_file_path.parent /
                        "Other" / source_file_path.name)
