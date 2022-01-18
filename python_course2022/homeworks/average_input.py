#! /usr/bin/python3

how_many_numbers = int(input("How many numbers will you be inputting?"))

i = 0
number_list = []
while i < how_many_numbers:
    number = int(input("Enter number"))
    number_list.append(number)
    i += 1
average=sum(number_list) / len(number_list)
print(f"The average is {average}")
