#! /usr/bin/python3

# Binary means that you have 2 values
# 0,1
# 0,1,2,3,4,5,6,7,8,9. 11

### base2 to base 10
#base10 = int(base2,2)

### zip lists to dictionary
'''abbreviation = ['AI', 'EENGR', 'CS'] 

values = ['Artificial Intelligence','Electrical Engineer','Computer Science']
dicto=dict(zip(abbreviation,values))
print(dicto)


### Append value to dict
my_dict = { "a": 1,"b": 2, "c": 3,"d":4}

my_dict["e"] = 5 

### Convert binary to base ten
def ten_baser(binary):
    number = int(binary,2)
    return number
    

### Function to convert string to int
def hexer(hexadecimal):
    try:
        #hexadecimal = hex(hexadecimal)
        integer = int(hexadecimal,16)
    except:
        print("not a valid hexadecimal")
        return 0
    return integer'''
        

'''print(11)
# print in binary form
print(bin(11))

for i in range (0,20):
    print(f"number {i} = {bin(i)} binary")
    #print(f"number {i} = {binhex(i)} binary")

import numpy as np
x = np.array([1,], dtype=np.uint16)
x = np.array([1,], dtype=np.uint8)

x[0] = 1

print(x[0])

x[0] = 14
print(x[0])

x[0] = 400
print(x[0])

print(bin(400))
print(bin(144))'''
### Convert a tuple of ints to different bases

def multi_baser(a_tuple):
    d = {}
    for i in a_tuple:
        d[i] = {"base10" : i, "base2" : bin(i), "base16" : hex(i)}
    return d

print(multi_baser((60,2,35)))

def pics_to_tuples(dictionary):
    #print(dictionary)
    new_d ={}
    for key, value in dictionary.items():
        if value not in new_d:
            new_d[value] = [key]
        else:
            new_d[value].append(key)
    for i,j in new_d.items():
        j=tuple(j)
        new_d[i] = j
    return new_d

def pics_from_tuples(dict_in):
    dict_to_return = {}
    for label in dict_in:
        for picture in dict_in[label]:
            dict_to_return[picture] = label
    return dict_to_return