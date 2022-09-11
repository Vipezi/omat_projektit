#! /usr/bin/python3


from unicodedata import name


class CustomerInfo:
    def __init__(self, name):
        self.name = name

        
    def add_info(self, name, age):
        self.age = age

    def get_age(self, age):
        print(self.age)
        
        
table = CustomerInfo(['Maria', 'Paul', 'Jenny', 'Markus']) 
table.add_info('Maria', 55) 
table.add_info('Paul', 34) 
table.add_info('Jenny', 45) 
table.add_info('Markus', 15)

table.get_age('Maria')