#! /usr/bin/python3

import random

def number_of_sides_in_dice(throws,number_of_sides):
    roller = [i for i in range(1, number_of_sides+1)]
    random_choice = random.choice(roller)
    print(f" You throwed on your {throws} throw: {random_choice}")
    all_together.append(random_choice)
    
    
def amount_of_throws(number_of_throws):
    throws = 0
    for i in range(number_of_throws):
        throws = throws + 1
        number_of_sides_in_dice(throws,number_of_sides)

while True:
    all_together = []
    again=input("Type y to begin the game or anything else to exit? ")
    
    if again == "y":
        number_of_sides=int(input("How many sided dice do you want to throw? "))    
        number_of_throws=int(input("How many times do you want to throw? "))
        amount_of_throws(number_of_throws)
        results=sum(all_together)
        print(f"The sum of all your resulst are {results}")
        

    else:
        print(f"And here is the sum of all your throws in the game {sum(all_together)}")
        break
    






