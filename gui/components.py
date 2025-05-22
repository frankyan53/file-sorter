import customtkinter as ctk
import gui.handlers as handlers
import gui.state as state
from PIL import Image


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
        "assets/file_sorter_logo.png"), size=(120, 120))
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
    button = ctk.CTkButton(sidebar, text=text, width=160, height=35, fg_color="transparent",
                           hover=False, text_color="white", font=("Roboto", 14, "bold"), anchor="w")
    button.pack(pady=(10, 5))

    def on_enter(e):
        if button != state.active_sidebar_button:
            button.configure(fg_color="white", text_color="#2c8850")

    def on_leave(e):
        if button != state.active_sidebar_button:
            button.configure(fg_color="transparent", text_color="white")

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button


def create_sidebar_buttons(sidebar, dashboard_frame, defaults_frame, settings_frame):
    dashboard_button = create_sidebar_button(sidebar, "Dashboard")
    defaults_button = create_sidebar_button(sidebar, "Defaults")
    settings_button = create_sidebar_button(sidebar, "Settings")
    sidebar_buttons = (dashboard_button, defaults_button, settings_button)
    dashboard_button.configure(command=lambda: handlers.handle_sidebar_button(
        dashboard_frame, dashboard_button, sidebar_buttons))
    defaults_button.configure(command=lambda: handlers.handle_sidebar_button(
        defaults_frame, defaults_button, sidebar_buttons))
    settings_button.configure(command=lambda: handlers.handle_sidebar_button(
        settings_frame, settings_button, sidebar_buttons))
    return dashboard_button, defaults_button, settings_button, sidebar_buttons


def create_page_title(text, frame):
    title = ctk.CTkLabel(frame, text=text, font=(
        "Roboto Black", 24, "bold"), text_color="#2c8850")
    title.place(x=25, y=25)
    return title


def create_page_titles(dashboard_frame, defaults_frame, settings_frame):
    dashboard_title = create_page_title("Dashboard", dashboard_frame)
    defaults_title = create_page_title("Defaults", defaults_frame)
    settings_title = create_page_title("Settings", settings_frame)


def create_get_parent_folder_frame(dashboard_frame):
    parent_path_frame = ctk.CTkFrame(
        dashboard_frame, width=550, height=70, corner_radius=5, fg_color="#f0ecec")
    parent_path_frame.place(x=25, y=75)
    parent_path_frame.pack_propagate(False)
    return parent_path_frame


def create_get_parent_folder_entry(parent_path_frame):
    parent_path_entry = ctk.CTkEntry(parent_path_frame, width=450, height=30, corner_radius=5, fg_color="transparent", text_color="black", font=(
        "Roboto", 14), placeholder_text="Select a folder to sort...", placeholder_text_color="gray", border_color="#2c8850", border_width=2)
    parent_path_entry.configure(state="disabled")
    parent_path_entry.place(x=10, y=10)
    parent_path_entry.propagate(False)
    parent_path_button = ctk.CTkButton(parent_path_frame, text="Browse", width=50, height=30, corner_radius=10, fg_color="#2c8850", font=(
        "Roboto", 14), hover=True, hover_color="#3cae68", command=lambda: handlers.handle_parent_path_button(parent_path_entry, parent_path_frame))
    parent_path_button.place(x=470, y=10)
    create_parent_path_status_label(parent_path_frame, "❌ No folder selected.")
    return parent_path_entry


def create_parent_path_status_label(parent_path_frame, text):
    status_label = ctk.CTkLabel(parent_path_frame, text=text, font=(
        "Roboto", 14), text_color="black", fg_color="transparent")
    status_label.place(x=10, y=42.5)


def create_dashboard_button(frame):
    button = ctk.CTkButton(frame, width=166.66, height=100, font=(
        "Roboto", 14), corner_radius=5, fg_color="#2c8850", hover=True, hover_color="#3cae68")
    return button


def create_dashboard_buttons(dashboard_frame, parent_path_entry, console):
    sort_button = create_dashboard_button(dashboard_frame)
    sort_button.configure(text="Sort Files", command=lambda: handlers.handle_sort_button(
        parent_path_entry, dashboard_frame, console))
    sort_button.place(x=25, y=170)
    unsort_button = create_dashboard_button(dashboard_frame)
    unsort_button.configure(text="Unsort Files", command=lambda: handlers.handle_unsort_button(
        parent_path_entry, dashboard_frame, console))
    unsort_button.place(x=216.66, y=170)
    delete_folders_button = create_dashboard_button(dashboard_frame)
    delete_folders_button.configure(text="Delete Empty Folders", command=lambda: handlers.handle_delete_folders_button(
        parent_path_entry, dashboard_frame, console))
    delete_folders_button.place(x=408.32, y=170)
    return sort_button, unsort_button, delete_folders_button


def create_dashboard_button_status_label(dashboard_frame, text):
    status_label = ctk.CTkLabel(dashboard_frame, text=text, font=(
        "Roboto", 14), text_color="black", fg_color="transparent")
    status_label.place(x=25, y=275)


def create_dashboard_console(dashboard_frame):
    console = ctk.CTkTextbox(dashboard_frame, width=550, height=170, corner_radius=5, font=(
        "Courier New", 12), text_color="black", fg_color="#f0ecec", wrap="word")
    console.place(x=25, y=305)
    console.tag_config("placeholder", foreground="grey")
    console.insert("end", "Console output will appear here...", "placeholder")
    console.configure(state="disabled")
    return console
