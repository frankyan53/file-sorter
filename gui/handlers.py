import core.logic as logic
import gui.components as components
import gui.state as state
import gui.utils as utils
from tkinter import filedialog


def handle_sidebar_button(frame, button, sidebar_buttons):
    state.active_sidebar_button = button
    frame.lift()
    button.configure(text_color="#2c8850", fg_color="white")
    for sidebar_button in sidebar_buttons:
        if button != sidebar_button:
            sidebar_button.configure(
                fg_color="transparent", text_color="white")


def handle_parent_path_button(parent_path_entry, parent_path_frame):
    old_parent_folder_path = parent_path_entry.get()
    new_parent_folder_path = filedialog.askdirectory()
    if not old_parent_folder_path and not new_parent_folder_path:
        components.create_parent_path_status_label(
            parent_path_frame, "❌ No folder selected.")
    elif old_parent_folder_path and not new_parent_folder_path:
        components.create_parent_path_status_label(
            parent_path_frame, "⚠️ Selected folder unchanged.")
    else:
        parent_path_entry.configure(state="normal")
        parent_path_entry.delete(0, "end")
        parent_path_entry.insert(0, new_parent_folder_path)
        parent_path_entry.configure(state="disabled")
        components.create_parent_path_status_label(
            parent_path_frame, "✔️ Folder selected.                        ")


def handle_sort_button(parent_path_entry, dashboard_frame, console):
    parent_folder_path = utils.get_parent_folder_path(parent_path_entry)
    created_folders_counter = logic.create_folders(parent_folder_path)
    has_source_files, sort_report, renamed_files, is_successful, sort_errors = logic.sort_files(
        parent_folder_path)
    if not is_successful and sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to sort files.                                ")
    if is_successful and sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some files could not be sorted.                      ")
    if is_successful and not sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Files sorted.                                        ")
    if not has_source_files and created_folders_counter == 0:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to sort.                                     ")
    elif not has_source_files and created_folders_counter > 0:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to sort.                                     ")
        lines = ["--- Sort Report ---",
                 f"{created_folders_counter} folder{"s" if created_folders_counter != 1 else ""} created."]
        utils.log_to_console(console, lines)
    elif has_source_files and created_folders_counter == 0:
        lines = ["--- Sort Report ---"]
        utils.append_sort_report(lines, sort_report, renamed_files)
        utils.log_to_console(console, lines)
    else:
        lines = ["--- Sort Report ---",
                 f"{created_folders_counter} folder{"s" if created_folders_counter != 1 else ""} created."]
        utils.append_sort_report(lines, sort_report, renamed_files)
        utils.log_to_console(console, lines)


def handle_unsort_button(parent_path_entry, dashboard_frame, console):
    parent_folder_path = utils.get_parent_folder_path(parent_path_entry)
    unsorted_file_count, deleted_folder_count, renamed_files, is_successful, unsort_errors = logic.unsort_files(
        parent_folder_path)
    if not is_successful and unsort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to unsort files.                              ")
    if is_successful and unsort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some files could not be unsorted.                    ")
    if is_successful and not unsort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Files unsorted.                                      ")
    if unsorted_file_count == 0 and deleted_folder_count == 0:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to unsort.                                   ")
    elif unsorted_file_count == 0 and deleted_folder_count > 0:
        lines = ["--- Unsort Report ---",
                 f"{deleted_folder_count} folder{"s" if deleted_folder_count != 1 else ""} deleted."]
        utils.log_to_console(console, lines)
    else:
        lines = ["--- Unsort Report ---", f"{unsorted_file_count} file{"s" if unsorted_file_count != 1 else ""} unsorted.",
                 f"{deleted_folder_count} folder{"s" if deleted_folder_count != 1 else ""} deleted."]
        for file in renamed_files:
            lines.append(
                f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")
        utils.log_to_console(console, lines)


def handle_delete_folders_button(parent_path_entry, dashboard_frame, console):
    parent_folder_path = utils.get_parent_folder_path(parent_path_entry)
    deleted_folder_count, is_successful, delete_errors = logic.delete_empty_folders(
        parent_folder_path)
    if not is_successful and delete_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to delete empty folders.                      ")
    if is_successful and delete_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some folders could not be deleted.                   ")
    if is_successful and not delete_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Folders deleted.                                     ")
    if deleted_folder_count == 0:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to delete.                                   ")
    else:
        lines = ["--- Delete Report ---",
                 f"{deleted_folder_count} folder{"s" if deleted_folder_count != 1 else ""} deleted."]
        utils.log_to_console(console, lines)
