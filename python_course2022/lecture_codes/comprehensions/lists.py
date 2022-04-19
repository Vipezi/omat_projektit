#! /usr/bin/python3

newlist = [x for x in range(10, 50, 5)]
#print(newlist)

newlist2 = [x for x in range(100) if x%3 ==0]
#print(newlist2)

# Make a list from 0-99, and keep values that are divisible with 5, if not change value to x
# https://pythonguides.com/python-list-comprehension-using-if-else/

newlist3 = [x if x % 5== 0 else "x" for x in range(100)]
#print(newlist3)

# Changed order
newlist4 = ["x" if x % 5 else x for x in range(100)]
#print(newlist4)

###################
# Copying the previous list

newlist5 = [x for x in newlist3]
print(newlist5)

#nested_list = [[x for x in range(100) if x%3 == 0],[x for x in range(100) if x%3 != 0]]
#print(nested_list)


## write a list comprehension to variable true_list, list has as many items that is number in variable List_length,
## if numbers remainder when divided with 5 or 2 is 0, item is 0, other wise it is the index number
List_length = 100
true_list = [0 if x % 5 == 0 or x % 2 == 0 else x for x in range(List_length)]


## Define a function called random_value_from_dict, that takes in one argument, a dictionary.
## using random librarys choise, take one random key, and return value from that key.


import random

def random_value_from_dict(dictionary):
    value = random.choice(list(dictionary.values()))
    return value

# original author: Emil Khaibrakhmano
# I the author grant the use of this code for teaching: yes
# Define a function called a_letter_finder, that takes in 1 argument, a string sentence
# Find all words in sentence that end in "a" and join them together separated by an hyphen -.
# return joined string
# sample input / output
# >>> cyberpunk replica doom dota supermarket formula good bad banana, replica-dota-formula-banana

def a_letter_finder(sentence):
    s = ""
    for word in sentence.split():
        if word.endswith("a"):
            s +=word+"-"
    return s[:-1]

# Original author: Jussi Lehtonen
# I the author grant the use of this code for teaching: yes

##Write a function named nth_lowest that takes list as argument and finds the nth lowest number from it.
##If the list contains strings your functions should convert them to int.
##If the list contains something else your function should remove them.
##For example:
##temp_list = [10,'4',None, 20, 2, 5, '100', True]
##nth_lowest(temp_list, 2)
##Would then find second lowest number on the list which is 4

def nth_lowest(number,alist):
    alist = list(filter(lambda num: type(num) == str or type(num) ==int, alist))
    alist = list(map(int, alist))
    alist.sort()
    return alist[number-1]

# original author: Juuso Lehtonen
# I the author grant the use of this code for teaching: yes

# (use pythons random module)
# Write a program with a while loop that has a 1% chance of stopping every loop!
# With every loop a number is
#  added to a list. The number has a 85% to be 0-9, 10% to be 10-99 and a 5% chance to be a 100.
# Sort the numbers in ascending order into three lists inside another list. First list with single digits, second with double digits and third with three digits.
# Sum the numbers and see which has the highest sum, one, two or three digit numbers.

import random
def roll():
    lists = [[],[],[]]
    while True:
        exit = random.randrange(0,99)
        if exit == 99:
            break
        else:
            chance = random.randint(0,99)
            if chance < 85:
                single = random.randint(0,9)
                lists[0].append(single)
            elif chance == 99:
                lists[2].append(100)
            else:
                double = random.randint(10,99)
                lists[1].append(double)
    sorted_list = [sorted(i) for i in lists]
    the_list = [sum(lists[0]), sum(lists[1]), sum(lists[2])]
    print(sorted_list) 
    print(the_list)


##################################################################################

# original author: anonymous student
# I the author grant the use of this code for teaching: yes, if my name isn't used.

#Write a function called check_password, that takes in a string and checks if it is a valid password. Returns Boolean True if valid.
#For a password to be valid it needs to:
#Has at least 1 capital and non capital letter.
#Has at least 1 number
#Has at least 1 special character from: [#$@]
#Is between 8 and 18 characters long
#Hint: Use RegEx module and remember passwords don't contain spaces.

import re

def check_password(string):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    pat = re.compile(reg)
    mat = re.search(pat, string)
    if mat:
        return True
    else:
        return False
