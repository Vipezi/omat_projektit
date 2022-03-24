#! /usr/bin/python3

#tuple_values = (66,64,78,4,5)
#print(tuple_values)
'''
# We can take values from tuples with the comma
one, two, three, four, five = tuple_values
print(one)

one = tuple_values[0]
two = tuple_values[1]
three = tuple_values[2]
four = tuple_values[3]
five = tuple_values[4]
print(two)

a, b, c, *d = tuple_values

print("*********")

print(a)
print(b)
print(c)
print(d)
'''

# Generate random dict with numbers in letters as keys and nummbers as values
# pip install inflect
import inflect
import random
p = inflect.engine()
a_dict = {}
random_numbers = random.sample(range(1, 30), 10)

for num in random_numbers:
    number_to_word=p.number_to_words(num)
    a_dict[number_to_word] = num

print(a_dict)


def show_cities(*args):
    print(f"cities to print")
    #for city in args:
    #    print(city)

#show_cities("Pori", "Helsinki", "Rome")

dict1 = {1 : "v1", 2 : "v2", 3 : "v3"}
dict2 = {4 : "v4", 5 : "v5", 6 : "v6"}

# Prints only the keys
dict3 = {*dict1, *dict2}
#print(dict3)

# Combine two dictionaries
dict3 = {**dict1, **dict2}
#print(dict3)

'''def average_house_value(**keyword):
    print(f"The type of kwargs is: {type(keyword)}")
    for key, value in keyword.items():
        print(f"key: {key}, value: {value}")


average_house_value(Pori = 100000, Turku = 200000, Helsinki = 400000)'''


# Join words of tuple to string

def string_combiner(*args):
    for word in args:
        print(word)
    args=''.join(args)
    return args