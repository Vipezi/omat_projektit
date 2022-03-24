#! /usr/bin/python3

# zip go make tuples from lists etc.

from itertools import zip_longest

list1 = [1,2,3,4]

list2 = ["one", "two", "three", "four"]

# combine list to tuple
a_tuple = zip(list1, list2)
'''
print(type(a_tuple))

for i in a_tuple:
    print(i)

for i in zip(range(4), list2):
    print(i)
'''


#print(list(zip(list1,list2)))

list3 = list(a_tuple)

#print(list3)

dict_to_zip = {1: "1", 2: "2", 3 : "3" }

for i in zip_longest(range(10), list2):
    print(i)


#Make a script that take in 2 lists: list1 , list2
#and combine them to tuple using zip, to the variable called combined_list

#Define a function called: zipper that takes in a list
#function returns a zip object where first item is number from 0 to n-1
#where n is number of elements in the function argument list

def zipper(a_list):
    second_list = [x for x in range(len(a_list))]
    zipped_object = zip(second_list,a_list)
    return zipped_object

#Define a function, called zip_longest_zeroes, that takes in 2 lists, and make a zip, as long longer list,
#by padding the sorter list with 0 values.
#function returns that zip, list1 is first element and list2 is second element in zip.

def zip_longest_zeroes(list1, list2):
    if len(list1) == len(list2):
        zipped_list = zip(list1,list2)
        return zipped_list
    else:
        if len(list1) > len(list2):
            difference = len(list1) - len(list2)
            listofzeros = [0] * difference
            list2.extend(listofzeros)
            zipped_list = zip(list1,list2)
            return zipped_list
        elif len(list1) < len(list2):
            difference = len(list2) - len(list1)
            listofzeros = [0] * difference
            list1.extend(listofzeros)
            zipped_list = zip(list1,list2)
            return zipped_list
