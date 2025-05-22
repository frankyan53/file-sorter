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
            parent_path_frame, "⚠️ Selected folder unchanged.")
    else:
        parent_path_entry.configure(state="normal")
        parent_path_entry.delete(0, "end")
        parent_path_entry.insert(0, new_parent_folder_path)
        parent_path_entry.configure(state="disabled")
        components.create_parent_path_status_label(
            parent_path_frame, "✔️ Folder selected.                        ")


def get_parent_folder_path(parent_path_entry):
    parent_folder_path = Path(parent_path_entry.get())
    return parent_folder_path


def handle_sort_button(parent_path_entry, dashboard_frame, console):
    parent_folder_path = get_parent_folder_path(parent_path_entry)
    logic.create_folders(parent_folder_path)
    has_source_files, report, renamed_files, is_successful, sort_errors = logic.sort_files(
        parent_folder_path)
    if not is_successful and sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to sort files.")
    if is_successful and sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some files could not be sorted.")
    if is_successful and not sort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Files sorted.")
    if not has_source_files:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to sort.")
    else:
        console.configure(state="normal")
        if state.console_placeholder_text:
            console.delete("1.0", "end")
            state.console_placeholder_text = False
        console.insert("end", "--- Sort Report ---\n")
        for child_folder, files_moved in report.items():
            if files_moved > 0:
                console.insert(
                    "end", f"{files_moved} file{"s" if files_moved != 1 else ""} moved into {child_folder}.\n")
        for file in renamed_files:
            console.insert(
                "end", f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.\n")
        console.insert("end", "\n")
        console.see("end")
        console.configure(state="disabled")


def handle_unsort_button(parent_path_entry, dashboard_frame, console):
    parent_folder_path = get_parent_folder_path(parent_path_entry)
    unsorted_file_count, deleted_folder_count, renamed_files, is_successful, unsort_errors = logic.unsort_files(
        parent_folder_path)
    if not is_successful and unsort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to unsort files.")
    if is_successful and unsort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some files could not be unsorted.")
    if is_successful and not unsort_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Files unsorted.")
    if unsorted_file_count == 0 and deleted_folder_count == 0:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to unsort.")
    else:
        console.configure(state="normal")
        if state.console_placeholder_text:
            console.delete("1.0", "end")
            state.console_placeholder_text = False
        console.insert("end", "--- Unsort Report ---\n")
        console.insert(
            "end", f"{unsorted_file_count} file{"s" if unsorted_file_count != 1 else ""} unsorted.\n")
        console.insert(
            "end", f"{deleted_folder_count} folder{"s" if deleted_folder_count != 1 else ""} deleted.\n")
        for file in renamed_files:
            console.insert(
                f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.\n")
        console.insert("end", "\n")
        console.see("end")
        console.configure(state="disabled")


def handle_delete_folders_button(parent_path_entry, dashboard_frame, console):
    parent_folder_path = get_parent_folder_path(parent_path_entry)
    deleted_folder_count, is_successful, delete_errors = logic.delete_empty_folders(
        parent_folder_path)
    if not is_successful and delete_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "❌ Failed to delete empty folders.")
    if is_successful and delete_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "⚠️ Some folders could not be deleted.")
    if is_successful and not delete_errors:
        components.create_dashboard_button_status_label(
            dashboard_frame, "✔️ Folders deleted.")
    if deleted_folder_count == 0:
        components.create_dashboard_button_status_label(
            dashboard_frame, "ℹ️ Nothing to delete.")
    else:
        console.configure(state="normal")
        if state.console_placeholder_text:
            console.delete("1.0", "end")
            state.console_placeholder_text = False
        console.insert("end", "--- Delete Report ---\n")
        console.insert(
            "end", f"{deleted_folder_count} folder{"s" if deleted_folder_count != 1 else ""} deleted.\n")
        console.insert("end", "\n")
        console.see("end")
        console.configure(state="disabled")
