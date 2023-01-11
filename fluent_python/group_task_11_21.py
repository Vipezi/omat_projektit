#! /usr/bin/python3
#Filee Arnauld-Christophe, Eskolin Emil, Dániel Kovács
# Menu 
# Dictionaries that store each user's data
    # Name :
        # current weight (the most recent weight)
        # first weight
        # 
        # BMI 
            #function: 
"""
user = {

    'name' : 'John',

    'current_weight' : 80,

    'first_weight' : 75,

    'height' : 1.81,

    'first_BMI' : 0 , # first_BMI = first_weight / (height * height)

    'current_BMI' : 0,  # current_BMI = current_weight / (height * height)

    'monthly_fee' : 40  

}"""



def menu():

    while True :

        try :

            name = input("What is your name ?\n")

            current_weight = int(input("What is your current weight ?\n"))

            first_weight = int(input("What was your weight when you joined the gym ?\n"))

            height = float(input("What is your height ?\n"))

            mountly_fee = input("Did you pay your mountly fee?")
            if mountly_fee.lower() == "yes":
                mountly_fee = True
            elif mountly_fee.lower() == "no" :
                mountly_fee = False
            else :
                mountly_fee = None
        except ValueError:

            print("Please enter a valid value !!!")

        else:

            break

    return {"name" : name ,"current_weight": current_weight,"first_weight": first_weight,"height": height, "mountly_fee" : mountly_fee}

       

   



def BMI(user):

    user["first_BMI"] = user["first_weight"] / (user["height"] * user["height"])

    user["current_BMI"] = user["current_weight"] / (user["height"] * user["height"])

    return user



def output_BMI(BMI_variable) :
    if BMI_variable < 18.5 :
        return "underweight"
    # And was not used because we used elif and this is
    # in increasing order
    elif BMI_variable <= 24.9 :
        return "normal"
    elif BMI_variable <= 29.9 :
        return "overweight"
    elif BMI_variable <= 34.9 :
        return "obese"
    else :
        return "extremely obese"
        

def main() :

    print("Welcome to the gym")
    # name, current_weight, first_weight, height :
    user = menu()
    BMI(user)
    current_BMI = user["current_BMI"]
    first_BMI = user["first_BMI"]
    print(f"You are {output_BMI(current_BMI)}\nAnd you were {output_BMI(first_BMI)}")
    print(user)


   

if __name__ == "__main__":

    main()