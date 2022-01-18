#! /usr/bin/python3

import numpy as np

# My version
num=[6,9,1,3,2]
result = num[0] * num[1]

i = 1

while i < 4 :
    i += 1
    result = result * num[i]

print(result)


# Tonis version
num=[6,9,1,3,2]

result = 1
i = 0

while i < len(num):
    result = result * num[i]
    i += 1

print(result)


#My way
num=[5,4,3,2,1]
result = 0 - num[0] - num[1]

i = 1

while i < len(num) - 1:
    i += 1
    result = result - num[i]

print(result)

#Tonis way
num=[5,4,3,2,1]

result = 0
i = 0

while i < len(num):
    result = result - num[i]
    i += 1

print(result)