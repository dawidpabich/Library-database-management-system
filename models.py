import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()


class Books(Base):
    __tablename__ = 'books'
    book_ID = db.Column(db.Integer, primary_key=True)
    author_ID = db.Column(db.Integer, db.ForeignKey("authors.author_ID"))
    publisher_ID = db.Column(db.Integer, db.ForeignKey("publishers.publisher_ID"))
    title = db.Column(db.String(50))
    genre = db.Column(db.String(40))
    author = relationship("Authors", back_populates="book")
    publisher = relationship("Publishers", back_populates="book")
    book_borrowed = relationship("BooksBorrowed", back_populates="book")


class BooksBorrowed(Base):
    __tablename__ = 'books_borrowed'
    borrow_ID = db.Column(db.Integer, primary_key=True)
    book_ID = db.Column(db.Integer, db.ForeignKey("books.book_ID"))
    borrower_ID = db.Column(db.Integer, db.ForeignKey("borrowers.borrower_ID"))
    borrow_date = db.Column(db.Date(), default=datetime.now())
    due_date = db.Column(db.Date, default=datetime.now() + timedelta(days=100))
    book = relationship("Books", back_populates="book_borrowed")
    borrower = relationship("Borrowers", back_populates="book_borrowed")


# zmienic w bazie na address
class Borrowers(Base):
    __tablename__ = 'borrowers'
    borrower_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    book_borrowed=relationship("BooksBorrowed", back_populates="borrower")


class Publishers(Base):
    __tablename__ = 'publishers'
    publisher_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    book = relationship("Books", back_populates="publisher")


class Authors(Base):
    __tablename__ = 'authors'
    author_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    book = relationship("Books", back_populates="author")


