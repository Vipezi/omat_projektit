#! /usr/bin/python3

def ask_user():
    answers = []
    for i in range(5):
        user_input=int(input("Yes or No :"))
        answers.append(user_input)
    return answers