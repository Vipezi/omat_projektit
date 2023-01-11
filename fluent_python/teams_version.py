#! usr/bin/python3

user = {

    'name' : 'John',

    'current_weight' : 80,

    'first_weight' : 75,

    'height' : 1.81,

    'first_BMI' : 0 , # first_BMI = first_weight / (height * height)

    'current_BMI' : 0,  # current_BMI = current_weight / (height * height)

    'monthly_fee' : 40  

}



def menu():

    while True :

        try :

            name = input("What is your name ?\n")

            current_weight = int(input("What is your current weight ?\n"))

            first_weight = int(input("What was your weight when you joined the gym ?\n"))

            height = float(input("What is your height ?\n"))

        except ValueError:

            print("Please enter a valid value !!!")

        else:

            break

       

   



def BMI(user):

    user["first_BMI"] = user["first_weight"] / (user["height"] * user["height"])

    user["current_BMI"] = user["current_weight"] / (user["height"] * user["height"])

    return user



def output_BMI():

    pass



def main() :

    print("Welcome to the gym")

    user = menu()
    BMI(user)
    user_current_BMI = user["current_BMI"]
    output_BMI(user_current_BMI)

   

if __name__ == "__main__":

    main()