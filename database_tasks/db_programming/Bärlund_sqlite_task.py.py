#!/usr/bin/python3

# NOTES:
# - Please do not remove the comments attached in this file. Numbers and comments are helpful for the person who will be
#   reviewing your work.
# - If you cannot complete some task(s), please add a comment into it so it is easier for someone to verify that it has not been
#   implemented or has been implemented improperly.

# Initialize sqlite3 and the database

import sqlite3
database = "sqlite_tasks.db"
connection = sqlite3.connect(database) # Initialize connection to database, we could also use the parameter :memory:
cursor = connection.cursor() # Fetch cursor from connection

#########################
# 0. BOMBING THE TABLES #
#########################

# 0.1) Drop table games if it already exists

cursor.execute("DROP TABLE IF EXISTS games")

# 0.2) Drop table users if it already exists

cursor.execute("DROP TABLE IF EXISTS users")

# 0.3) Drop table userGames if it already exists

cursor.execute("DROP TABLE IF EXISTS userGames")

##########################
# 1. CREATING THE TABLES #
##########################

# Note: You need to come up with correct data types for all the fields yourself.
# Basic types in SQLite: TEXT, INTEGER, REAL

# 1.1) Create a table called games with the given structure:
  # gameId: primary and automatically incrementing
  # name: cannot be empty
  # price: cannot be empty

cursor.execute('''
  CREATE TABLE games (
    gameId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL)
''')

# 1.2) Create a table called users with the given structure:
  # userId: primary and automatically incrementing
  # name: cannot be empty
  # password: cannot be empty
  # email: unique, cannot be empty

cursor.execute('''
  CREATE TABLE users (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL)
''')

# 1.3) Create a table called userGames with the given structure:
  # userGameId: primary and automatically incrementing
  # userId: cannot be empty, foreign key to users
  # gameId: cannot be empty, foreign key to games

cursor.execute('''
  CREATE TABLE userGames (
    userGameId INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL,
    gameId INTEGER NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(userId),
    FOREIGN KEY(gameId) REFERENCES games(gameId))
''')


#####################
# 2. INSERTING DATA #
#####################

# 2.1 Insert the contents of variable games into the table games with qmark style.

games = [
  ("Dota 2", 0),
  ("Resident Evil: Village", 49.99),
  ("Farming Simulator 22", 40)
]

cursor.executemany("INSERT INTO games (name, price) VALUES (?, ?)", games)

# 2.2 Insert the contents of variable users into the table users with named style.

users = [
  { "name": "Robert Ruthless", "password": "123", "email": "rob@laws.com" },
  { "name": "Penny Pennie", "password": "abc", "email": "pennypennie@gmail.com" },
  { "name": "Tomas Train", "password": "abc123", "email": "tomas@toottoot.com" }
]

cursor.executemany("INSERT INTO users (name, password, email) VALUES (:name, :password, :email)", users)

# 2.3 In table userGames, insert an entry where user with ID 1 will be associated with games 2 and 3.
#     Use named style. Do NOT insert the userGameId, just let it automatically increment.

usergames = [
  { "userId": 1, "gameId": 2},
  { "userId": 1, "gameId": 3}
]

cursor.executemany("INSERT INTO userGames (userId, gameId) VALUES (:userId, :gameId)", usergames)

# 2.4 In table userGames, insert an entry where user with ID 2 will be associated with game 1.
#     Use named style. Do NOT insert the userGameId, just let it automatically increment.

cursor.execute("INSERT INTO userGames (userId, gameId) VALUES (:userId, :gameId)", { "userId": 2, "gameId": 1 })

# 2.5 In table userGames, insert an entry where user with ID 3 will be associated with game 1.
#     Use qmark style. Do NOT insert the userGameId, just let it automatically increment.

cursor.execute("INSERT INTO userGames (userId, gameId) VALUES (?, ?)", (3, 1))


####################
# 3. UPDATING DATA #
####################

# 3.1 Change name of the game with ID 1 to Deathloop. Use qmark style.

