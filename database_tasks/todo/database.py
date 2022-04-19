#! /usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean

engine = create_engine('sqlite:///todo.db', echo = False)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Tables

class Item(Base):
    __tablename__ = "items"
    itemId = Column(Integer, primary_key = True)
    name = Column(String)
    #isCompleted = Column(Boolean)
    #completedAt = Column(DateTime)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()