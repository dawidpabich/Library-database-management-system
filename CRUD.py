import dearpygui.dearpygui as dpg
from models import Books, BooksBorrowed, Authors, Borrowers, Publishers
from exceptions import IDError, EmptyInput, error_window
from database import session


class ShowRecords:

    def create_table(self, records, columns, values):
        it = 0
        if dpg.does_item_exist("show_window"):
            dpg.delete_item("show_window")

        with dpg.window(tag="show_window", no_title_bar=True, no_background=False, pos=(700, 0), width=700, height=800):
            with dpg.table(header_row=True):
                for column in columns:
                    dpg.add_table_column(label=column)

                for i in records:
                    with dpg.table_row():
                        for j in range(len(columns)):
                            dpg.add_text(values[it])
                            it += 1

    def show_books(self):
        records = session.query(Books, Authors, Publishers).join(Authors).join(Publishers).all()
        columns = ["Book ID", "Author first name", "Author last name", "Publisher", "Title", "Genre"]
        values = []
        for book, author, publisher in records:
            values.append(book.book_ID)
            values.append(author.first_name)
            values.append(author.last_name)
            values.append(publisher.name)
            values.append(book.title)
            values.append(book.genre)

        self.create_table(records, columns, values)

    def show_borrowed_books(self):
        records = session.query(BooksBorrowed, Books, Borrowers).join(Books).join(Borrowers).all()
        columns = ["Borrow ID", "Borrower ID", "First name", "Last name", "Book name", "Borrow date", "Due date"]
        values = []
        for book_borrowed, book, borrower in records:
            values.append(book_borrowed.borrow_ID)
            values.append(borrower.borrower_ID)
            values.append(borrower.first_name)
            values.append(borrower.last_name)
            values.append(book.title)
            values.append(book_borrowed.borrow_date)
            values.append(book_borrowed.due_date)

        self.create_table(records, columns, values)

    def show_borrowers(self):
        records = session.query(Borrowers)
        columns = ["borrower_ID", "first_name", "last_name", "address", "phone"]
        values = []
        for borrower in records:
            values.append(borrower.borrower_ID)
            values.append(borrower.first_name)
            values.append(borrower.last_name)
            values.append(borrower.address)
            values.append(borrower.phone)

        self.create_table(records, columns, values)

    def show_publishers(self):
        records = session.query(Publishers)
        columns = ["publisher_ID", "name", "address", "phone"]
        values = []
        for publisher in records:
            values.append(publisher.publisher_ID)
            values.append(publisher.name)
            values.append(publisher.address)
            values.append(publisher.phone)

        self.create_table(records, columns, values)

    def show_authors(self):
        records = session.query(Authors)
        columns = ["author_ID", "first_name", "last_name"]
        values = []
        for author in records:
            values.append(author.author_ID)
            values.append(author.first_name)
            values.append(author.last_name)

        self.create_table(records, columns, values)


