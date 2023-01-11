#! /usr/bin/python3

from Project import *

def main():
    print("Welcome to the Projector app!")
    print("")
    project = Project("Scorpio", "Ville Vihtalahti", 56656)
    print(project.employee)

    project.set_employee_name("Kalle")
    print(project.employee)

    project.change_amount(6000)
    print(project.money)

if __name__ == "__main__":
    main()