#! /usr/bin/python3

"""
#Converting minutes to seconds

def second_converter(minutes: int):
    converted_result = minutes * 60
    return converted_result


minutes= int(input("Hello! I can convert minutes to seconds. Give me a number: "))
answer=second_converter(minutes)
print(f"{minutes} minutes is {answer} seconds.")
"""

"""
#Add 1 to each number

def add1(number: int):
    addition = number + 1
    return addition

number=int(input("Give a number: "))
answer=add1(number)
print(f" {number} is 1 smaller than {answer}")
"""

"""

#Counting the area of a triangle

def triangle_area_counter(base, height):
    area = (base * height)/2
    return area

x, y = input("Give me a base and height value: ").split()
x = int(x)
y = int(y)
answer = triangle_area_counter(x, y)
print(answer)
"""

"""

#Counting the cubic/cubed of a number

def cubed(number):
    cube = number * number * number
    return cube

x = int(input("What number do you want to be cubed? "))

result=cubed(x)
print(f"The cubed number {x} is {result}.")
"""


"""

#Counting the characters in a number

def number_length(number):
    counter = 0
    for char in number:
        counter += 1
    print(f"The number {num} has {counter} characters.")

num = input("Give a number and I will give you the character-length of the number: ")

number_length(num)
"""

"""

#Changing type from int to str and vice versa.

def int_to_str(number):
    number = str(number)
    print(type(number))
    return number

def str_to_int(string):
    string = int(string)
    print(type(string))
    return string


string_number = input("Give me a number: ")
number = int(input("Give me a number: "))

answer=str_to_int(string_number)
print(answer)

result=int_to_str(number)
print(result)"""

"""
# Checking if number is dividible by 3 or 5

def fizzerbuzzer(number):
    if number % 3 == 0 and number % 5 != 0:
        return "Fizz."
    elif number % 5 == 0 and number % 3 != 0:
        return "Buzz."
    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    else:
        number = str(number)
        print(type(number))
        return number

user_number = int(input("Lets check if number is a fizzbuzz: "))

FIZZ=fizzerbuzzer(user_number)
print(FIZZ)
"""

#from math import pi

"""
#Giving the multiplication table of a number until

def count(num, length):
    multiplication_table = []
    counter = 0
    while counter <= length-1:
        counter+=1
        answer = counter * num
        multiplication_table.append(answer)
    return multiplication_table

def count_2(num, length):
    multiplication_table = []
    counter = 0
    for i in range(0,length):
        counter+=1
        answer = counter * num
        multiplication_table.append(answer)
    return multiplication_table

x = int(input("Give a number: "))
y = int(input("And the table until: "))


result=count(x, y)
result2=count_2(x, y)
print(f"The first {y} numbers in the multiplication table of {x}: {result}")
print(f"The first {y} numbers in the multiplication table of {x}: {result2}")
"""


"""
# Calculating a countrys landmass in percents from the worlds

def area_of_country(country, mass):
    world_area = 148940000
    procent_of_world_area = mass/world_area
    return f"{country} is {str(round(procent_of_world_area*100, 2))}% of the total world's landmass."


country = input("Give me a country: ")
mass = int(input("Now give me the landmass of the country: "))
result=area_of_country(country, mass)
print(result)
"""
"""
#Testing classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old.")


p1 = Person("Ville", 28)
#p1.age = 29

#print(p1.name)
#print(p1.age)
p1.myfunc()
"""


"""
#Checking wovels in string

a_string = "abcde"
lowercase = a_string.lower() #Convert to lowercase.
vowel_counts = {}
for vowel in "aeiouyåäö":
    count = lowercase.count(vowel) #Count vowels.
    vowel_counts[vowel] = count #Add to dictionary.
print(vowel_counts)
"""


#Function to hide credit card number
"""
def maskify(cc):
    str = ''
    for char in cc[-4:]:
        str += '#'
    str += cc[-4:]
    return str

def maskify2(cc):
    new_string = ''
    if len(cc) > 4:
        new_string += '#' * (len(cc) - 4) + cc[4:]
    else:
        return cc
    return new_string

credit_card = input("Give card number: ")

result=maskify(credit_card)
result2=maskify2(credit_card) 
print(result, result2)
"""

#Password creater

"""from string import ascii_lowercase
import random

#print(ascii_lowercase)

random_list=list(ascii_lowercase)

alphabet = list(ascii_lowercase)

random_list.extend(alphabet)

j = 0

for x in range(9):
    for y in range(9):
        random_list.append(random.randint(1,9))

#print(random_list)

for x in range(10):
    random.shuffle(random_list)

#print(random_list)

sample=random.sample(random_list,10)

print(f"Here is a password suggestion: ", *sample)

"""

#