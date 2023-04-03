import sqlalchemy as db
from sqlalchemy.orm import relationship
from database import Base

class Publisher(Base):
    __tablename__ = 'publishers'
    publisher_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    book = relationship("Book", back_populates="publisher")