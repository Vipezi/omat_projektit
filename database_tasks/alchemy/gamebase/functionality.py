#! /usr/bin/python3

from todo_assignment.database import session, Game, User, UserGame

# Using SQLAlchemy, find the game with the name Dota 2.
#  Store the result in a variable game. Print the name of the found game.
game = session.query(Game).filter( Game.name == "Dota 2").first()
if game is not None:
    print(game.name)

#1) Find all users and store the results in variable users
#2) Create a variable userNames
#3) Use a for loop and store each name of the user inside the variable userNames,
# separated by a comma. Leave the last comma inside the variable.
# See the example below for example output.
users = session.query(User)
userNames = ""
for user in users:
    userNames += user.name + ","

# 1) Use OR to find users with password 123, abc123 and store the results in variable users
# 2) Create a variable userNames
# 3) Use a for loop and store each name of the user inside the variable userNames, separated by a comma.
# Leave the last comma inside the variable. 
# See the example below for example output.
users = session.query(User).filter( (User.password == "123") | (User.password == "abc123") )
userNames = ""
for user in users:
    userNames += user.name + ","

# 1) Find all games with price over 10 and store the results in variable games
# 2) Create a variable gameNames
# 3) Use a for loop and store each name of the game inside the variable gameNames, separated by a comma.
#  Leave the last comma inside the variable. 
# See the example below for example output.
games = session.query(Game).filter( Game.price > 10 )
gameNames =""
for game in games: gameNames += game.name + ","

# Using SQLAlchemy,  insert a new Game with the given details:
# name: Elden Ring
# price: 60
session.add(Game(
    name = "Elden Ring",
    price = 60
    ))
session.commit()

# Create a list that contains the User objects described below. 
# Name the variable as newUsers. 
# Insert the user objects into the database using the session.add_all function.
# User 1
# name: Nanny Nameless
# password: 123
# email: nan@nan.com
# User 2
# name: Tommy Timeless
# password: tom
# email: tom@timeless.com
  
newUsers = session.add_all([
    User(name = "Nanny Nameless", password = "123", email = "nan@nan.com"),
    User(name = "Tommy Timeless", password = "tom", email = "tom@timeless.com")
    ])
session.commit()

# Create and insert a User and a Game described below. 
# Associate the newly added Game for the User. Use SQLAlchemy.
# User
# name: Nanny Nameless
# password: 123
# email: nan@nan.com
# Game
# name: Tetris
# price: 999

newUser = User( name = "Nanny Nameless", password= "123", email="nan@nan.com")
newGame = Game( name = "Tetris", price = 999)
session.add(newUser)
session.add(newGame)
relation = session.query(Game).filter( Game.name == "Tetris").first()
newUser.games.append(relation)

session.commit()

# Using SQLAlchemy, remove the game with ID 3 from the database.
game = session.query(Game).filter( Game.gameId == 3).first()
session.delete(game)
session.commit()

# Using SQLAlchemy, remove the game with the name Dota 2 from the database.
game = session.query(Game).filter( Game.name == "Dota 2").first()
session.delete(game)
session.commit()

# Using SQLAlchemy, remove all data from the table objects Game, User and UserGame.
# Do NOT hardcode names of the records when removing them, 
# but dynamically remove all the records.

allGames = session.query(Game)
allUsers = session.query(User)
for user in allUsers:
    session.delete(user)

for game in allGames:
    session.delete(game)

session.commit()

# Using SQLAlchemy, find a user with the name Tomas Train. 
# Remove game with the name Dota 2 from that user. 
# Do NOT directly use the UserGame object.

user = session.query(User).filter( User.name == "Tomas Train").first()
for game in user.games:
    if game.name == "Dota 2":
        user.games.remove(game)
session.commit()

# Using SQLAlchemy, find the user by email address pennypennie@gmail.com
# and update the user's email address to newpenny@gmail.com and password to pennies.

user = session.query(User).filter( User.email == "pennypennie@gmail.com" ).first()
user.email = "newpenny@gmail.com"
user.password = "pennies"
session.commit()

# Using SQLAlchemy, find the game by the name 
# Farming Simulator 22 and update the price to 33.

game = session.query(Game).filter( Game.name == "Farming Simulator 22" ).first()
game.price = 33
session.commit()

# Create a function addNewGame that accepts the parameters name, price.
# Make the function insert a new game
# with the given parameters into the database using SQLAlchemy.

def addNewGame(name, price):
    newGame = Game( name = name, price = price)
    session.add(newGame)
    session.commit()

# Create a function removeGame that accepts parameter gameId. 
# Make the function remove the given game from the database.
# If the game that needs to be removed was found, the function should finally return text REMOVED. 
# If the game with the given ID was not found, the function should return text NOTREMOVED.

def removeGame(gameId):
    game = session.query(Game).filter( Game.gameId == gameId).first()
    try:
        session.delete(game)
        return "REMOVED"
        session.commit()
    except:
        return "NOTREMOVED"

# Create a function getAllRecords that accepts parameter tableObject. 
# Parameter tableObject is your table's object, like User or Game. 
# Make the function return number of records in the given table.
# NOTE: When doing the session.query, you can replace the table with tableObject. 
# For example User can be replaced with tableObject.

def getAllRecords(tableObject):
    number_of_records= session.query(tableObject)
    length = []
    for amount in number_of_records:
        length.append(amount)
    return len(length)