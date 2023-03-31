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