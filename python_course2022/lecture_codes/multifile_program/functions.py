#! /usr/bin/python3

import os

def useless_function(value1=2, value2=1):
    answer = value1 - value2 * value2
    return answer

print(os.getpid())

if __name__ == '__main__':
    print("This is from functions.py")
    print(useless_function(4,5))
    print(useless_function())
