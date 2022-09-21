#! /usr/bin/python3

# Add items to the list and checks if you want to add an item that already exists in the list
def add_item(shopping_list, item):
    length_of_dict = len(shopping_list)
    if length_of_dict == 0:
        shopping_list.update({1: item})
    else:
        if item in shopping_list:
            are_you_sure = input("The item already exists in the list. Type 'yes' to add it again.")
            if are_you_sure == "yes":
                shopping_list[length_of_dict+1] = item
            else:
                pass
        else:
            shopping_list[length_of_dict+1] = item

# Removes item from list if it exists in it
def remove_item(shopping_list, item):
    # To make the app work more efficently I changed the input also to lowercase
    item = item.lower()
    try:
        for key, value in list(shopping_list.items()):
            if value == item:
                del shopping_list[key]
            
    except ValueError as e:
        print(e)
        print("Not found in list.")

# Begins the program
def main():
    shopping_list = {}
    while True:
        print("Welcome to the shopping list app.")
        print("1. Add ")
        print("2. Delete item from list")
        print("3. Show list")
        print("4. Exit")
        print("")
        selection = input("Select what to do with the app: ")
        
        if selection == "1":
            add = input("What do you wan to add to the shopping list? ")
            # Changing the string to lowercase so that every item is in the same format
            add = add.lower()
            add_item(shopping_list, add)
        
        elif selection == "2":
            delete = input("What do you want to remove from the shopping list? ")
            remove_item(shopping_list, delete)

        elif selection == "3":
            # Printing the items of the shopping list one by one
            print(shopping_list)

        elif selection == "4":
            # Exits the program
            break

        else:
            # If none of the options was written. Begins the program anew
            print("")
            print("Not an option. Try again.")
            

if __name__ == "__main__":
    main()
