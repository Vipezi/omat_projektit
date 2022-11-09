#! /usr/bin/python3

# Ville Vihtalahti

### This is just me of finding my own way of doing this
### I thought about doing the rock, paper, scissors comparing
### how much place they all take in memory

#import sys
#memory_size_rock = sys.getsizeof("rock")
#memory_size_paper = sys.getsizeof("paper")
#memory_size_scissors = sys.getsizeof("scissors")
#print(memory_size_rock)
#print(memory_size_paper)
#print(memory_size_scissors)

import random
def points(games, result):
    games[result] += 1

def computer_choice(choices):
    hand = random.choice(choices)
    return hand

def game():
    games = {"wins": 0, "losses": 0, "ties": 0}
    choices = ["rock","paper","scissors"]
    
    while True:
        computer_hand = computer_choice(choices)
        player_hand = input("Rock, paper or scissors? Type 'quit' to end the game: ")
        print(f"You choosed: {player_hand} and the computer choosed: {computer_hand}")
        if player_hand in choices:
            if player_hand == computer_hand:
                print("It's a tie.")
                points(games, "ties")

            elif player_hand == "rock":
                if computer_hand == "scissors":
                    print("You win!")
                    points(games, "wins")
                else:
                    print("You lose.")
                    points(games, "losses")
            elif player_hand == "paper":
                if computer_hand == "rock":
                    print("You win!")
                    points(games, "wins")
                else:
                    print("You lose.")
                    points(games, "losses")
            elif player_hand == "scissors":
                if computer_hand == "paper":
                    print("You win!")
                    points(games, "wins")
                else:
                    print("You lose.")
                    points(games, "losses")

        elif player_hand == "quit":
            print("Goodbye!")
            print(f"Here are your stats: {games} ")
            break

            
        else:
            print("Not a valid answer. Try again")
  
def main():
    print("Welcome to a game of rock paper scissors! Type 'y' to start the game.")
    print("If you write anything else I will exit the game.")
    answer = input()
    if answer == "y":
        game()
    else:
        print("goodbye!")

if __name__ == "__main__":
    main()

