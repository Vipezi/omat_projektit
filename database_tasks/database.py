from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
Base = declarative_base()

# Create engine
engine = create_engine('sqlite:///todo.db', echo = False)

# Create declarative base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# ---
# TABLES
# ---

# Items
class Item(Base):
  __tablename__ = "items"
  itemId = Column(Integer, primary_key = True, autoincrement = True)
  userId = Column(Integer, ForeignKey('users.userId'))
  name = Column(String, nullable=False)
  users = relationship('User', back_populates = 'items')

class User(Base):
  __tablename__ = "users"
  userId = Column(Integer, primary_key = True, autoincrement = True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  items = relationship('Item', back_populates = 'users', cascade = 'all, delete, delete-orphan')
  logIns =relationship("LogIn", back_populates="users", cascade = "all, delete, delete-orphan")


class LogIn(Base):
  __tablename__ = 'logIns'
  logId = Column(Integer, primary_key = True, autoincrement = True)
  userId = Column(Integer, ForeignKey('users.userId'))
  loggedAt = Column(DateTime(timezone=True), server_default=func.now())
  users =relationship("User", back_populates="logIns")

# Create the tables
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()