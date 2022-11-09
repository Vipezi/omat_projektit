#! /usr/bin/python3

# To multiply and convert string to int
def multiplicator(x,y,z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        multiplication = x * y * z
        return multiplication
    except ValueError as e:
        print(e)

# To sum and convert string to int
def summer(x,y,z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        sum = x + y + z
        return sum
    except ValueError as e:
        print(e)

# To substract and convert string to int
def substractor(x,y,z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        substraction = x - y - z
        return substraction
    except ValueError as e:
        print(e)

# To divide and convert string to int
def divider(x,y):
    try:
        x = int(x)
        y = int(y)
        division = x / y
        return division
    except ValueError as e:
        print(e)


def main():
    while True:
        print("Welcome to the calculator app.")
        print("1. Add ")
        print("2. Substact")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("")

        what_to_do = input("Chose your pick: ")
        if what_to_do == "1":
            # I wanted to get the input in one sentence I could have used separat inputs, but I liked this one.
            # Every input is inside and exception clause. You can put it outside of course, but this works fine at the moment.
            try:
                x, y ,z = input("Give three numbers. Separated with a space. E.g. 3 5 6: ").split(" ")
                result = summer(x,y,z)
                print("And the answer is: ", result)
                print("")
            except ValueError as e:
                print(e)
                print("You did not use the input correctly. Try again in right format separated with a space.")
                print("")

        elif what_to_do == "2":
            try:
                x, y, z = input("Give three numbers. Separated with a space. E.g. 3 5 6: ").split(" ")
                result = substractor(x,y,z)
                print("And the answer is: ", result)
                print("")
            except ValueError as e:
                print(e)
                print("You did not use the input correctly. Try again in right format separated with a space.")
                print("")

        elif what_to_do == "3":
            try:
                x, y, z = input("Give three numbers. Separated with a space. E.g. 3 5 6: ").split(" ")
                result = multiplicator(x,y,z)
                print("And the answer is: ", result)
                print("")
            except ValueError as e:
                print(e)
                print("You did not use the input correctly. Try again in right format separated with a space.")
                print("")

        elif what_to_do == "4":
            try:
                x, y = input("Give two numbers. Separated with a space. E.g. 3 5 6: ").split(" ")
                result = divider(x,y)
                print("And the answer is: ", result)
                print("")
            except ValueError as e:
                print(e)
                print("You did not use the input correctly. Try again in right format separated with a space.")
                print("")

        elif what_to_do == "5":
            print("Goodbye!")
            break

        else:
            print("Not a valid option. Try again.")
            print("")

if __name__ == "__main__":
    main()