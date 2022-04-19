#! /usr/bin/python3

# Your final assignment is about creating a register /
# login functionality to your app.
# You need to also associate each todo item created in the database,
# with the corresponding logged-in user.
# For storing and retrieving the users you ARE REQUIRED TO USE SQLAlchemy.
# if not using SQLAlchemy, then the whole assignment will give you a direct fail (0 points).

# What you need to do:
# First, create table for holding users. 
# Class model should be called 'User' and name of the table should be 'users'.
#   The users table should have at least the fields userId, username and password.
#   Make sure that you also have foreign key relationship between
#    the items and users tables and relationship created from both tables
#    into each another.
# Before your main application launches,
#  it should ask the user if they want to REGISTER or LOGIN
#   If user wants to REGISTER,
#       the application should then ask the user for the username and password combination
#      If user with this username already exists in the table users,
#        app should notify about that and not create the new user
#      If this username did not exist, 
#        create account for the user in the table users
#   If user wants to LOGIN, then you need to ask user the username and password
#      If the given username and password combination does not exist in the table
#        users, then inform user about this and do not allow user into the system
#      If this username and password combination exists in the table users,
#        then allow the user in the system and store the user that logged in
# Finally, you will also need to associate each item created with the logged-in user.
#  This way each logged-in user will have their own todo items.

import sys
from database import Item, session, User, UserItem
from getpass import getpass

# Main app function
def main(userId):
  while True:
    print("\nWhat do you want to do today?")
    print("1: View todo items")
    print("2: Create new todo item")
    print("3: Remove item")
    print("4: Exit")
    print("5: Clean user table ps. Admin only\n")
    selection = input()
    if (selection == "1"): showItems(userId)
    elif (selection == "2"): createItem(userId)
    elif (selection == "3"): removeItem(userId)
    elif (selection == "4"): sys.exit("Goodbye!")
    elif (selection == "5"): removeAccount()


# Lists all todo items
def showItems(userId):
  print("\nYour todo lists:")
  print("---")
  items = session.query(Item)
  for item in items:
    print(item.itemId, ": " + item.name)
  print("---\n")

# Creates new todo item
def createItem(userId):
  global items
  print("Name for the item:")
  itemName = input()
  newItem = Item(name = itemName)

  session.add(newItem)
  session.commit()

# Removes todo item with ID
def removeItem(userId):
  itemAmount = session.query(Item).count()

  if (itemAmount < 1):
    print("You should add some items first.")
    return
  
  print("Give ID:")
  itemId = int(input())

  removableItem = session.query(Item).filter(Item.itemId == itemId)

  if (removableItem.count() > 0):
    session.delete(removableItem.one())
    session.commit()
  else:
    print("Invalid ID!")

def removeAccount():
  session.query(User).delete()
  session.commit()
  # This is just for cleaning the whole users table
    

def create_account():
  print("----------------\n")
  while True:
    username = input("Input username: ")
    password = getpass("Input password: ")
    user = session.query(User).filter(User.userName == username).first()
    if user is None:
      session.add(User(
        userName = username,
        password = password
      ))
      session.commit()
      print("User created! \n")
      login()
    else:
      print("Username already exists. Try another one.")
      break
  

def login():
  print("----------------\n")
  while True:
    username = input("Input username: ")
    password = getpass("Input password: ")
    user = session.query(User).filter(User.userName == username , User.password == password).first()
    if user is None:
      print("Invalid user or password! Try again.\n")
    else:
      print("Logged in! \n")
      for userId in users.userId
      main(userId)
  
# Start the app

print("Welcome to TOD-O LIST O-MAKER Version 5123.524")
while True:
  choice = input("""Type 'register' to make a new account
or 'login' to log in to an existing account. Anything else typed
will exit the programm: """)
  if choice == "register":
    create_account()
  elif choice == "login":
    login()
  else:
    print("Goodbye!")
    break
      

#main()