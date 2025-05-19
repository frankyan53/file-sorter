from cli import get_parent_folder_path
from logic import create_folders, sort_files, unsort_files, delete_empty_folders
from output import print_create_errors, print_sort_errors, print_no_files, print_renamed_sort_files, print_unsort_errors, print_renamed_unsort_files, print_delete_errors
from utils import initialize_all_json


def main():
    initialize_all_json()
    parent_folder_path = get_parent_folder_path()
    is_successful, create_errors = create_folders(parent_folder_path)
    print_create_errors(is_successful, create_errors)
    has_source_files, report, renamed_files, is_successful, sort_errors = sort_files(
        parent_folder_path)
    print_sort_errors(is_successful, sort_errors)
    print_no_files(has_source_files, report)
    print_renamed_sort_files(renamed_files)
    renamed_files, is_successful, unsort_errors = unsort_files(
        parent_folder_path)
    print_unsort_errors(is_successful, unsort_errors)
    print_renamed_unsort_files(renamed_files)
    is_successful, delete_errors = delete_empty_folders(parent_folder_path)
    print_delete_errors(is_successful, delete_errors)


if __name__ == "__main__":
    main()
