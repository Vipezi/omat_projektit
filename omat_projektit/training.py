#! /usr/bin/python3

#https://www.practicepython.org/

#ex 1
"""
def hundred_age(age):
    answer = (2021 - age) +100
    return answer

name = input("Enter name: ")
age = int(input("Enter age: "))

answer=hundred_age(age)
print(f"{name} will be 100 years old in the year {answer}")"""

#ex 2

"""
num = int(input("Give a number: "))
check = int(input("Give a second number: "))
answer = num % check

if answer == 0:
    print(f"{num} can be divided evenly by {check}!")
else:
    print(f"{num} can't be divided evenly by {check}!")
"""

#ex 3

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(input("Give a number: "))
for i in a:
    if i < number:
        print(i)

print([i for i in a if i < number])
"""

#ex 4
"""
number = int(input("Give a number: "))

list_range = list(range(1,number+1))

divisor_list = []

for i in list_range:
    if number % i == 0:
        divisor_list.append(i)

print(divisor_list)
"""

#ex 5

"""

import random
randomlist = []
second_list = []
same_numbers = []
while len(randomlist) < 6 and len(second_list) < 6:
    n = random.randint(1,30)
    if n not in randomlist:
        randomlist.append(n)
    
    i = random.randint(1,30)
    if i not in second_list:
        second_list.append(i)
    
print(randomlist, second_list)
randomlist.sort()
second_list.sort()

[i for i, j in zip(randomlist, second_list) if i == j]
same_numbers.append(i)

print(randomlist, second_list)
print(same_numbers)

"""

#ex 6

"""
string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

"""