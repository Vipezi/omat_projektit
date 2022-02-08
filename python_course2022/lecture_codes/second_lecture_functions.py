#! /usr/bin/python3
#lotto numbers
"""
import random

def lucky_numbers():
    number=random.randint(1,50)
    return number

lotto_numbers = int(input("How many random lotto numbers do you want?"))
your_numbers = []
while len(your_numbers) < lotto_numbers:
    number=lucky_numbers()
    if number not in your_numbers:
        your_numbers.append(number)

print(sorted(your_numbers))
"""

# simplest function
"""
print("this")
int("10")

def simplest_function():
    pass

simplest_function()
"""

"""
def new_function():
    print("I am a function and I will always print this ")

new_function()
"""

# range function
"""
def new_function_with_argument(input_to_function):
    for i in range(input_to_function):
        print("I am a function and I will always print this ")

new_function_with_argument(2)
"""

# function with return
"""
def function_with_return(input_to_function1, input_to_function2):
    variable_we_return_from_function = input_to_function1 + input_to_function2
    return variable_we_return_from_function

returned_value=function_with_return(5,3)
print(returned_value)

returned_value=function_with_return("5","3")
print(returned_value)

returned_value=function_with_return("five","three")
print(returned_value)
"""

# for loop
"""
for i in range(6):
    print("something")

for i in range(2,6):
    print("something")

for i in range(2,6,2):
    print("something")

"""

#default value for argument

"""
def function_with_return(input1, input2=0, input3=0):
    variable_we_return_from_function = input1 + input2 + input3
    return variable_we_return_from_function

print(function_with_return(1))
print(function_with_return(1,3))
print(function_with_return(1,3,5))
"""
#with infinite amount of inputs

def function_with_n_args(*inputs):
    sum = 0
    for i in range(len(inputs)):
        sum = sum + inputs[i]
    return sum

def function_with_n_args(*inputs):
    sum = 0
    for i in inputs:
        sum = sum + i
    return sum

print(function_with_n_args(1,2,3,4))
print(function_with_n_args(1,2,3))
print(function_with_n_args(1,2,3,4,5,6,7))

