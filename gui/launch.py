import gui.components as components
import gui.helpers as helpers


def launch():
    app = components.create_app()
    sidebar = components.create_sidebar_frame(app)
    components.create_sidebar_logo(sidebar)
    dashboard_frame, defaults_frame, settings_frame = components.create_main_frames(
        app)
    components.create_page_titles(
        dashboard_frame, defaults_frame, settings_frame)
    dashboard_button, defaults_button, settings_button, sidebar_buttons = components.create_sidebar_buttons(
        sidebar, dashboard_frame, defaults_frame, settings_frame)
    helpers.handle_sidebar_button(
        dashboard_frame, dashboard_button, sidebar_buttons)
    parent_path_frame = components.create_get_parent_folder_frame(
        dashboard_frame)
    console = components.create_dashboard_console(dashboard_frame)
    parent_path_entry = components.create_get_parent_folder_entry(
        parent_path_frame)
    sort_button, unsort_button, delete_folders_button = components.create_dashboard_buttons(
        dashboard_frame, parent_path_entry, console)
    app.mainloop()
