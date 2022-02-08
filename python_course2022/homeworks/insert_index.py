#! /usr/bin/python3

def insert_index():
    my_list =["yes","no","yes","no","yes","no","no"]
    something=input("Say something here !: ")
    number=int(input("Enter a number: "))
    my_list.insert(number, something)
    print(my_list)

insert_index()