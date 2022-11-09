#! /usr/bin/python3


## I decided to begin with asking the user to give
import maskpass
import numpy as np

def show_account_info(users, name_of_user):
    print("Password, account number and balance: ", users[name_of_user])
    print("Id of users", id(users))
    print("")


def withdraw_money(users, name_of_user):
    amount = int(input("How much money do you want to withdraw from your account? "))
    print("Id of users", id(users))
    print("")

    if users[name_of_user][-1] < amount:
        print("You do not have enough balance. Please try again!")
        print("Id of users", id(users))
        print("")

    else:
        users[name_of_user][-1] -= amount
        print("The withdraw wass successfull.")
        print("Id of users", id(users))
        print("")

    return users

def deposit_money(users, name_of_user):
    amount = int(input("How much money do you want to add to your account? "))
    print("Id of users", id(users))
    print("")
    users[name_of_user][-1] += amount

    return users

def login(users):
    print("Id of users", id(users))
    name_of_user = input("Write user you want to login into: ")
    if name_of_user in users:
        password = maskpass.askpass("Please tell me your password? ")
        if password == users[name_of_user][0]:
            print("Login was successfull!")
            while True:
                print("Press a number to select what you would want to do.")
                print("1. To deposit money.")
                print("2. To withdraw money.")
                print("3. Show account info.")
                print("4. Delete bank account.")
                print("5. Logout")
                print("")
                choice = input()
                if choice == "1":
                    deposit_money(users, name_of_user)

                elif choice == "2":
                    withdraw_money(users, name_of_user)

                elif choice == "3":
                    show_account_info(users, name_of_user)

                elif choice == "4":
                    sure = input("Press y to proceed deleting the account. ")
                    if sure == "y":
                        del users[name_of_user]
                        print("You have deleted your account and logged out successfully!")
                        print("")
                        break
                    else:
                        continue

                elif choice == "5":
                    print("Logged out successfully")
                    print("")
                    break


                

                        
        else:
            print("Invalid password or username!")

    else:
        print("Not a valid user. Try again.")
        

def make_account(users):
    print("Id of users", id(users))
    user = {}
    name = input("Please tell me the name of user of the account: ")
    balance = 0
    print("")
    if len(user)  == 0:
        password = maskpass.askpass("Please tell me what password you want to use: ")
        print("")
        account_number = np.random.randint(10000000,99999999)
        
        user[name] = [password, account_number, balance]
        return user
    elif name not in users[user]:
        password = maskpass.askpass("Please tell me what password you want to use: ")
        print("")
        account_number = np.random.randint(10000000,99999999)
        user[name] = [password, account_number, balance]
        return user
    else:
        print("The user already exists")
        print("")


def main():
    users = []
    print("Id of users", id(users))
    while True:
        print("Welcome to the bank program. Press a number to select what you would want to do.")
        print("")
        print("1. To make a new account.")
        print("2. Login to your account")
        print("3. To exit the program.")
        print("I am the administrator, I wanna see all account information! Press 13 ")
        print("")
        choice = input()
        if choice == "1":
            user = make_account(users)
            users.append(user)
            print("Id of users: ", id(user))

        elif choice == "2":
            login(user)
            print("ID of users: ", id(user))

        elif choice == "3":
            print("Goodbye!")
            break
        
        elif choice == "13":
            print(users)

        else:
            print("Not a valid answer! Try again.")

        #elif choice == "3":


if __name__ == "__main__":
    main()