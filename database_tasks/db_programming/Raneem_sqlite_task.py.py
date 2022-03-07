#! /usr/bin/python3

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
cursor.execute("CREATE TABLE games (gameId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL NOT NULL)")

# 1.2) Create a table called users with the given structure:
  # userId: primary and automatically incrementing
  # name: cannot be empty
  # password: cannot be empty
  # email: unique, cannot be empty
cursor.execute("CREATE TABLE users (userId INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL, password TEXT NOT NULL, email TEXT UNIQUE NOT NULL)")


# 1.3) Create a table called userGames with the given structure:
  # userGameId: primary and automatically incrementing
  # userId: cannot be empty, foreign key to users
  # gameId: cannot be empty, foreign key to games
cursor.execute("CREATE TABLE userGames (userGameId INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER NOT NULL, gameId INTEGER NOT NULL, FOREIGN KEY(gameId) REFERENCES games(gameId),FOREIGN KEY(userId) REFERENCES users(userId))")


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
cursor.execute("INSERT INTO userGames (userId, gameId) VALUES (:userId, :gameId)", {"userId":1, "gameId":2})
cursor.execute("INSERT INTO userGames (userId, gameId) VALUES (:userId, :gameId)", {"userId":1, "gameId":3})



# 2.4 In table userGames, insert an entry where user with ID 2 will be associated with game 1.
#     Use named style. Do NOT insert the userGameId, just let it automatically increment.
cursor.execute("INSERT INTO userGames (userId, gameId) VALUES (:userId, :gameId)", {"userId":2, "gameId":1})


# 2.5 In table userGames, insert an entry where user with ID 3 will be associated with game 1.
#     Use qmark style. Do NOT insert the userGameId, just let it automatically increment.
cursor.execute("INSERT INTO userGames (userId, gameId) VALUES (?, ?)", (3,1,))



####################
# 3. UPDATING DATA #
####################

# 3.1 Change name of the game with ID 1 to Deathloop. Use qmark style.
cursor.execute("UPDATE games SET name=? WHERE gameId = 1", ('Deathloop',))

#for row in cursor.execute("SELECT * FROM games"):
#    print(row[1])
# 3.2 Change user with email address of pennypennie@gmail.com to newpenny@gmail.com.
#     Target with email address. Use named style.

# FOR THIS QUESTION,I THOUGHT I COULD ALSO USE REPLACE WITH THE UPDATE COMMAND,AND IT SEEM TO WORK GREAT. 
# I DECIDED TO PUT BOTH OF MY ANSWERS, JUST IN CASE, SINCE I WAS HAVING A HARD TIME SOLVING THE TASK WITH NAMED STYLE.
cursor.execute("UPDATE users SET email='newpenny@gmail.com' WHERE email=('pennypennie@gmail.com')")
cursor.execute("UPDATE users SET email=REPLACE(email,'pennypennie@gmail.com','newpenny@gmail.com')")
#for row in cursor.execute("SELECT * FROM users"):
#    print(row)

####################
# 4. REMOVING DATA #
####################

# 4.1 Remove game with ID 1. Use qmark style.
cursor.execute("DELETE FROM games WHERE gameId = ?",(1,))


###################
# 5. FINDING DATA #
###################

# 5.1 Find price for the game with ID 2. Use qmark style. Print out the result.
#     Expected output: Game ID 2 price: 49.99
price_game2 = cursor.execute("SELECT price FROM games WHERE gameId = 2").fetchone()[0]
if (price_game2 > 0): print(price_game2)
else: print("Price was not found")

# 5.2 Find the amount of all users. Print out the result.
#     Expected output: User amount: 3
usersAmount = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]
if (usersAmount > 0): print(usersAmount)
else: print("Users was not found")

# 5.3 Use JOIN to get user with ID 1 and their games (including game name). Use named style.
#     Print out names of the games that the user owns.
#     Expected output:
#        Resident Evil: Village
#        Farming Simulator 22

#? I wasnt able to execute the code properly, i have the idea on how to but i just cant seem to write it correctly


# 5.4 Print out the data in table games
#     Expected output:
#        (2, 'Resident Evil: Village', 49.99)
#        (3, 'Farming Simulator 22', 40.0)
for row in cursor.execute("SELECT * FROM games"):
    print(row)


# 5.5 Print out the data in table users
#     Expected output:
#        (1, 'Robert Ruthless', '123', 'rob@laws.com')
#        (2, 'Penny Pennie', 'abc', 'newpenny@gmail.com')
#        (3, 'Tomas Train', 'abc123', 'tomas@toottoot.com')
for row in cursor.execute("SELECT * FROM users"):
    print(row)
  

# 5.6 Print out the data in table userGames
#     Expected output:
#        (1, 1, 2)
#        (2, 1, 3)
#        (3, 2, 1)
#        (4, 3, 1)
for row in cursor.execute("SELECT * FROM userGames"):
    print(row)

#############
# 6. INPUTS #
#############

# 6.1 Ask user for name of the game and it's price. Insert the new game into the database using qmark style.
#     Expected output:
#        Name of the game? <input>
#        Price for the game? <input>

name = input("Name of the game? ")
price = float(input("Price of the game? "))

cursor.execute("INSERT INTO games (name,price) VALUES (?,?)", (name, price,))



connection.commit()
connection.close()