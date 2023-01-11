#! /usr/bin/python3

# Ville Vihtalahti
# Dániel Kovács
# Emil Eskolin
# Filee Arnauld-Christophe

# Functions: 
# main() = Begins the program. Asks for user to login, create or secret admin feature to see all users 
# make_account() = Creates user, with its features etc.
# login() = Login to account
# program() = After loggin in, can edit weight, see account info, change subscription, erase account
# edit_weight() = edit weight, changes bmi also and makes new keys "changed", "current BMI", "current weight"
# print_user_info() = Prints all the info on display for the user, maybe trying to mask password in future?
# change_subscription() = activates or deactivates subscription. Could add some sort of payment?#
# erase_account() = delete the info based on userid.
# save_to_csv() = saves every account made to a csv/dataframe
# admin() = sees all accounts and their info




import pandas as pd
from os.path import exists
import getpass
import random

def login(customers):
    try: 
        userid = int(input("Give userid: "))
    except ValueError as e:
        print("Usernumber type not valid.")
        program(customers)    
    password = getpass.getpass("Type in password: ")
    if userid in customers:
        
        if customers[userid]["password"] == password:
            return True
        else:
            return False
    else:
        print("Could not find user with the right number. ")

def make_account(customers):
    while True:
        userid = random.randint(1, 10000)
        print(f"Your usernumber is: {userid}")
        if userid not in customers.keys():
            user = {}
            name = input("Tell me the name of the user? ")
            password = getpass.getpass("Tell me the password you want to use: ")
            try:
                length_in_cm = float(input("Please tell me your length in cm: "))
                first_weight_in_kg = float(input("Please tell me your weight in kg: "))
            except ValueError as e:
                print(e)
                print("No numbers given. Length and weight are usually written in numbers if you didn't know.")
                main()
            first_BMI = first_weight_in_kg / (length_in_cm * length_in_cm)
            
            user["name"] = name
            user["password"] = password
            user["length in cm"] = length_in_cm
            user["first weight in kg"] = first_weight_in_kg
            user["first BMI"] = first_BMI * 10000
            user["subscription"] = "active"
            customers[userid] = user
            print("Your userid/numbers", customers[userid])
            return customers

        else:
            continue


def edit_weight(customers):
    try: 
        userid = int(input("Give userid: "))
    except ValueError as e:
        print("Usernumber type not valid.")
        program(customers)

    if userid in customers:
        for key in customers.keys():
            if key == userid:
                new_weight = float(input("Input new weight: "))
                customers[userid]["current weight in kg"] = new_weight
                length_in_cm = customers[userid]["length in cm"]
                customers[userid]["current BMI"] = 10000 * new_weight / (length_in_cm * length_in_cm)
                weight_change = new_weight - customers[userid]["first weight in kg"]
                bmi_change = customers[userid]["current BMI"] - customers[userid]["first BMI"]
                customers[userid]["weight change"] = weight_change
                customers[userid]["bmi change"] = bmi_change
                print(customers)

            else:
                pass
    else:
        print("User not found.")
    
def print_user_info(customers):
    try: 
        userid = int(input("Give userid: "))
    except ValueError as e:
        print("Usernumber type not valid.")
        program(customers)

    if userid in customers:
        print(customers[userid])

    else:
        print("User not found.")


## Still need to do this subscription to the end
def change_subscription(customers):
    try: 
        userid = int(input("Give userid: "))
    except ValueError as e:
        print("Usernumber type not valid.")
        program(customers)
    password = getpass.getpass("Type in password: ")
    if customers[userid]["password"] == password:
        if customers[userid]['subscription'] == "active":
            cancel = input("Type 'y' to cancel, 'n' to keep subscription. ")
            if cancel == 'y':
                customers[userid]['subscription'] = "deactive"
                print("Ending subscription.")

            elif cancel == 'n':
                print("Keeping subscription active.")

            else:
                print("Invalid input.")

        elif customers[userid]['subscription'] == "deactive":
            print("Your subscription is not active.")
            activate = input("Do you want to activate it again? y/n ")
            if activate == "y":
                customers[userid]['subscription'] = "active"
                print("Subscription activated.")

            elif activate == "n":
                print("Subscription not active.")

            else:
                print("Not a valid input.")
    else:
        print("User not found.")

def erase_account(customers):
    userid = int(input("Type userid: "))
    password = getpass.getpass("Type in password: ")
    if customers[userid]["password"] == password:
        erase = input("Type 'y' to delete account, everything else will continue the program.")
        if erase == "y":
            del customers[userid]
            print("Account deleted successfully.")
            return customers, main()
        else:
            print("Nothing deleted.")

## Try this save to csv, overwriting to csv file
def save_to_csv(customers):
    df = pd.DataFrame(customers)
    df = df.T
    df.rename(columns = {'Unnamed: 0':'userid'}, inplace = True)
    print(df)
    filename = input("Give the filename you want to use (it should end with '.csv'): ")
    if filename.endswith('.csv'):
        file_exists = exists(filename)

        if file_exists:
            print("File already exists.")
            choice = input("Do you want to overwrite existing file? (y/n) ")

            if choice == "y":
                df.to_csv(filename,index=True, header=True)
                print("File created! successfully!")

            elif choice == "n":
                new_filename = input("Input name of new file: ")
                
                if new_filename.endswith('.csv'):
                    df.to_csv(new_filename,index=True, header=True)
                    print("File created with new name.")
                else:
                    print("Not a valid filename.")
            
            else:
                print("The file was not created.")
        else:
            df.to_csv(filename,index=True, header=True)
            print("File created! successfully!")

    else:
        print("Wrong file ending.")

def program(customers):
    while True:
        print("")
        print("Press the number you want to use.")
        print("1. Edit weight")
        print("2. Get your info.")
        print("3. Change subscription.")
        print("4. Delete account.")
        print("5. log out.")
        choice = input()
        print("")
            
        if choice == "1":
            edit_weight(customers)

        elif choice == "2":
            print_user_info(customers)

        elif choice == "3":
            change_subscription(customers)

        elif choice == "4":
            erase_account(customers)
            
        elif choice == "5":
            break

def admin(customers):
    for key, value in customers.items():
        print(key, value)


def main():
    customers = {}
    while True:
        print("")
        print("Welcome to the gym app!")
        print("Login or create account? type 'c' or 'l'. Anything else will exit the program.")
        create_or_login = input()

        if create_or_login == "c":
            customers = make_account(customers)
            print("User was created successfully.")

        elif create_or_login == "l":
            successfull=login(customers)

            if successfull == True:
                print("Login was successfull!")
                program(customers)

            else:
                print("Wrong username or password.")

        elif create_or_login == "admin":
            admin(customers)

        else:
            print("Goodbye!")
            #print(customers)
            save_to_csv(customers)
            break

if __name__ == "__main__":
    main()