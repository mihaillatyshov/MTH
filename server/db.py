from sqlalchemy import Column, ForeignKey, String, Integer, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date
from utils import *

db_username, db_password, db_name = get_configs()
engine = create_engine(f"postgresql://{db_username}:{db_password}@localhost:5432/{db_name}")
Base = declarative_base()
Session = sessionmaker(bind=engine)

"""Users"""
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    confirmed = Column(Integer, nullable=False)

    def __init__(self, last_name, first_name, username, email, password, confirmed) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.username = username
        self.email = email
        self.password = password
        self.confirmed = confirmed
        

class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True)
    value = Column(String, nullable=False)

    def __init__(self, value) -> None:
        self.value = value

Base.metadata.create_all(engine)
session = Session()