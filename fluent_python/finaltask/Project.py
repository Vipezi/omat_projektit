#! /usr/bin/python3

class Project:
    
    def __init__(self, project_name, employee, money):
        self.project_name = project_name
        self.employee = employee
        self.money = money

    def set_employee_name(self, employee):
        self.employee = employee
        return employee

    def change_amount(self, money):
        self.money = self.money - money
        return money