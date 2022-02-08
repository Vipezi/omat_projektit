#! /usr/bin/python3

# For communicating with sqlite database
import sqlite3

# Initialize connection to the database
# You can connect to file or memory (:memory:)
connection = sqlite3.connect("first.db")

cursor = connection.cursor()

# Execute SQL commands
#cursor.execute("DROP TABLE IF EXISTS users")
"""
cursor.execute('''
    CREATE TABLE users(
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    age SMALLINT,
    name TEXT)
    ''')


cursor.execute('''
    INSERT INTO users(age, name) VALUES
    (29, "Ville Vihtalahti"),
    (25, "Heli Vihtalahti")
''')
# For longer SQL commands

cursor.execute('''
  DROP TABLE
  IF EXISTS
  users
''')
"""

# Prints the name of the users tables
#for row in cursor.execute("SELECT name FROM users"):
#  print(row)

# Both are valid
#for row in cursor.execute("SELECT * FROM users"):
#  print(row[2])

# Check how many user/rows there are
#userAmount = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]
#print(userAmount)

#foundUser = cursor.execute("SELECT COUNT(*) FROM users WHERE userId == 1").fetchone()[0]
#if foundUser < 0: print("User was found!")
#else: print("User was not found!")

# DO NOT TO IT LIKE THIS!! SECURITY REASONS
#user3 = "Toni"
#user3 = input()
#cursor.execute(f"INSERT INTO users(age, name) VALUES (35,{user3})")


#Inserting new user into database with questionmark style
#user6 = "Joni"
#cursor.execute("INSERT INTO users(age, name) VALUES (?, ?)", (23, user6))

#cursor.execute("INSERT INTO users(age, name) VALUES (:age, :name)", {"age" : 42, "name" : "Annika"})

#for row in cursor.execute("SELECT * FROM users"):
#  print(row)

# Some examples where qmark / names style doesn't work

#tablename = "cars"
#cursor.execute("CREATE TABLE ? (carId INTEGRER), (tablename)")

# Question marks / named style does not work on tables/columns only VALUES!!!


users = [
  (11, "Mike"),
  (80, "Stephen"),
  (26, "Hailey")
]

# Inserting multiple users into table
# Amount of columns = amount of qmarks
cursor.executemany("INSERT INTO users (age, name) VALUES(?, ?)", users)

for row in cursor.execute("SELECT * FROM users"):
  print(row)

connection.commit()
connection.close()
