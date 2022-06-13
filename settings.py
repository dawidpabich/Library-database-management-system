# GUI settings

import dearpygui.dearpygui as dpg
from CRUD import ShowRecords, AddRecord, DeleteRecord, UpdateRecord
from os import path

ICON_PATH = path.join("icon", "book.ico")
FONT_PATH = path.join("font", "Arialn.ttf")


class UserInterface:
    show = ShowRecords()
    add = AddRecord()
    delete = DeleteRecord()
    update = UpdateRecord()

    def __init__(self):
        dpg.create_context()
        with dpg.font_registry():  # add new font
            default_font = dpg.add_font(file=FONT_PATH, size=20, parent="Primary Window")
        dpg.bind_font(default_font)  # replace original font with the new font
        dpg.create_viewport(title='Library database manager', width=1400, height=800, resizable=False, large_icon=ICON_PATH)
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def __del__(self):
        dpg.destroy_context()

    def window(self):  # create window containing tree nodes menu for user
        with dpg.window(tag="Primary Window"):
            dpg.set_primary_window("Primary Window", True)
            dpg.add_text("Welcome to library database manager!")
            self.show_records_tree_node()
            self.add_record_tree_node()
            self.update_record_tree_node()
            self.delete_record_tree_node()

    def show_records_tree_node(self):
        with dpg.tree_node(label="Show records"):
            dpg.add_button(label="Show books", width=150, height=30,
                           callback=self.show.show_books)

            dpg.add_button(label="Show borrowed books", width=150, height=30,
                           callback=self.show.show_borrowed_books)

            dpg.add_button(label="Show borrowers", width=150, height=30,
                           callback=self.show.show_borrowers)

            dpg.add_button(label="Show publishers", width=150, height=30,
                           callback=self.show.show_publishers)

            dpg.add_button(label="Show authors", width=150, height=30,
                           callback=self.show.show_authors)

    def add_record_tree_node(self):
        with dpg.tree_node(label="Add record"):
            with dpg.tree_node(label="Add book "):
                dpg.add_input_text(label="Book ID", tag="add_book.book_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="Author ID", tag="add_book.author_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="Publisher ID", tag="add_book.publisher_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="Title", tag="add_book.title_ID", width=120)
                dpg.add_input_text(label="Genre", tag="add_book.genre_ID", width=120)
                dpg.add_button(label="Confirm", callback=self.add.add_book)

            with dpg.tree_node(label="Add borrowed book "):
                dpg.add_input_text(label="Borrow ID", tag="add_borrowed_book.borrow_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="Book ID", tag="add_borrowed_book.book_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="Borrower ID", tag="add_borrowed_book.borrower_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_button(label="Confirm", callback=self.add.add_borrowed_book)

            with dpg.tree_node(label="Add borrower "):
                dpg.add_input_text(label="Borrower ID", tag="add_borrower.borrower_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="First name", tag="add_borrower.first_name", width=120)
                dpg.add_input_text(label="Last name", tag="add_borrower.last_name", width=120)
                dpg.add_input_text(label="Address", tag="add_borrower.address", width=120)
                dpg.add_input_text(label="Phone", tag="add_borrower.phone", width=120)
                dpg.add_button(label="Confirm", callback=self.add.add_borrower)

            with dpg.tree_node(label="Add publisher"):
                dpg.add_input_text(label="Publisher ID", tag="add_publisher.publisher_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="Name", tag="add_publisher.publisher_name", width=120)
                dpg.add_input_text(label="Address", tag="add_publisher.address", width=120)
                dpg.add_input_text(label="Phone", tag="add_publisher.phone", width=120)
                dpg.add_button(label="Confirm", callback=self.add.add_publisher)

            with dpg.tree_node(label="Add author"):
                dpg.add_input_text(label="Author ID", tag="add_author.author_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="First name", tag="add_author.first_name", width=120)
                dpg.add_input_text(label="Last name", tag="add_author.last_name", width=120)
                dpg.add_button(label="Confirm", callback=self.add.add_author)

    def update_record_tree_node(self):
        with dpg.tree_node(label="Update record"):
            with dpg.tree_node(label="Update book"):
                dpg.add_input_text(label="ID of the book to update", tag="update_book.book_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="New first name", tag="update_book.title", width=120)
                dpg.add_input_text(label="New last name", tag="update_book.genre", width=120)
                dpg.add_button(label="Confirm", callback=self.update.update_book)

            with dpg.tree_node(label="Update borrower"):
                dpg.add_input_text(label="ID of the borrower to update", tag="update_borrower.borrower_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="New first name", tag="update_borrower.first_name", width=120)
                dpg.add_input_text(label="New last name", tag="update_borrower.last_name", width=120)
                dpg.add_input_text(label="New address", tag="update_borrower.address", width=120)
                dpg.add_input_text(label="New phone number", tag="update_borrower.phone", width=120)
                dpg.add_button(label="Confirm", callback=self.update.update_borrower)

            with dpg.tree_node(label="Update publisher"):
                dpg.add_input_text(label="ID of the publisher to update", tag="update_publisher.publisher_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="New name", tag="update_publisher.name", width=120)
                dpg.add_input_text(label="New address", tag="update_publisher.address", width=120)
                dpg.add_input_text(label="New phone", tag="update_publisher.phone", width=120)
                dpg.add_button(label="Confirm", callback=self.update.update_publisher)

            with dpg.tree_node(label="Update author"):
                dpg.add_input_text(label="ID of the author to update", tag="update_author.author_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_input_text(label="New first name", tag="update_author.first_name", width=120)
                dpg.add_input_text(label="New last name", tag="update_author.last_name", width=120)
                dpg.add_button(label="Confirm", callback=self.update.update_author)

    def delete_record_tree_node(self):
        with dpg.tree_node(label="Delete record"):

            with dpg.tree_node(label="Delete book"):
                dpg.add_input_text(label="Book ID", tag="delete_book.book_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_button(label="Confirm", callback=self.delete.delete_book)

            with dpg.tree_node(label="Delete borrow of book"):
                dpg.add_input_text(label="Borrowed book ID", tag="delete_book_borrowed.book_borrowed_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_button(label="Confirm", callback=self.delete.delete_borrowed_book)

            with dpg.tree_node(label="Delete borrower"):
                dpg.add_input_text(label="Borrower ID", tag="delete_borrower.borrower_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_button(label="Confirm", callback=self.delete.delete_borrower)

            with dpg.tree_node(label="Delete publisher"):
                dpg.add_input_text(label="Publisher ID", tag="delete_publisher.publisher_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_button(label="Confirm", callback=self.delete.delete_publisher)

            with dpg.tree_node(label="Delete author"):
                dpg.add_input_text(label="Author ID", tag="delete_author.author_ID", width=120, decimal=True, no_spaces=True)
                dpg.add_button(label="Confirm", callback=self.delete.delete_author)
