#! /usr/bin/python3

def month_switcher():
    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
    else:
        print("Not a valid number.")


def month_dict(number):
    switchdict = {
        1 : "January",
        2 : "February",
        3 : "Mars",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }

    if number in switchdict:
        return switchdict[number]

    else:
        return "Not a valid number."



month = int(input("Give the number associated with month? "))

month_switcher(month)
month = month_dict(month)
print(month)
