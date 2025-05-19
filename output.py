from logic import create_folders, sort_files, unsort_files, delete_empty_folders


def print_create_errors(is_successful, create_errors):
    if not is_successful and create_errors:
        print(
            f"Failed to create any folders. Encountered {len(create_errors)} error{"s" if len(create_errors) != 1 else ""}. See \"create_errors.json\" for more details.")
    elif is_successful and create_errors:
        print(
            f"Some folders couldn't be created. Encountered {len(create_errors)} error{"s" if len(create_errors) != 1 else ""}. See \"create_errors.json\" for more details.")
    else:
        print("Folders created successfully.")


def print_sort_errors(is_successful, sort_errors):
    if not is_successful and sort_errors:
        print(
            f"Failed to sort any files. Encountered {len(sort_errors)} error{"s" if len(sort_errors) != 1 else ""}. See \"sort_errors.json\" for more details.")
    elif is_successful and sort_errors:
        print(
            f"Some files couldn't be moved. Encountered {len(sort_errors)} error{"s" if len(sort_errors) != 1 else ""}. See \"sort_errors.json\" for more details.")
    elif is_successful and not sort_errors:
        print("Files sorted successfully.")
    else:
        return


def print_no_files(has_source_files, report):
    if not has_source_files:
        print("No files available to sort.")
    else:
        print(f"{"Sort Report":=^40}")
        for child_folder, files_moved in report.items():
            if files_moved > 0:
                print(
                    f"{files_moved} file{"s" if files_moved != 1 else ""} moved into {child_folder}.")


def print_renamed_sort_files(renamed_files):
    for file in renamed_files:
        print(
            f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")


def print_unsort_errors(is_successful, unsort_errors):
    if not is_successful and unsort_errors:
        print(
            f"Failed to unsort any files. Encountered {len(unsort_errors)} error{"s" if len(unsort_errors) != 1 else ""}. See \"unsort_errors.json\" for more details.")
    elif is_successful and unsort_errors:
        print(
            f"Some files couldn't be unsorted. Encountered {len(unsort_errors)} error{"s" if len(unsort_errors) != 1 else ""}. See \"unsort_errors.json\" for more details.")
    else:
        print("Files unsorted successfully.")


def print_renamed_unsort_files(renamed_files):
    for file in renamed_files:
        print(
            f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")


def print_delete_errors(is_successful, delete_errors):
    if not is_successful and delete_errors:
        print(
            f"Failed to delete any folders. Encountered {len(delete_errors)} error{"s" if len(delete_errors) != 1 else ""}. See \"delete_errors.json\" for more details.")
    elif is_successful and delete_errors:
        print(
            f"Some folders couldn't be deleted. Encountered {len(delete_errors)} error{"s" if len(delete_errors) != 1 else ""}. See \"delete_errors.json\" for more details.")
    else:
        print("Folders deleted successfully.")
