#! /usr/bin/python3


from functionality import *

# ADD DATA

addOneCar()
addMultipleCars()

# PRINT DATA
#printAllCars()
#removeCar()
#printSingleCar()

# EDIT DATA
#printSingleCar()
#editCar()
#printSingleCar()

# PRINT DATA: FILTERS
#printFilters()
#printOne()


# RELATIONSHIPS

#addInvoiceForCar()
#printCarInvoices()

manyToManyExample()

addNewCar("Ford", "Kuga")
removeItem(Car, Car.manufacturer == "Wolkswagen")

printAllCars()
# CLEANUP

removeAllCars()
removeAllInvoices()
removeAllPerson()
removeAllPersonCars()

