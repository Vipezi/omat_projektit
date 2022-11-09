#! /usr/bin/python3

# Ville Vihtalahti
# From the variable names one can guess that this was
# supposed to be a rock paper scissors game.
# The code had many bugs and functionality issues
# Now it should work good. I made some changes, but overall the code looks fine
# I did not add functions or any other fancy things.
# I made also and own implementation for this.

import random


def games ():
  userpoints = 0
  rounds = 0
  losses = 0
  choices = ["rock","paper","scissors"]
  while True:
    print("")
    user_choice = input("Rock, paper or scissors? Or type 'quit' to exit the program. ")
    
    if user_choice in choices:
      print("You chose: ", user_choice)
      computer_choice = random.choice(choices)
      print("Computer choosed: ", computer_choice)
      print("")
      if user_choice == "rock" and computer_choice == "scissors":
        print("You WIN!")
        userpoints += 1

      elif user_choice == "scissors" and computer_choice == "paper":
        print("You WIN!")
        userpoints += 1

      elif user_choice == "paper" and computer_choice == "rock":
        print("You WIN!")
        userpoints += 1

      elif computer_choice == "rock" and user_choice == "scissors":          
        print("You LOSE!")
        losses += 1

      elif computer_choice == "paper" and user_choice == "rock":
        print("You LOSE!")
        losses += 1

      elif computer_choice == "scissors" and user_choice == "paper":
        print("You LOSE!")
        losses += 1

      elif user_choice == computer_choice:
        print("It's a tie")
        rounds += 1

    elif user_choice == "quit":
      rounds = rounds + losses + userpoints
      print(f"You played {rounds } rounds, won {userpoints} times and lost {losses} times.")
      break

    else :
      print("Incorrect selection. Be sure to write in lowercase letters.")
      print("The program is very case sensitive. Be aware of typos. :)")
      print("")
  
  
  
def main():  
    games()

if __name__ == "__main__":
    main()
