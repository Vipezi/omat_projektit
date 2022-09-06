#! /usr/bin/python3

# Your final assignment is about creating a register / login functionality to your app.
# You need to also associate each todo item created in the database with the corresponding logged-in user.
# For storing and retrieving the users you ARE REQUIRED TO USE SQLAlchemy. if not using SQLAlchemy, then the whole assignment will give you a direct fail (0 points).

# What you need to do:
# First, create table for holding users. Class model should be called 'User' and name of the table should be 'users'. 
#   The users table should have at least the fields userId, username and password. 
#   Make sure that you also have foreign key relationship between the items and users tables and relationship created from both tables into each another.
# Before your main application launches, it should ask the user if they want to REGISTER or LOGIN 
#   If user wants to REGISTER, the application should then ask the user for the username and password combination 
#      If user with this username already exists in the table users, app should notify about that and not create the new user 
#      If this username did not exist, create account for the user in the table users 
#   If user wants to LOGIN, then you need to ask user the username and password 
#      If the given username and password combination does not exist in the table users, then inform user about this and do not allow user into the system 
#      If this username and password combination exists in the table users, then allow the user in the system and store the user that logged in 
# Finally, you will also need to associate each item created with the logged-in user. This way each logged-in user will have their own todo items.

import sys
from database import Item, session, User, LogIn

# Main app function
def main():
  while True:
      print("\nWhat do you want to do today?")
      print("1: View todo items")
      print("2: Create new todo item")
      print("3: Remove item")
      print("4: Exit\n")
      selection = input()
      if (selection == "1"): showItems()
      elif (selection == "2"): createItem()
      elif (selection == "3"): removeItem()
      elif (selection == "4"): sys.exit("Goodbye!")

# Lists all todo items
def showItems():
  print("\nYour todo lists:")
  print("---")
  user = session.query(User).filter(User.username == login_username).first()
  for item in user.items:
        print(item.itemId, ": " + item.name)
  print("---\n")

# Creates new todo item
def createItem():
  itemName = input("Name for the item:\n")
  user = session.query(User).filter(User.username == login_username).first()
  user.items.append(Item(name = itemName))
  session.commit()

# Removes todo item with ID
def removeItem():
  user= session.query(User).filter(User.username == login_username).first()
  itemAmount = len(user.items)

  if (itemAmount < 1):
    print("You should add some items first.")
    return
  
  itemId = int(input("Give ID:\n"))

  removedItem = False
  for item in user.items:
    if item.itemId == itemId:
      removedItem = True
      session.query(Item).filter(Item.itemId == item.itemId).delete()
      session.commit()
      print("Item succesfully removed!")

  if removedItem == False:
      print("Invalid ID!")

# Start the app
print("Welcome to TOD-O LIST O-MAKER Version 5123.524")

# Login/register functionality
def register_login():
  global login_username
  while True:
    user_choice = input("Do you want to register or login? (register/login): \n")
    if user_choice  == 'register':
      False
      # -------- REGISTER FUNCTION -------- #
      new_username = input('Input your new username: ')
      new_password = input('Input your new password: ')
      username_repeated = session.query(User).filter(User.username == new_username).first()
      if username_repeated is not None:
        print(f'Unfortunately that username was taken. Please try again with a different one')
      else:
        newUser = User(username = new_username, password = new_password)
        session.add(newUser)
        session.commit()
        print("New user successfully created!. Now you can log in with your new credentials :)")
      # -------- END REGISTER FUNCTION -------- #
    elif user_choice == 'login':
      False
      # -------- LOGIN FUNCTION -------- #
      login_username = input("Username: ")
      login_password = input("Password: ")
      foundUser = session.query(User).filter(User.username == login_username).first()
      if foundUser is None:
        print("User not found!. Please make sure that your username is correct")
      else:
        if foundUser.password != login_password:
          print("The password is incorrect. Please try again with a different password")
        else:
          foundUser.logIns.append(LogIn())
          session.commit()
          log = session.query(LogIn).filter(LogIn.userId == foundUser.userId).order_by(LogIn.logId.desc()).first()
          print(f"You're correctly logged in at {log.loggedAt} as {foundUser.username}. :)")
          main()
      # -------- END LOGIN FUNCTION -------- #
    elif user_choice == 'exit':
      exit('Bye!')
    else:
      print("Please, type register or login. Type exit for exiting this program")

register_login()