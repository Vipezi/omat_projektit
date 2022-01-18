#! /usr/bin/python3


while True:
    print("I am sleeping")
    user_input = input("Did you set the alarm?")
    if user_input == "yes" or user_input == "Yes":
        print("Wake up!!")
        break
    else:
        print("let me sleep")
        print("...")
        continue