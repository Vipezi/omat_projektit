#! /usr/bin/python3

## I decided to use a different approach
## First I ask how many numbers the user wants to use
## Then I make a list of all the numbers added
## Then I ask what operator the user wants to use
## Addition, I decided to first sum all the values in the list, which was easy with the sum function
## Substraction, I sliced the first number and substracted the whole sum from the first number
## Multiplication, I used numpy.prod which multiplies all the numbers with eache other


import numpy as np

def list_maker(amount):
    list_of_numbers = []
    for i in range(amount):
        number = int(input("Please add the number: "))
        list_of_numbers.append(number)
    return list_of_numbers


def calculate(numberlist):
    op = ['+', '-', '*']
    print(f"Please chose one of these as your operator: {op}")
    choice = input()
    if choice == '+':
        result = sum(numberlist)
        return result
    elif choice == '-':
        result = numberlist[0] - sum(numberlist[1:])
        return result
    elif choice == '*':
        result = np.prod(numberlist)
        return result
    else:
        print("Not a valid operator.")
        
def main():
    while True:
        amount = int(input("Please tell me the amount of numbers you want to use? "))
        numberlist = list_maker(amount)
        print(f"Here are your numbers: {numberlist}")
        print("")
        answer = calculate(numberlist)
        print(answer)
        end = input("Type y to continue. Anything else will end the program. ")
        if end == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()

