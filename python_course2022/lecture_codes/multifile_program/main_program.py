#! /usr/bin/python3

import os


from functions_no_name_is_main import useless_function
from functions import useless_function as useless_function2

print(useless_function2(30,4))
print(useless_function(30,4))
print(os.getpid())
