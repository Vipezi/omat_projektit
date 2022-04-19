#! /usr/bin/python3

class Animal:
    def __init__(self, age):
        self.age = age

zebra = Animal(20)
horse = Animal(12)

#print(f"Combined age of the animals is: {zebra.__add__(horse)}")

x = 1
y = 1

# These two lines does the same thing
#print(x+y)
#print(x.__add__(y))

class Animal2:
    def __init__(self,age):
        self.age = age
    
    def __add__(self, other):
        return self.age + other.age

zebra2 = Animal2(20)
horse2 = Animal2(12)

print(f"Combined age of the animals is: {zebra2 + horse2}")

#zebras = [a for a in Animal 2range()]
#print(zebras)