import sqlalchemy as db
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from database import Base


class BookBorrowed(Base):
    __tablename__ = 'books_borrowed'
    borrow_ID = db.Column(db.Integer, primary_key=True)
    book_ID = db.Column(db.Integer, db.ForeignKey("books.book_ID"))
    borrower_ID = db.Column(db.Integer, db.ForeignKey("borrowers.borrower_ID"))
    borrow_date = db.Column(db.Date(), default=datetime.now())
    due_date = db.Column(db.Date, default=datetime.now() + timedelta(days=100))
    book = relationship("Book", back_populates="book_borrowed")
    borrower = relationship("Borrower", back_populates="book_borrowed")