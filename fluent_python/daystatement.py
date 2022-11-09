#! /usr/bin/python3


def day_switcher(day):
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Not a valid number.")


def day_dict(number):
    switchdict = {
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
        7 : "Sunday"
    }

    if number in switchdict:
        return switchdict[number]

    else:
        return "Not a valid number."



day = int(input("Give the number associated with weekday? "))

day_switcher(day)
weekday = day_dict(day)
print(weekday)

