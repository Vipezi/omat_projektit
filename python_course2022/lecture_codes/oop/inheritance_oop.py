#! /usr/bin/python3


class Organism:
    def __init__(self,  species):
        self.species = species

    def print_species(self):
        print(self.species)

worm = Organism("worm")
worm.print_species()

# We can make child class from Organism, 
# by giving the name of the class as an "argument"
# when we make a child class

# simplest example of the inheritance
'''
class Animal(Organism):
    pass

bird = Animal("bird")
bird.print_species()
'''



# Inheritance with child methods
class Animal2(Organism):
    def print_species_2_times(self):
        for x in range(2):
            print(self.species)

bird = Animal2("bird")
#bird.print_species()
bird.print_species_2_times()

# with inherited init plus child init

class Animal3(Organism):
    def __init__(self, species, speed):
        Organism.__init__(self, species)
        self.speed = speed

bird3 = Animal3("bird", 6)
bird3.print_species()

# with inherited init plus child init, the other way

class Animal4(Organism):
    def __init__(self ,species, speed):
        super().__init__(species)
        self.speed = speed

eagle = Animal4("eagle", 6)
eagle.print_species()


class Animal5(Organism):
    def __init__(self ,species, speed):
        super().__init__(species)
        self.speed = speed

    def print_all(self):
        print(self.species , self.speed)

eagle = Animal5("eagle", 6)
eagle.print_all()