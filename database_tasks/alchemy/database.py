#! /usr/bin/python3

from sqlalchemy import create_engine

# Establish connection to in-memory database.
# If parameter echo is True, will print all SQL queries to console. Can be also set to False.
# Parameter future needs to be True to use the latest sqlalchemy 2.0 engine functionality.
engine = create_engine("sqlite+pysqlite:///carDatabase.db", echo=False, future=True)

# Import declarative_base that is required to create the ORM tables
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

# Model for a car
class Car(Base):
  __tablename__ = "cars"
  carId = Column(Integer, primary_key = True, autoincrement = True)
  manufacturer = Column(String, nullable = False)
  model = Column(String, nullable = False)
  invoices = relationship("Invoice", back_populates = "cars", cascade = "all, delete, delete-orphan")
  persons = relationship("Person", secondary = "personcars", back_populates = "cars", cascade = "all, delete, delete-orphan", single_parent = True)

# Model for a car invoice
class Invoice(Base):
  __tablename__ = "invoices"
  invoiceId = Column(Integer, primary_key = True)
  # Define foreign key
  carId = Column(Integer, ForeignKey('cars.carId'))
  description = Column(String, nullable = True)
  amount = Column(Float, nullable = False)
  cars = relationship("Car", back_populates = "invoices")

# Model for a person
class Person(Base):
  __tablename__ = "persons"
  personId = Column(Integer, primary_key = True, autoincrement = True)
  firstname = Column(String, nullable = False)
  lastname = Column(String, nullable = False)
  age = Column(Integer, nullable = True)
  cars = relationship("Car", secondary = "personcars",back_populates = "persons", cascade = "all, delete-orphan", single_parent = True ) 

# Associative table model for cars and persons
class PersonCar(Base):
  __tablename__ = "personcars"
  personId = Column(Integer, ForeignKey("persons.personId"), primary_key = True)
  carId = Column(Integer, ForeignKey("cars.carId"), primary_key = True)


# Create the tables
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()