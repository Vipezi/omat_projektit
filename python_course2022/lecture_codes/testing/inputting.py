#! /usr/bin/python3

def ask_from_user():
    answer = input("Do you want to continue?")
    if answer == "yes":
        return True
    else:
        return False