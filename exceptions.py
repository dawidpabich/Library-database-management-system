# exceptions

import dearpygui.dearpygui as dpg


def error_window(message):  # create window showing error message from exception
    if dpg.does_item_exist("show_window"):
        dpg.delete_item("show_window")
    with dpg.window(tag="show_window", no_title_bar=True, no_background=False, pos=(700, 0), width=700, height=800):
        dpg.add_text("ERROR", color=(200, 0, 0))
        dpg.add_text(message)


class IDError(Exception):
    def __init__(self, inputted_ID):
        if inputted_ID:
            self.inputted_ID = inputted_ID
        else:
            self.inputted_ID = None
        self.message = None

    def __str__(self):
        self.message = f"Inputted ID (ID = {self.inputted_ID}) is not in valid range"
        return self.message


class EmptyInput(Exception):
    def __init__(self):
        self.message = None

    def __str__(self):
        self.message = "Fill in all text fields"
        return self.message
