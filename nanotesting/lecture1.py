#! /usr/bin/python3

def function_with_return(input_to_function1, input_to_function2):
    variable_that_we_return_from_function = input_to_function1 + input_to_function2
    return variable_that_we_return_from_function


# call to function

answer_to_print1 = function_with_return(1,4)
print(answer_to_print1)
