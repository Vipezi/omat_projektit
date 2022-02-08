#! /usr/bin/python3

def tuples2d_to_2dlists(a_tuple):
    a_list_of_tuples=[list(x) for x in a_tuple]
    return a_list_of_tuples


a_tuple = ((21,3),(4,5))
print(tuples2d_to_2dlists(a_tuple))