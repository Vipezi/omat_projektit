#! /usr/bin/python3


### Except without ValueError. Infinite loop. CTRL + C not working
'''
while True:
    try:
        answer = input("give a number: ")
        int_answer = int(answer)
        print("You wrote a valid number!")
        break
    except:
        print("Not a valid number")'''


#calculation = int(answer)*3
#print(calculation)

"""while True:
    try:
        answer = input("give a number: ")
        int_answer = int(answer)
        print("You wrote a valid number!")
        break
    except ValueError as e:
        print(f"{type(e).__name__} was raised: {e}")
        print("Not a valid number")"""

def safe_divider(num1, num2):
    try:
        result = num1 / num2
        a_tuple = (result, 0, '')
        return a_tuple
    except(ValueError, ZeroDivisionError) as error:
        return ((0, 1, (error)))

def file_printer(file_name):
    try:
        with open(file_name, 'r') as f:
            content=f.read()
            print(content)
    except:
        print("file not found")




def inputter():
    exceptions = []
    while True:
        try:
            num1 = input("give 1. number: ")
            converted_int1 = int(num1)
            num2 = input("give 2. number: ")
            converted_int2 = int(num2)
            
            print(converted_int1 + converted_int2)
            print(converted_int1 / converted_int2)
            break
        except ValueError as error:
            exceptions.append(error)
            continue
    return exceptions