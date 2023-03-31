import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publishers'
    publisher_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    book = relationship("Books", back_populates="publisher")