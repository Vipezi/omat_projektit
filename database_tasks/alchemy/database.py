#! /usr/bin/python3

from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///carDatabase.db", echo = True, future = True)

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

class Invoice(Base):
  __tablename__ = "invoices"
  invoiceId = Column(Integer, primary_key = True, autoincrement = True)
  carId = Column(Integer, ForeignKey('cars.carId'))
  description = Column(String, nullable = True)
  amount = Column(Float, nullable = False)
  cars = relationship("Car", back_populates = "invoices")

# Create the tables
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()