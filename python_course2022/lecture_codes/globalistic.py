#! /usr/bin/python3

# this is a global variable
"""
x = 4
print(x)

def for_testing(x):
    x = 3
    print(x)

for_testing(x)
print(x)

# normal way to go from local- to global variable using return
def for_testing(x):
    x = 3
    print(x)
    return x

x = for_testing(x)
print(x)


# changing character types
x = str(x)
print(type(x))

a = 4
b = 3
c = a/b
print(c, type(c))

# printing whole numbers with two //
e = 3
f = 4
g = f // e
print(g)

# python rounds numbers down, even if the decimal is over 5

# number in 1d line:
# 4 -4,-3,-2,-1,0,1,2,3,4

# complex number is 2d number, so it is just point in plane
# real part, like 4, imaginary part 4j

k = 4j + 4j
print(k)
print(type(k))

# complex numbers can not be converted to int

# use real function
l = k.real
print(l)
print(type(l))

p = f"with f strings you can have text and variables in the same line {l} {k} {a}"
print(p)

v = [i for i in range(10)]

print(v)
print(v[0])

# to add numbers always use append or insert
v.append(12)

v[2] = "You are the best"
print(v)

# mutable and immutable
x = 1001
print(id(x))

x = 1002
print(id(x))

q = [1,2,3]
print(q)
print(id(q))

q[0] = 4
print(id(q))


def list_f(list_to_f):
    list_to_f[0] = "change from function"

list_f(q)

print(q)
print(id(q))

list1 = [i for i in range(10)]
#print(list1)

#print(id(list1))

list3 = list1.copy
list2 = list1[:]


print(id(list1), id(list2), id(list3))

# tuples are immutable, they do not support item assignment
a_tuple = ("you", "can not", "change", "me")

a_tuple2 = tuple(list1)
a_list = list(a_tuple2)

print(a_tuple2, a_list)

import copy

def realizator(list_of_complex_numbers):
    a_copy = copy.deepcopy(list_of_complex_numbers)
    for i in range(len(a_copy)):
        for u in range(len(a_copy[i])):
            a_copy[i][u] = a[i][u].real
    tuple_to_return = tuple(a_copy)

    return tuple_to_return

list_of_numbers = [[1+2j],[2+3j],[3+4j],[4+5j],[5+6j]]

print(realizator(list_of_numbers))



def tuplenator(a_list):
    length_of_list = len(a_list)
    sum_of_list = sum(a_list)
    a_tuple=a_list.copy()
    a_tuple.insert(0,length_of_list)
    a_tuple.insert(1,sum_of_list)
    a_tuple=tuple(a_tuple)
    return a_tuple

number_list = [2,6,4,10]

print(tuplenator(number_list))

"""



def list_mutator(a_list):
    shallow_list = a_list.copy()
    i, j = 0, 1
    fibo_list = [0,1]
    count = 0
    ones = []
    for x in range(len(shallow_list)):
        ones.append(1)
    while count < len(shallow_list):
        #print(i)
        result = i + j
        i = j
        j = result
        fibo_list.append(j)
        count += 1
    #print(fibo_list)
        
    shallow_list_modified = [ones[fibo_list.index(i)] if i in fibo_list else shallow_list[i] for i in range(len(shallow_list))]
    
    return shallow_list_modified

 #0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
        
       

a_list = [1, 3, 4, 6, 10, 13, 15, 17, 19]
print(list_mutator(a_list))

