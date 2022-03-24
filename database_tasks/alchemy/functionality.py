#! /usr/bin/python3

from database import session, Car, Invoice, Person, PersonCar

# INSERT FUNCTIONALITY

def addOneCar():
  session.add(Car(
    manufacturer = 'Tesla',
    model = 'Model 3'
  ))
  session.commit()

def addMultipleCars():
  session.add_all([
    Car(manufacturer = "Porche", model = "Cayenne"),
    Car(manufacturer = "Wolkswagen", model = "ID.3"),
    Car(manufacturer = "Ford", model = "Mondeo"),
    Car(manufacturer = "Wolkswagen", model = "Golf")
  ])
  session.commit()

def addInvoiceForCar():
  ford = session.query(Car).filter( Car.manufacturer == "Wolkswagen", Car.model == "Golf" ).first()
  ford.invoices.append( Invoice( description = "Fixed brakes of the car.", amount = 340.50 ) )
  session.commit()

# PRINT FUNCTIONALITY

def printAllCars():
  allCars = session.query(Car)
  if (allCars is None): return

  for car in allCars:
    print(car.manufacturer, car.model)

def printSingleCar():
  car = session.query(Car).filter( Car.manufacturer == "Ford" ).first()
  if (car is not None):
    print(car.manufacturer, car.model)
  else:
    print("Single car was not found!")

def printFilters():
  # >: Print first car with ID larger than 1
  car = session.query(Car).filter( Car.carId > 1 ).first()
  print(car.carId, car.manufacturer, car.model)

  # <: Print all cars with ID less than 3
  cars = session.query(Car).filter( Car.carId < 3 )
  for car in cars: print(car.carId, car.manufacturer, car.model)

  # AND: Print car that has model "Model 3" and manufacturer "Tesla"
  car = session.query(Car).filter( Car.model == "Model 3", Car.manufacturer == "Tesla" ).first()
  print(car.carId, car.manufacturer, car.model)

  # LIKE: Print car that has manufacturer like 'wagen'
  car = session.query(Car).filter( Car.manufacturer.like("%wagen%") ).first()
  print(car.carId, car.manufacturer, car.model)

  # IN: Print cars that have manufacturer Wolkswagen or Ford
  cars = session.query(Car).filter( Car.manufacturer.in_( [ "Wolkswagen", "Tesla" ] ) )
  for car in cars: print(car.carId, car.manufacturer, car.model)

  # OR: Print cars that have manufacturer Wolkswagen or Ford
  print("OR:")
  cars = session.query(Car).filter( (Car.manufacturer == "Wolkswagen") | (Car.manufacturer == "Ford") )
  for car in cars: print(car.carId, car.manufacturer, car.model)

  # OR & AND: Print cars that have model "ID.3" OR model "Golf" AND the manufacturer is "Wolkswagen"
  print("OR AND:")
  cars = session.query(Car).filter( (Car.model == "ID.3") | (Car.model == "Golf"), Car.manufacturer == "Wolkswagen" )
  for car in cars: print(car.carId, car.manufacturer, car.model)

  # SORT BY: Find all cars with ID over 1, sorted by manufacturer in ascending order
  # Note: import desc for descending order
  from sqlalchemy import asc
  cars = session.query(Car).filter( Car.carId > 1 ).order_by( asc( Car.manufacturer ) )
  print("ORDER BY:")
  for car in cars: print(car.carId, car.manufacturer)

  # LIMIT: Find all cars with ID over 1, order by carId asc, limit to 2 entries
  cars = session.query(Car).filter( Car.carId > 1 ).order_by( asc( Car.carId ) ).limit(2)
  print("LIMIT:")
  for car in cars: print(car.carId, car.manufacturer)

def printOne():
  from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

  try:
    #car = session.query(Car).filter( Car.carId == 1 ).one()
    car = session.query(Car).filter( Car.carId > 0 ).one()
    #car = session.query(Car).filter( Car.carId == 8 ).one()
    print(car.carId, car.manufacturer, car.model)
  except NoResultFound:
    print("No results found!")
  except MultipleResultsFound:
    print("Multiple results found, when one was required!")

def printCarInvoices():
  car = session.query(Car).filter( Car.manufacturer == "Wolkswagen", Car.model == "Golf" ).first()
  for invoice in car.invoices:
    print(invoice.description, invoice.amount)

# REMOVE FUNCTIONALITY

def removeAllCars():
  # Automatic way
  session.query(Car).delete()
  session.commit()

  # Manual way
  #allCars = session.query(Car)
  #for car in allCars:
  #  session.delete(car)
  #session.commit()

def removeAllInvoices():
  session.query(Invoice).delete()
  session.commit()

def removeAllPersonCars():
  session.query(PersonCar).delete()
  session.commit()

def removeAllPerson():
  session.query(Person).delete()
  session.commit()

def removeCar():
  car = session.query(Car).filter( Car.manufacturer == "Ford" ).first()
  session.delete(car)
  session.commit()

# UPDATE FUNCTIONALITY

def editCar():
  car = session.query(Car).filter( Car.model == "Mondeo" ).first()
  car.model = "Fiesta"
  session.commit()

# MANY TO MANY EXAMPLE:

def manyToManyExample():
  # Add new person
  newperson = Person( firstname = "Test", lastname = "mctester", age = 22)
  session.add(newperson)

  # Find first car with model 3
  car = session.query(Car).filter( Car.model == "Model 3").first()


  # Associate person with the found car
  newperson.cars.append(car)
  session.commit()

  # Find all persons, print them out alongside the cars they own
  allPersons = session.query(Person)
  for person in allPersons:
    carAmount = len(person.cars)
    print(person.firstname, person.lastname, "owns cars: ")
    print(carAmount)
    for car in person.cars:
      print(car.carId, car.manufacturer, car.model)
      # Car is Model 3? 
      # The we can remove that association from that person
      if car.model == "Model 3":
        person.cars.remove(car)
        session.commit()

# FUNCTION PARAMETERS

def addNewCar(manufacturer, model):
  newCar = Car( manufacturer = manufacturer, model= model)
  session.add(newCar)
  session.commit()

def removeItem(model, filters):
  item = session.query(model).filter( filters )
  item.delete()
  session.commit()