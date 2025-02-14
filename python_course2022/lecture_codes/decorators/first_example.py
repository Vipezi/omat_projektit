#! /usr/bin/python3

def normal_function():
    print("I am just a normal function")

normal_function()

def i_am_a_decorator(func):
    def inner():
        print("This here is the wrapper around the original function")
    return inner

decorator = i_am_a_decorator(normal_function)
decorator()


@i_am_a_decorator
def normal_function2():
    print("I am just a normal function")
    
@i_am_a_decorator
def normal_function3():
    print("I am also a normal function")

normal_function2()
normal_function3()