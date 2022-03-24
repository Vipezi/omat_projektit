#! /usr/bin/python3
import numpy as np

my_first_set = {1,5,6,7}

# Set does not have indexes
# It can not have duplicates
# But you can add

my_first_set.add(5)

# Or update
my_first_set.update(["Come", "along"])
print(my_first_set)

my_list = [1,2,3,4,5]
second_set = set(my_list)
print(second_set)

new_set = set((1,2,4))
print(new_set)

# Takes one of each characters found in string
characters = set("I said yeeeeeeah")

# Raises and error if not in set
characters.remove("I")

# Does not raise an error if not in set
characters.discard("s")
print(characters)

# Set comprhension

set_comprehension = {x for x in my_list}
set_comprehension = {x for x in [1,2,3,4,5,6]}
set_comprehension = {x**x for x in range(10) if x % 3 == 0}


print(set_comprehension)



dict1 = {1:"1", 2:"2", 3:"3"}
# Get keys and values from dicts 
set_to_dict = set(dict1)
set_to_dict_keys = set(dict1.keys())
set_to_dict_values = set(dict1.values())
print(set_to_dict, set_to_dict_keys, set_to_dict_values)

# array to set

an_array = np.array([1,2,3,8,9])
array_to_set = set(an_array)
print(array_to_set)

## Define a function called dict_to_tuple_sets, that takes in a dictionary,
## and returns tuple that has 4 elements, where:
## 1. element is set of dictionary keys
## 2. element is set of dictionary values
## 3. element is a Boolean, where it should we true, if sets are equal long, false if other is shorter.
## 4. element is length of the keys in integer

def dict_to_tuple_sets(dictionary):
    set_to_dict_keys = set(dictionary.keys())
    set_to_dict_values = set(dictionary.values())
    if len(set_to_dict_values) == len(set_to_dict_keys):
        returned_tuple = (set_to_dict_keys, set_to_dict_values, True, len(set_to_dict_keys))
        return returned_tuple
    else:
        returned_tuple = (set_to_dict_keys, set_to_dict_values, False, len(set_to_dict_keys))
        return returned_tuple
