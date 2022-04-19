#! /usr/bin/python3

import sys
from database import Item, session

items = []
currentItemId = 0

def main():
    while True:
        print("\nWhat do you want to do today?")
        print("1. View todo items")
        print("2. Create new todo item")
        print("3. Remove item")
        print("4. Exit\n")
        selection = input()
        if selection == "1": showItems()
        if selection == "2": createItem()
        if selection == "3": removeItem()
        if selection == "4": sys.exit("Goodbye!")

def showItems():
    print("Your todo lists:")
    print("---")
    items = session.query(Item)
    for item in items:
        print(f"{item.itemId}: {item.name}") 
    print("---")

def createItem():
    print("Name for the item:")
    itemName = input()
    session.add( Item (name = itemName))
    session.commit()

    
def removeItem():
    itemAmount = session.query(Item).count()
    print(f"Amount of items: {itemAmount}")

    if itemAmount < 1:
        print("Add some first!")
        return
    print("Give ID:")
    itemId = int(input())

    item = session.query(Item).filter (Item.itemId == itemId ).first()
    if item is not None:
        print(f"Item with name {item.name} was removed!")
        session.delete(item)
        session.commit()
    else:
        print("We did not find the item!")

    # Remove the item with given ID from the list items
    # pop: remove item with the given index
    # items

print("Welcome to TODO LIST MAKER VERSION 13")
main()