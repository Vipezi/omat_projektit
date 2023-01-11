#! /usr/bin/python3

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

    def animal_sound(self, sound):
        return f"{sound} said the {self.species}"

    def set_weight(self, weight):
        self.weight = weight
        return weight

    def set_height(self, height):
        self.height = height
        return height

    def set_color(self, color):
        self.color = color
        return color

    def set_gender(self, gender):
        self.gender = gender
        return gender

    def set_speed(self, speed):
        self.speed = speed
        return speed
    
    
