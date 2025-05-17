import textwrap


def create_child_folders():
    child_list = ["Images", "Videos", "Audio", "Documents",
                  "Archives", "Code", "Executables", "Other"]
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
