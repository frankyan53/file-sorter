from cli import get_parent_folder_path
from output import print_create_errors, print_sort_errors, print_no_files, print_renamed_sort_files, print_unsort_errors, print_renamed_unsort_files, print_delete_errors


def main():
    parent_folder_path = get_parent_folder_path()
    print_sort_errors(parent_folder_path)
    print_create_errors(parent_folder_path)
    print_sort_errors(parent_folder_path)
    print_no_files(parent_folder_path)
    print_renamed_sort_files(parent_folder_path)
    print_unsort_errors(parent_folder_path)
    print_renamed_unsort_files(parent_folder_path)
    print_delete_errors(parent_folder_path)


if __name__ == "__main__":
    main()
