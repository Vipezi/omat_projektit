#! /usr/bin/python3

from database import session, Game, User, UserGame

# Find Dota game
def printOne():
    game = session.query(Game).filter( Game.name == "Dota 2").first()
    if game is not None:
        print(game.name)
