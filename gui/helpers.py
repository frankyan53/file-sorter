import core.logic as logic
import gui.components as components
import gui.state as state
from pathlib import Path
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
            parent_path_frame, "✔️ Folder selected.      ")
    else:
        parent_path_entry.configure(state="normal")
        parent_path_entry.delete(0, "end")
        parent_path_entry.insert(0, new_parent_folder_path)
        parent_path_entry.configure(state="disabled")
        components.create_parent_path_status_label(
            parent_path_frame, "✔️ Folder selected.      ")


def get_parent_folder_path(parent_path_entry):
    parent_folder_path = Path(parent_path_entry.get())
    return parent_folder_path


def handle_sort_button(parent_path_entry, dashboard_frame):
    parent_folder_path = get_parent_folder_path(parent_path_entry)
    logic.create_folders(parent_folder_path)
    has_source_files, report, renamed_files, is_successful, sort_errors = logic.sort_files(
        parent_folder_path)
    if not is_successful and sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to sort files.")
    elif is_successful and sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some files could not be sorted.")
    elif is_successful and not sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Files sorted successfully.")
    else:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Files have already been sorted.")


def handle_unsort_button(parent_path_entry):
    parent_folder_path = get_parent_folder_path(parent_path_entry)
    renamed_files, is_successful, unsort_errors = logic.unsort_files(
        parent_folder_path)


def handle_delete_folders_button(parent_path_entry):
    parent_folder_path = get_parent_folder_path(parent_path_entry)
    is_successful, delete_errors = logic.delete_empty_folders(
        parent_folder_path)
