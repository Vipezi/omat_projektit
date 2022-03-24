#! /usr/bin/python3

def ask_number():
    while True:
        try:
            number_input = int(input("Give me a number as digit: "))
            return number_input
            
        except ValueError:
            pass


if __name__ == "__main__":
    ask_number()