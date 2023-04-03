import sqlalchemy as db
from sqlalchemy.orm import relationship

from database import Base


class Book(Base):
    __tablename__ = 'books'
    book_ID = db.Column(db.Integer, primary_key=True)
    author_ID = db.Column(db.Integer, db.ForeignKey("authors.author_ID"))
    publisher_ID = db.Column(db.Integer, db.ForeignKey("publishers.publisher_ID"))
    title = db.Column(db.String(50))
    genre = db.Column(db.String(40))
    author = relationship("Author", back_populates="book")
    publisher = relationship("Publisher", back_populates="book")
    book_borrowed = relationship("BookBorrowed", back_populates="book")