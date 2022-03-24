#! /usr/bin/python3

def calculator(operation, number1, number2):
    if operation == "add":
        answer = number1 + number2
    elif operation == "multiply":
        answer = number1 * number2
    else:
        answer = ""
    return answer

#print(calculator("add", "kind", "mind"))