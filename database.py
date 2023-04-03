from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'library_database'

def get_connection():
    return create_engine(
        url="mysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

engine = get_connection()
Session = sessionmaker(bind=engine)
session = Session()




