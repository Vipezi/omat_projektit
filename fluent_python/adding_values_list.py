#! /usr/bin/python3

def empty_finder(a_list):
    length_of_list = len(a_list)
    i = 0
    new_list = []
    while i < length_of_list:
        if isinstance(a_list[i], int):
            new_list.append(a_list[i])
            i+=1
        else:
            break
    return new_list

print(empty_finder([1,2,3,4,5,"",42,6,7]))