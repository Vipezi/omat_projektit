#! /usr/bin/python3

from fourth_class import Zoo
from datetime import date

class Animal(Zoo):
    @classmethod
    def max_age(cls, max_age):
        cls.max_age = max_age

    @staticmethod
    def zoo_location(name):
        if name == "first":
            print("London")
        elif name == "second":
            print("Paris")
        else:
            print("not known")

Animal.zoo_location("second")

dog1 = Animal("dog", 4, "Won Wuffester")
dog2 = Animal("dog", 6, "Doggester")


Animal.max_age(10)
print(dog1.max_age)
print(dog2.max_age)
print(Animal.max_age)

'''class Animal2(Zoo):
    @classmethod'''