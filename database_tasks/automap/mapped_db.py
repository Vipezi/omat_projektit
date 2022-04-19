#! /usr/bin/python3

# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Car(Base):
    __tablename__ = 'cars'

    carId = Column(Integer, primary_key=True)
    manufacturer = Column(String, nullable=False)
    model = Column(String, nullable=False)

    persons = relationship('Person', secondary='personcars')


class Person(Base):
    __tablename__ = 'persons'

    personId = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer)


class Invoice(Base):
    __tablename__ = 'invoices'

    invoiceId = Column(Integer, primary_key=True)
    carId = Column(ForeignKey('cars.carId'))
    description = Column(String)
    amount = Column(Float, nullable=False)

    car = relationship('Car')


t_personcars = Table(
    'personcars', metadata,
    Column('personId', ForeignKey('persons.personId'), primary_key=True, nullable=False),
    Column('carId', ForeignKey('cars.carId'), primary_key=True, nullable=False)
)
