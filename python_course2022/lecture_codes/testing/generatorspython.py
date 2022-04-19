#! /usr/bin/python3

import time
#x = [y for y in range(100_00_00_00)]
#time.sleep(5)

def numbers_for_ever():
    next_number = 0
    while True:
        yield next_number
        next_number += 1

ready_generator_to_use = numbers_for_ever()

print(ready_generator_to_use)

#print(next(ready_generator_to_use))
#print(next(ready_generator_to_use))
print(next(ready_generator_to_use))
print(next(ready_generator_to_use))

'''for item in ready_generator_to_use:
    pass'''

def yield_something_for_limited_times(times):
    strings = ["first string", "second string", "third string"]
    for i in range(times):
        for string in strings:
            yield string

string_gen = yield_something_for_limited_times()

print(next(string_gen))
print(next(string_gen))
print(next(string_gen))
print(next(string_gen))

#print(next(yield_something_for_limited_times()))
#print(next(yield_something_for_limited_times()))


#####

def numbers_for_ever(number=0):
    next_number = 0 + number
    while True:
        yield next_number
        next_number += 1

ready_generator_to_use = numbers_for_ever(5)

print(ready_generator_to_use)

#print(next(ready_generator_to_use))
#print(next(ready_generator_to_use))
print(next(ready_generator_to_use))
print(next(ready_generator_to_use))



# Define a generator called strings_from_list that yields string from the list,
# after list is empty, yields type None

#list of strings:
 
# This will be the first of many.
# Now we get to the second phase of the things.
# We are at middle point already.
# I don't have that much more to say, sorry.
# This will be the last entry, I hope this was enough for you.

def strings_from_list():
    list_of_strings = ["This will be the first of many.", "Now we get to the second phase of the things.",
    "We are at middle point already.", "I don't have that much more to say, sorry.", "This will be the last entry, I hope this was enough for you."]
    num = 0
    while True:
        try:
            yield list_of_strings[num]
            num += 1
        except IndexError:
            yield None

# Define a generator called powers_of_number, generator is infinite generator that yield a tuple of powers where
# first element is power to 0,
# second power to 1,
# third is power to 2,
# fourth is power to 3

# if no argument is given, then first base number is 0,
# if argument is given, then that number is first base number

def powers_of_number(number = 0):
    if number != 0:
        while True:
            yield(number**0, number**1, number**2, number**3)
            number += 1
    else:
        while True:
            yield(number**0, number**1, number**2, number**3)
            number += 1

# Define a generator called next_fibonacci that yields next fibonacci number
def next_fibonacci():
    a = 0
    b = 1
    sum = 0
    count = 1
    while True:
        yield sum
        count +=1
        a = b
        b = sum
        sum = a + b

# Define a generator called next_fibonacci that yields next fibonacci number,
# it can take an argument that start yielding the series from that point, or next bigger,
# if number given is not fibonacci number

def next_fibonacci(n=0):
    if 0 == n:
        yield 0
    a = 0
    b = 1
    sum = 0
    count = 1
    while True:
        a = b
        b = sum
        sum = a + b
        if sum >= n:
            yield sum


#define a generator called: numbers_names_cities
#that yields in sequence next item from list names,
#then next from salary,
#and then next fron city,
#Then second item from names ...
#These are given to generator as list arguments, 3 arguments
#this is done until generator is yielded number of times that was given to generator as argument as int,
#so generator takes in 4 arguments, first 3 lists and then int.
#StopIteration exception if given, if generator is asked to yield after number specified
#You can also break your answer to for example in to two different generators, and call first one from the second.

def numbers_names_cities(names, salaries, cities, times):
    #import copy
    all_of_them = []
    for (a, b, c) in zip(names, salaries, cities):
        all_of_them.append(a)
        all_of_them.append(b)
        all_of_them.append(c)
    copied_list = all_of_them.copy()
    for i in range(times):
        yield all_of_them[i]
        all_of_them.append(all_of_them[i])

#define a generator called abc_numbers that yields infinite sequence

#"a","b","c",0,"a","b","c",1,"a","b","c",2,"a","b","c",4,"a","b","c",8,"a","b","c",16,"a","b","c",32,"a","b","c",64........

def abc_numbers():
    counter = 0
    while True:
        yield "a"
        yield "b"
        yield "c"
        if counter == 0 or counter == 1:
            yield counter
            counter += 1
        elif counter > 1:
            yield counter
            counter *= 2

#define a generator called chars_in_line that processes one line from file at the time,
#and yields how many chars there are in the line.

def chars_in_line(file):
    with open(file, 'r') as f:
        for line in f:
            yield len(line)

#Define a generator called: text_crawler that opens a file, with name that is given as argument.
#Another argument is a string, generator yield next line, if given string is in line,
#otherwise yields None type

def text_crawler(file, string):
    with open(file, 'r') as f:
        for line in f:
            if string in line:
                yield line
            else:
                yield None