class AddRecord:
    def success_window(self):
        if dpg.does_item_exist("show_window"):
            dpg.delete_item("show_window")
        with dpg.window(tag="show_window", no_title_bar=True, no_background=False, pos=(700, 0), width=700, height=800):
            dpg.add_text("SUCCESS", color=(0, 128, 0))
            dpg.add_text("Record added")

    def add_book(self):
        try:
            valid_author_ID = False
            valid_publisher_ID = False
            records = session.query(Books, Authors, Publishers).join(Authors).join(Publishers).all()
            book_to_add = Books(book_ID=dpg.get_value("add_book.book_ID"),
                         author_ID=dpg.get_value("add_book.author_ID"),
                         publisher_ID=dpg.get_value("add_book.publisher_ID"),
                         title=dpg.get_value("add_book.title_ID"),
                         genre=dpg.get_value("add_book.genre_ID"))

            for value in book_to_add.__dict__.values():
                if not value:
                    raise EmptyInput

            for book, author, publisher in records:
                if book.book_ID == int(dpg.get_value("add_book.book_ID")):
                    raise IDError(dpg.get_value("add_book.book_ID"))
                if author.author_ID == int(dpg.get_value("add_book.author_ID")):
                    valid_author_ID = True
                if publisher.publisher_ID == int(dpg.get_value("add_book.publisher_ID")):
                    valid_publisher_ID = True

            if not valid_author_ID:
                raise IDError(dpg.get_value("add_book.author_ID"))
            elif not valid_publisher_ID:
                raise IDError(dpg.get_value("add_book.publisher_ID"))
            else:
                session.add(book_to_add)
                self.success_window()
                session.commit()


        except EmptyInput as er:
            error_window(er)

        except IDError as er:
            error_window(er)

    def add_borrowed_book(self):
        try:
            valid_book_ID = False
            valid_borrower_ID = False
            records = session.query(BooksBorrowed)
            borrowed_book_to_add = BooksBorrowed(borrow_ID=dpg.get_value("add_borrowed_book.borrow_ID"),
                                          book_ID=dpg.get_value("add_borrowed_book.book_ID"),
                                          borrower_ID=dpg.get_value("add_borrowed_book.borrower_ID"))
            for value in borrowed_book_to_add.__dict__.values():
                if not value:
                    raise EmptyInput

            for book_borrowed in records:
                if book_borrowed.borrow_ID == int(dpg.get_value("add_borrowed_book.borrow_ID")):
                    raise IDError(dpg.get_value("add_borrowed_book.borrow_ID"))
                if book_borrowed.book_ID == int(dpg.get_value("add_borrowed_book.book_ID")):
                    valid_book_ID = True
                if book_borrowed.borrower_ID == int(dpg.get_value("add_borrowed_book.borrower_ID")):
                    valid_borrower_ID = True

            if not valid_book_ID:
                raise IDError(dpg.get_value("add_borrowed_book.book_ID"))
            elif not valid_borrower_ID:
                raise IDError(dpg.get_value("add_borrowed_book.borrower_ID"))
            else:
                session.add(borrowed_book_to_add)
                self.success_window()
                session.commit()


        except EmptyInput as er:
            error_window(er)

        except IDError as er:
            error_window(er)

    def add_borrower(self):
        try:
            records = session.query(Borrowers)
            borrower_to_add = Borrowers(borrower_ID=dpg.get_value("add_borrower.borrower_ID"),
                                 first_name=dpg.get_value("add_borrower.first_name"),
                                 last_name=dpg.get_value("add_borrower.last_name"),
                                 address=dpg.get_value("add_borrower.address"),
                                 phone=dpg.get_value("add_borrower.phone"))
            for value in borrower_to_add.__dict__.values():
                if not value:
                    raise EmptyInput

            for borrower in records:
                if borrower.borrower_ID == int(dpg.get_value("add_borrower.borrower_ID")):
                    raise IDError(dpg.get_value("add_borrower.borrower_ID"))

            session.add(borrower_to_add)
            self.success_window()
            session.commit()

        except EmptyInput as er:
            error_window(er)

        except IDError as er:
            error_window(er)

    def add_publisher(self):
        try:
            records = session.query(Publishers)
            publisher_to_add = Publishers(publisher_ID=dpg.get_value("add_publisher.publisher_ID"),
                                   name=dpg.get_value("add_publisher.publisher_name"),
                                   address=dpg.get_value("add_publisher.address"),
                                   phone=dpg.get_value("add_publisher.phone"))
            for value in publisher_to_add.__dict__.values():
                if not value:
                    raise EmptyInput

            for publisher in records:
                if publisher.publisher_ID == int(dpg.get_value("add_publisher.publisher_ID")):
                    raise IDError(dpg.get_value("add_publisher.publisher_ID"))

            session.add(publisher_to_add)
            self.success_window()
            session.commit()

        except EmptyInput as er:
            error_window(er)

        except IDError as er:
            error_window(er)

    def add_author(self):
        try:
            records = session.query(Authors)
            author_to_add = Authors(author_ID=dpg.get_value("add_author.author_ID"),
                                    first_name=dpg.get_value("add_author.first_name"),
                                    last_name=dpg.get_value("add_author.last_name"))
            for value in author_to_add.__dict__.values():
                if not value:
                    raise EmptyInput

            for author in records:
                if author.author_ID == int(dpg.get_value("add_author.author_ID")):
                    raise IDError(dpg.get_value("add_author.author_ID"))

            session.add(author_to_add)
            session.commit()

        except EmptyInput as er:
            error_window(er)

        except IDError as er:
            error_window(er)


