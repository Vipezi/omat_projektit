#! /usr/bin/python3

import random

def second_dice_game(number_of_sides):
    roller = [i for i in range(1, number_of_sides+1)]
    random_choice = random.choice(roller)
    return random_choice

def results(number_of_throws):
    throws = 0
    for i in range(number_of_throws):
        throws = throws + 1
        numbers=second_dice_game(number_of_sides)
        all_together.append(numbers)
        print(f"Your {throws} throw is: {numbers}")

    Sum=sum(all_together)
    print(f"Here is the sum of all your throws: {Sum}")

while True:
    all_together = []
    again=input("Type y to begin the game or anything else to exit? ")
    if again == "y":
        number_of_sides=int(input("How many sided dice do you want to throw? "))    
        number_of_throws=int(input("How many times do you want to throw? "))
        results(number_of_throws)
    else:
        break
    






