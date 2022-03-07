#! /usr/bin/python3

from database import session, Car, Invoice

# INSERT FUNCTIONALITY

def addOneCar():
  session.add(
    Car(
      manufacturer = "Tesla",
      model = "Model 3"
    )
  )

  #firstCar = Car(manufacturer = "test", model = "test2")
  #session.add(firstCar)
  #session.commit()

def addMultipleCars():
    session.add_all(
        [
            Car(manufacturer = "Porche", model = "Cayenne"),
            Car(manufacturer = "Volkswagen", model = "Golf"),
            Car(manufacturer = "Ford", model = "Mondeo"),
            Car(manufacturer = "Seat", model = "Leon" )
        ]
    )
    session.commit()

# PRINT FUNCTIONALITY

def printAllCars():
    allCars = session.query(Car)
    if allCars is None: return

    for car in allCars:
        print(car.manufacturer, car.model)

def printSingleCar():
    car = session.query(Car).filter(Car.manufacturer == "Ford").first()
    if car is not None:
        print(car.manufacturer, car.model)
    else:
        print("Single car was not found.")