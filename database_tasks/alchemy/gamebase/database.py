#! /usr/bin/python3

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
# Establish connection to in-memory database.
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

# Import declarative_base that is required to create the ORM tables
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# YOUR CODE GOES HERE


# Finally, remember to create the tables with this
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()