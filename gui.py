import customtkinter as ctk
from PIL import Image
from tkinter import filedialog

active_sidebar_button = None


def create_app():
    app = ctk.CTk()
    app.geometry("800x500")
    return app


def create_sidebar_frame(app):
    sidebar = ctk.CTkFrame(app, width=200, corner_radius=0, fg_color="#2c8850")
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    return sidebar


def create_sidebar_logo(sidebar):
    logo_image = ctk.CTkImage(Image.open(
        "file_sorter_logo.png"), size=(120, 120))
    logo_label = ctk.CTkLabel(sidebar, text="", image=logo_image)
    logo_label.pack(pady=(30, 20))


def create_main_frame(app):
    frame = ctk.CTkFrame(app, width=600, height=500, fg_color="white")
    frame.place(x=200, y=0)
    frame.pack_propagate(False)
    return frame


def create_main_frames(app):
    dashboard_frame = create_main_frame(app)
    defaults_frame = create_main_frame(app)
    settings_frame = create_main_frame(app)
    return dashboard_frame, defaults_frame, settings_frame


def create_sidebar_button(sidebar, text):
    global active_sidebar_button
    button = ctk.CTkButton(sidebar, text=text, width=160, height=35, fg_color="transparent",
                           hover=False, text_color="white", font=("Roboto", 14, "bold"), anchor="w")
    button.pack(pady=(10, 5))

    def on_enter(e):
        if button != active_sidebar_button:
            button.configure(fg_color="white", text_color="#2c8850")

    def on_leave(e):
        if button != active_sidebar_button:
            button.configure(fg_color="transparent", text_color="white")

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button


def create_sidebar_buttons(sidebar, dashboard_frame, defaults_frame, settings_frame):
    dashboard_button = create_sidebar_button(sidebar, "Dashboard")
    defaults_button = create_sidebar_button(sidebar, "Defaults")
    settings_button = create_sidebar_button(sidebar, "Settings")
    sidebar_buttons = (dashboard_button, defaults_button, settings_button)
    dashboard_button.configure(command=lambda: button_handler(
        dashboard_frame, dashboard_button, sidebar_buttons))
    defaults_button.configure(command=lambda: button_handler(
        defaults_frame, defaults_button, sidebar_buttons))
    settings_button.configure(command=lambda: button_handler(
        settings_frame, settings_button, sidebar_buttons))
    return dashboard_button, defaults_button, settings_button, sidebar_buttons


def button_handler(frame, button, sidebar_buttons):
    global active_sidebar_button
    active_sidebar_button = button
    frame.lift()
    button.configure(text_color="#2c8850", fg_color="white")
    for sidebar_button in sidebar_buttons:
        if button != sidebar_button:
            sidebar_button.configure(
                fg_color="transparent", text_color="white")


def create_get_parent_folder_frame(dashboard_frame):
    parent_path_frame = ctk.CTkFrame(
        dashboard_frame, width=550, height=60, corner_radius=5, fg_color="#f0ecec")
    parent_path_frame.pack(pady=150)
    parent_path_frame.pack_propagate(False)
    return parent_path_frame


def get_parent_folder_path(parent_path_frame):
    parent_path_entry = ctk.CTkEntry(parent_path_frame, width=450, height=30, corner_radius=5, fg_color="transparent", text_color="black", font=(
        "Roboto", 14), placeholder_text="Enter folder path...", placeholder_text_color="gray", border_color="#2c8850", border_width=2, state="disabled")
    parent_path_entry.pack(side="left", padx=10, pady=5)
    parent_path_entry.propagate(False)
    parent_path_button = ctk.CTkButton(parent_path_frame, text="Browse", width=50, height=30, corner_radius=10,
                                       fg_color="#2c8850", font=("Roboto", 14), command=lambda: parent_path_button_handler(parent_path_entry))
    parent_path_button.pack(side="right", padx=(0, 10), pady=5)
    return parent_path_entry


def parent_path_button_handler(parent_path_entry):
    parent_file_path = filedialog.askdirectory()
    if parent_file_path:
        parent_path_entry.configure(state="normal")
        parent_path_entry.delete(0, "end")
        parent_path_entry.insert(0, parent_file_path)
        parent_path_entry.configure(state="disabled")
    return parent_path_entry.get()


def launch_gui():
    app = create_app()
    sidebar = create_sidebar_frame(app)
    create_sidebar_logo(sidebar)
    dashboard_frame, defaults_frame, settings_frame = create_main_frames(
        app)
    dashboard_button, defaults_button, settings_button, sidebar_buttons = create_sidebar_buttons(
        sidebar, dashboard_frame, defaults_frame, settings_frame)
    button_handler(dashboard_frame, dashboard_button, sidebar_buttons)
    parent_path_frame = create_get_parent_folder_frame(dashboard_frame)
    get_parent_folder_path(parent_path_frame)
    app.mainloop()
