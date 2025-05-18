def main():
    parent_folder_path = get_parent_folder_path()
    create_child_folders(parent_folder_path)
    move_file(parent_folder_path)


if __name__ == "__main__":
    main()
