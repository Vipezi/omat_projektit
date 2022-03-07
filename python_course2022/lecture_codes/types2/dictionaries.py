#! /usr/bin/python3

import pandas as pd


#print(first_dict)

# does not work the same ways when printing a list, there is no order.
# keyerror
# do not use index first_dict[0], use key

list_example = [1,2,3]
#print(list_example[0])

# update dict
#first_dict["height"] = [178, 183]
#print(first_dict)

def dict_from_list(list_to_in):
    dict_to_return = {}
    for i in range(len(list_to_in)):
        dict_to_return[str(i)] = list_to_in[i]
    return dict_to_return

#print(dict_from_list(list_example))

first_dict = { "name" : ["Ville","Kalle"] ,"age" : [29, 31], "is a live" : [True, False] }
list_inside_dict = pd.DataFrame.from_dict(first_dict)
#print(list_inside_dict.head())

person1 = {"name" : "Harri", "age" : 34, "is alive" : True}
person2 = {"name" : "Jari", "age" : 31, "is alive" : True}
person3 = {"name" : "Jore", "age" : 40, "is alive" : False}

humans = {
    "person1" : person1,
    "person2": person2,
    "person3" : person3
    }

dict_inside_dict = pd.DataFrame.from_dict(humans)
#print(dict_inside_dict.head())

# person1 and humans["person1"] have same memory address
person1["name"] = "Kari"
#print(humans)
#print(id(humans))
#print(id(humans["person1"]))
#print(id(person1))


humans2 = {
    "person1" : person1.copy(),
    "person2": person2.copy(),
    "person3" : person3.copy()
    }

#print(id(humans2))
#print(id(humans2["person1"]))
#print(id(person1))

# use deep copy on nested dictionaries and other types as well
# shallow copy has same memory address
humans3 = humans.copy()

import copy

humans4 = copy.deepcopy(humans)
print(id(person1))
print(id(humans["person1"]))
print(id(humans2["person1"])) 
print(id(humans3["person1"])) 
print(id(humans4["person1"])) # deep copy