cursor.execute('''
  UPDATE games
  SET name = (?)
  WHERE gameId = (?)
''', ("Deathloop",1))

# Test to show that the changes have been made

print("")
print("Test to show that the changes in task 3.1 have been made:")
for x in cursor.execute('''
  SELECT
  *
  FROM games
'''):
  print(x)
print("")

# 3.2 Change user with email address of pennypennie@gmail.com to newpenny@gmail.com.
#     Target with email address. Use named style.

cursor.execute('''
  UPDATE users
  SET email = (:email)
  WHERE email = (:email2)
''', { "email": "newpenny@gmail.com", "email2": "pennypennie@gmail.com" })


####################
# 4. REMOVING DATA #
####################

# 4.1 Remove game with ID 1. Use qmark style.

cursor.execute('''
  DELETE FROM games
  WHERE gameId = (?)
''', (1,))


###################
# 5. FINDING DATA #
###################

# 5.1 Find price for the game with ID 2. Use qmark style. Print out the result.
#     Expected output: Game ID 2 price: 49.99

id = 2

print("Task 5.1:")
for x in cursor.execute('''
  SELECT
  price
  FROM games
  WHERE gameId = (?)
''',(id,)):
  print(f"Game ID {id} price: {x[0]}")
print("")

# 5.2 Find the amount of all users. Print out the result.
#     Expected output: User amount: 3

print("Task 5.2:")
for x in cursor.execute('''
  SELECT
  count(*)
  FROM users
'''):
  print(f"User amount: {x[0]}")
print("")

# 5.3 Use JOIN to get user with ID 1 and their games (including game name). Use named style.
#     Print out names of the games that the user owns.
#     Expected output:
#        Resident Evil: Village
#        Farming Simulator 22

print("Task 5.3:")
for x in cursor.execute('''
  SELECT
  g.name
  FROM userGames uG
  JOIN users u on u.userId = uG.userId
  JOIN games g on g.gameId = uG.gameId
  WHERE u.userId = (:userid)
''', { "userid": 1 }):
  print(x[0])
print("")

# 5.4 Print out the data in table games
#     Expected output:
#        (2, 'Resident Evil: Village', 49.99)
#        (3, 'Farming Simulator 22', 40.0)

print("Task 5.4:")
for x in cursor.execute('''
  SELECT
  *
  FROM games
'''):
  print(x)
print("")

# 5.5 Print out the data in table users
#     Expected output:
#        (1, 'Robert Ruthless', '123', 'rob@laws.com')
#        (2, 'Penny Pennie', 'abc', 'pennypennie@gmail.com')
#        (3, 'Tomas Train', 'abc123', 'tomas@toottoot.com')
# Note to reviewer: The second email should be newpenny@gmail.com and not pennypennie@gmail.com. Just a mistake in the material.

print("Task 5.5:")
for x in cursor.execute('''
  SELECT
  *
  FROM users
'''):
  print(x)
print("")

# 5.6 Print out the data in table userGames
#     Expected output:
#        (1, 1, 2)
#        (2, 1, 3)
#        (3, 2, 1)
#        (4, 3, 1)

print("Task 5.6:")
for x in cursor.execute('''
  SELECT
  *
  FROM userGames
'''):
  print(x)
print("")

#############
# 6. INPUTS #
#############

# 6.1 Ask user for name of the game and it's price. Insert the new game into the database using qmark style.
#     Expected output:
#        Name of the game? <input>
#        Price for the game? <input>

game = input("Name of the game? ")
price = float(input("Price for the game? "))
price_fix = "{:.2f}".format(price)
cursor.execute('''
  INSERT INTO games (name, price) VALUES (?,?)
''',(game,price_fix))

# Test to show that the changes have been made

print("")
print("Test to show that the changes in chapter 6 have been made:")
for x in cursor.execute('''
  SELECT
  *
  FROM games
'''):
  print(x)
print("")

connection.commit()
connection.close()