class DeleteRecord:
    def success_window(self):
        if dpg.does_item_exist("show_window"):
            dpg.delete_item("show_window")
        with dpg.window(tag="show_window", no_title_bar=True, no_background=False, pos=(700, 0), width=700, height=800):
            dpg.add_text("SUCCESS", color=(0, 128, 0))
            dpg.add_text("Record deleted")

    def delete_book(self):
        try:
            inputted_id = dpg.get_value("delete_book.book_ID")
            result_to_delete = session.query(Books).filter(Books.book_ID == inputted_id).first()

            if not result_to_delete:
                raise IDError(inputted_id)

            session.delete(result_to_delete)
            session.commit()
            self.success_window()

        except IDError as er:
            error_window(er)

    def delete_borrowed_book(self):
        try:
            inputted_id = dpg.get_value("delete_book_borrowed.book_borrowed_ID")
            result_to_delete = session.query(BooksBorrowed).filter(BooksBorrowed.borrow_ID == inputted_id).first()

            if not result_to_delete:
                raise IDError(inputted_id)

            session.delete(result_to_delete)
            session.commit()
            self.success_window()

        except IDError as er:
            error_window(er)

    def delete_borrower(self):
        try:
            inputted_id = dpg.get_value("delete_borrower.borrower_ID")
            result_to_delete = session.query(Borrowers).filter(Borrowers.borrower_ID == inputted_id).first()

            if not result_to_delete:
                raise IDError(inputted_id)

            session.delete(result_to_delete)
            session.commit()
            self.success_window()

        except IDError as er:
            error_window(er)

    def delete_publisher(self):
        try:
            inputted_id = dpg.get_value("delete_publisher.publisher_ID")
            result_to_delete = session.query(Publishers).filter(Publishers.publisher_ID == inputted_id).first()

            if not result_to_delete:
                raise IDError(inputted_id)

            session.delete(result_to_delete)
            session.commit()
            self.success_window()

        except IDError as er:
            error_window(er)

    def delete_author(self):
        try:
            inputted_id = dpg.get_value("delete_author.author_ID")
            result_to_delete = session.query(Authors).filter(Authors.author_ID == inputted_id).first()

            if not result_to_delete:
                raise IDError(inputted_id)

            session.delete(result_to_delete)
            session.commit()
            self.success_window()

        except IDError as er:
            error_window(er)


class UpdateRecord:  # user inputted ID must be in database and text fields cannot be empty

    def update_book(self):
        try:
            inputted_ID = dpg.get_value("update_book.book_ID")
            result_to_update = session.query(Books).filter(Books.book_ID == inputted_ID).first()

            if not result_to_update:
                raise IDError(inputted_ID)
            if not dpg.get_value("update_book.title") or dpg.get_value("update_book.genre"):
                raise EmptyInput

            result_to_update.title = dpg.get_value("update_book.title")
            result_to_update.genre = dpg.get_value("update_book.genre")
            session.commit()

        except IDError as er:
            error_window(er)
        except EmptyInput as er:
            error_window(er)

    def update_borrower(self):
        try:
            inputted_ID = dpg.get_value("update_borrower.borrower_ID")
            first_name = dpg.get_value("update_borrower.first_name")
            last_name = dpg.get_value("update_borrower.last_name")
            address = dpg.get_value("update_borrower.address")
            phone = dpg.get_value("update_borrower.phone")
            result_to_update = session.query(Borrowers).filter(Borrowers.borrower_ID == inputted_ID).first()

            if not result_to_update:
                raise IDError(inputted_ID)
            if not first_name or last_name or address or phone:
                raise EmptyInput

            result_to_update.first_name = first_name
            result_to_update.last_name = last_name
            result_to_update.address = address
            result_to_update.phone = phone
            session.commit()

        except IDError as er:
            error_window(er)
        except EmptyInput as er:
            error_window(er)

    def update_publisher(self):
        try:
            inputted_ID = dpg.get_value("update_publisher.publisher_ID")
            name = dpg.get_value("update_publisher.name")
            address = dpg.get_value("update_publisher.address")
            phone = dpg.get_value("update_publisher.phone")
            result_to_update = session.query(Publishers).filter(Publishers.publisher_ID == inputted_ID).first()

            if not result_to_update:
                raise IDError(inputted_ID)
            if not name or address or phone:
                raise EmptyInput

            result_to_update.name = name
            result_to_update.address = address
            result_to_update.phone = phone
            session.commit()

        except IDError as er:
            error_window(er)
        except EmptyInput as er:
            error_window(er)

    def update_author(self):
        try:
            inputted_ID = dpg.get_value("update_author.author_ID")
            first_name = dpg.get_value("update_author.first_name")
            last_name = dpg.get_value("update_author.last_name")
            result_to_update = session.query(Authors).filter(Authors.author_ID == inputted_ID).first()

            if not result_to_update:
                raise IDError(inputted_ID)
            if not first_name or last_name:
                raise EmptyInput

            result_to_update.first_name = first_name
            result_to_update.last_name = last_name
            session.commit()

        except IDError as er:
            error_window(er)
        except EmptyInput as er:
            error_window(er)


    # session.commit()

