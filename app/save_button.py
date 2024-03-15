"""A module for the utilities of the application."""
from app.get_buttons import GetButtons as gb
from database.json_helpers import JsonHelpers as jh
# from app.show_buttons import ShowButtons as shb


class SaveButton:
    """A class to represent the utilities of the application."""

    def __init__(self, id_button, root, title, domain, username,
                 domain_controller):
        self.id_button = id_button
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

    def save_button(self, entry_data, button_id=None):
        """This method saves the button to the database."""
        if button_id is None:
            append_button = gb.get_button_list(self)
        else:
            current_data = gb.get_button_list(self)
            append_button = [
                button for button in current_data if not button.id == button_id
            ]

        new_title = entry_data["title"]
        new_domain = entry_data["domain"]
        new_username = entry_data["username"]
        new_domain_controller = entry_data["domain_controller"]

        # Generate a unique id_button for the button
        if button_id is None:
            max_id = max(button.id_button for button in append_button)
            button_id = max_id + 1

        button = SaveButton(id_button=button_id,
                            root='',
                            title=new_title,
                            domain=new_domain,
                            username=new_username,
                            domain_controller=new_domain_controller)
        append_button.append(button)
        append_button = sorted(append_button, key=lambda x: x.id_button)

        jh.save_changes_to_db(self, button_list=append_button)
        # shb.show_button_list(self, top_frame, "cmd")
