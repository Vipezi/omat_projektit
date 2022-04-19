#! /usr/bin/python3

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()
engine = create_engine("sqlite:///cardb_automap.db")
Base.prepare(engine, reflect=True)

# Base.classes.tablename
# relationships: Base.classes.tablename.tablename_collection

#print(Base.classes.cars)

# Function that prints all table structures in the database for reference
def describeDatabase(engine):
  from sqlalchemy.inspection import inspect
  from sqlalchemy import MetaData
  print("\n---- STARTING TO PRINT DATABASE STRUCTURE")

  metadata_obj = MetaData()
  metadata_obj.reflect(bind=engine)
  for table in metadata_obj.sorted_tables:
    print("\n- DESCRIBE TABLE:", table)
    print("Access with: " , "Base.classes.", table)
    print("Columns:")
    for col in table.columns:
      print(col)
  # Printing table relationships for reference
  print("\n- STARTING TO PRINT RELATIONSHIPS\n")
  for item in Base.classes:
    inspectedItem = inspect(item)
    print("Table", item, "has these relationships:")
    print(inspectedItem.relationships.items())
  print("\n---- END PRINTING DATABASE STRUCTURE")
#describeDatabase(engine)


Car = Base.classes.cars
Invoice = Base.classes.invoices
Person = Base.classes.persons

session = Session(engine)

# Add new car
session.add( Car( manufacturer = "Test", model = "Test") )
session.commit()

# Find all cars
allCars = session.query(Car)
for car in allCars:
    print(car.manufacturer, car.model)

# Relationships
# Find the person with lastname mctester
person = session.query(Person).filter( Person.lastname == "mctester").first()
for car in person.cars_collection:
    print("Person owns: ", car.manufacturer)
