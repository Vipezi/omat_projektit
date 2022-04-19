#! /usr/bin/python3

# Using list comprehension with classes.

our_list = [x for x in range(10)]
power_of_two_list = [x**2 for x in range(10)]

class Animal:
    def __init__(self, age):
        self.age = age

animal_with_age = Animal(20)
animals = [Animal(x) for x in range(10)]
animals2 = [Animal(x) for x in power_of_two_list]

#for animal in animals: print(animal.age)

print(animals[5].age)

for animal in animals:
    animal.age = 40
    animal.name = "Cat"

#for animal in animals: print(animal.age), print(animal.name)

