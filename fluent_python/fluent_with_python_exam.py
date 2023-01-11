#! /usr/bin/python3

# Exam Fluent With Python 29 Oct 2022
# Valentin Lhermitte
# Ville Vihtalahti
# melek chelik
# Sultanov Alisher

import random


hands = ['rock', 'paper', 'scissors', "quit"]

def random_choice():
    return random.randint(0, 2)

def user_choice():
    user_input = input("Press enter to play (rock, paper or scissors) : ")
    choice = hands.index(user_input.lower())
    return choice

def points(scores, result):
    scores[result] += 1
    scores["rounds"] += 1

# rock = 1, paper = 2, scissors = 3
def games(check):
    # We are making a dict to keep track of the scores
    scores = {"wins": 0, "losses": 0, "ties": 0, "rounds": 0}
    while check:
        # We ask the use for his choice, and we choose randomly for the computer
        computer = random_choice()
        user = user_choice()
        print(f"The computer chooses : {hands[computer]}")

        # We store the information about the user and the computer choice as number and not string,
        # because it is more efficient.
        if computer == user:
            print("It a tie !")
            points(scores, "ties")
        elif user == 0:
            if computer == 1:
                print("You win !")
                points(scores, "wins")
            else:
                print("You lose !")
                points(scores, "losses")
        elif user == 1:
            if computer == 0:
                print("You win !")
                points(scores, "wins")
            else:
                print("You lose !")
                points(scores, "losses")
        elif user == 2:
            if computer == 1:
                print("You win !")
                points(scores, "wins")
            else:
                print("You lose !")
                points(scores, "losses")
        elif user == 3:
            check = False
        else:
            print("Incorrect selection.")
    return scores


def main():
    check = True
    scores = games(check)
    print(f"You played {scores['rounds']} rounds.")
    print(f"You won {scores['wins']} times \n"
          f"You lost {scores['losses']} times \n"
          f"You tied {scores['ties']} times")


if __name__ == '__main__':
    main()
