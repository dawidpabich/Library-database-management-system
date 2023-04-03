import sqlalchemy as db
from sqlalchemy.orm import relationship
from database import Base


class Borrower(Base):
    __tablename__ = 'borrowers'
    borrower_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    book_borrowed=relationship("BookBorrowed", back_populates="borrower")