#! /usr/bin/python3

city_list = ["pori", "turku"]

city ="pori"

print(len(city_list))
print(len(city))

class Organism:
    def __init__(self, species):
        self.species = species
        #self.max_age = max_age

    def print_species(self):
        print(self.species)

    def print_max_age(self):
        print("max age for organism is 4841")

class Animal(Organism):
    def print_max_age(self):
        print("max age for animal is 190")

tree = Organism("pine")
tree.print_max_age()
turtle = Animal("turtle")
turtle.print_max_age()

# now we can iterate over objects from different classes, and use same method name in calls
# even methods that are different. This is polymorphism

for age in (tree, turtle):
    age.print_max_age()

