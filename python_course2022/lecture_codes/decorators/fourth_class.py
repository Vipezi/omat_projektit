#! /usr/bin/python3

class Zoo:
    def __init__(self, species, age, name):
        self.species = species
        self.age = age
        self.name = name
        
    def change_name(self, new_name):
        self.name = new_name
        print(new_name)

    def print_all_data(self):
        print(f"Species of animal is: {self.species}")
        print(f"Age of the animal is: {self.age}")
        print(f"Name of the animal is: {self.name}")

if __name__ == "__main__":
    zebra1 = Zoo("zebra", 74, "Arnold")

    print(zebra1.name)

    zebra1.change_name("Conan")
    zebra1.print_all_data()

