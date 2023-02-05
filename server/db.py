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
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    confirmed = Column(Integer, nullable=False, default=0)
        

class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True)
    value = Column(String, nullable=False)


Base.metadata.create_all(engine)
session = Session()