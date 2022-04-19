#! /usr/bin/python3

from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

# Create engine
engine = create_engine('sqlite:///todo.db', echo = False)

# Create declarative base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Users
class User(Base):
  __tablename__ = "users"
  userId = Column(Integer, primary_key = True)
  userName = Column(String, nullable = False)
  password = Column(String, nullable = False)
  items = relationship("Item", secondary = "useritems", back_populates = "users", cascade= "all, delete")
# , cascade = "all, delete, delete-orphan")
# Items
class Item(Base):
  __tablename__ = "items"
  itemId = Column(Integer, primary_key = True)
  name = Column(String, nullable = False)
  users = relationship("User", secondary="useritems", back_populates ="items")

class UserItem(Base):
  __tablename__ = "useritems"
  userId = Column(Integer, ForeignKey("users.userId"), primary_key=True)
  itemId = Column(Integer, ForeignKey("items.itemId"), primary_key=True)

# Create the tables
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()