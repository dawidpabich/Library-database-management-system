import sqlalchemy as db
from sqlalchemy.orm import relationship
from database import Base


class Author(Base):
    __tablename__ = 'authors'
    author_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    book = relationship("Book", back_populates="author")