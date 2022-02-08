#! /usr/bin/python3

def grocery_list():
    list_of_groceries = []
    number_of_groceries = 0
    while True:
        answer=input("Hello! Please write product name below or write ! to stop the program!: ")
        if answer == "!":
            number_of_groceries = len(list_of_groceries)
            break
        else:
            list_of_groceries.append(answer)
    return list_of_groceries, number_of_groceries
    

gl=grocery_list()

print(gl)


