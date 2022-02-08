#! /usr/bin/python3

def Singular_numbers(integrer):
    uneven_list = []
    while integrer > 0:
        if integrer % 2 == 1:
            uneven_list.insert(0, integrer)
        integrer = integrer - 1
    return uneven_list