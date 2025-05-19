import json
from pathlib import Path


def initialize_json(file_path, data):
    if not Path(file_path).exists():
        write_json(file_path, data)


def initialize_all_json():
    data = [
        "3D Models",
        "Archives",
        "Audio",
        "Code",
        "Documents",
        "Executables",
        "Fonts",
        "Images",
        "Other",
        "Spreadsheets",
        "Videos"
    ]
    initialize_json("child_folders.json", data)
    data = {
        "3D Models": [
            ".obj",
            ".fbx",
            ".stl",
            ".3ds",
            ".dae",
            ".blend",
            ".gltf",
            ".glb",
            ".x3d"
        ],
        "Archives": [
            ".zip",
            ".rar",
            ".tar",
            ".gz",
            ".7z",
            ".bz2",
            ".xz",
            ".cab",
            ".iso",
            ".lz",
            ".lzma",
            ".z",
            ".ace",
            ".arj",
            ".jar"
        ],
        "Audio": [
            ".mp3",
            ".wav",
            ".aac",
            ".flac",
            ".ogg",
            ".m4a",
            ".wma",
            ".alac",
            ".aiff",
            ".amr",
            ".mid",
            ".midi",
            ".opus",
            ".ra",
            ".pcm"
        ],
        "Code": [
            ".py",
            ".js",
            ".html",
            ".css",
            ".cpp",
            ".c",
            ".java",
            ".rb",
            ".sh",
            ".json",
            ".xml",
            ".ipynb",
            ".php",
            ".go",
            ".rs",
            ".swift",
            ".ts",
            ".tsx",
            ".jsx",
            ".cs",
            ".vb",
            ".kt",
            ".scala",
            ".pl",
            ".lua",
            ".sql",
            ".yml",
            ".yaml",
            ".bat",
            ".cmd",
            ".ini",
            ".cfg"
        ],
        "Documents": [
            ".pdf",
            ".doc",
            ".docx",
            ".ppt",
            ".pptx",
            ".xls",
            ".xlsx",
            ".txt",
            ".rtf",
            ".odt",
            ".odp",
            ".ods",
            ".epub",
            ".md",
            ".tex",
            ".log",
            ".csv",
            ".pages",
            ".numbers",
            ".key",
            ".xps"
        ],
        "Executables": [
            ".exe",
            ".msi",
            ".dmg",
            ".pkg",
            ".bat",
            ".sh",
            ".app",
            ".deb",
            ".rpm",
            ".run",
            ".apk",
            ".bin",
            ".com",
            ".command",
            ".gadget"
        ],
        "Fonts": [
            ".ttf",
            ".otf",
            ".woff",
            ".woff2",
            ".eot",
            ".fon"
        ],
        "Images": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".tif",
            ".webp",
            ".svg",
            ".heic",
            ".ico",
            ".raw",
            ".cr2",
            ".nef",
            ".orf",
            ".sr2",
            ".psd",
            ".ai",
            ".eps"
        ],
        "Other": [],
        "Spreadsheets": [
            ".xls",
            ".xlsx",
            ".ods",
            ".csv",
            ".tsv"
        ],
        "Videos": [
            ".mp4",
            ".mkv",
            ".mov",
            ".avi",
            ".flv",
            ".wmv",
            ".webm",
            ".mpeg",
            ".mpg",
            ".3gp",
            ".m4v",
            ".ts",
            ".mts",
            ".vob",
            ".rm",
            ".rmvb"
        ]
    }
    initialize_json("folder_extensions.json", data)
    initialize_json("create_errors.json", None)
    initialize_json("sort_errors.json", None)
    initialize_json("unsort_errors.json", None)
    initialize_json("delete_errors.json", None)


def load_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def get_unique_path(original_file_path):
    counter = 1
    renamed_file_path = original_file_path
    while renamed_file_path.exists():
        renamed_file_path = original_file_path.with_stem(
            f"{original_file_path.stem}_{counter}")
        counter += 1
    return renamed_file_path


def append_rename_dict(renamed_files_list, original_file_path, renamed_file_path):
    if original_file_path != renamed_file_path:
        renamed_files_list.append(
            {"original": original_file_path.name, "renamed": renamed_file_path.name})


def append_error_dict(errors_list, directory, operation, error):
    errors_list.append({"directory": str(directory),
                       "operation": operation, "error": str(error)})
