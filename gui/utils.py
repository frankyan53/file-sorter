import gui.state as state
from pathlib import Path


def get_parent_folder_path(parent_path_entry):
    parent_folder_path = Path(parent_path_entry.get())
    return parent_folder_path


def log_to_console(console, lines):
    console.configure(state="normal")
    if state.console_placeholder_text:
        console.delete("1.0", "end")
        state.console_placeholder_text = False
    for line in lines:
        console.insert("end", line + "\n")
    console.insert("end", "\n")
    console.see("end")
    console.configure(state="disabled")


def append_sort_report(lines, sort_report, renamed_files):
    for child_folder, files_moved in sort_report.items():
        if files_moved > 0:
            lines.append(
                f"{files_moved} file{"s" if files_moved != 1 else ""} moved into {child_folder}.")
    for file in renamed_files:
        lines.append(
            f"{file["original"]} was renamed to {file["renamed"]} due to a duplicate filename.")
