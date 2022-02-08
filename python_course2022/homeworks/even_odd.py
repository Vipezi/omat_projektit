#! /usr/bin/python3

def even_or_odd():
    which_one = int(input("Input a number:"))
    if which_one % 2 == 0:
        print(f"{which_one} is even")
    else:
        print(f"{which_one} is odd")