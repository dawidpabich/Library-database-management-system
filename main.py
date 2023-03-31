from dearpygui.dearpygui import start_dearpygui
from gui import UserInterface

if __name__ == "__main__":
    UI = UserInterface()
    UI.window()
    start_dearpygui()

