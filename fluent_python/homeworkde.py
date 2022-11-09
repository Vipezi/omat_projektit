#! /usr/bin/python3

def sum_list(numbers): 
    """This function sum the value from a list of numbers and return a number
    """
    result = 0
    for x in numbers:
        result += x 
    return result  

# return should be outside of loop
# it does not add the values to one another,
# because the result gets returned everytime it loops,
# and therefore the previous number,
#  does not exist anymore inside the function



def main():
    my_numbers= [1,3,4,5,56,64,345]
    resultOfSum = sum_list(my_numbers)
    print(resultOfSum)

if "__name__" == main():
    main()