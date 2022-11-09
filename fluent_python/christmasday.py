#! /usr/bin/python3

# import Python's datetime module

import datetime

# weekdays as a tuple

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# Find out what day of the week is this year's Christmas

thisXMas    = datetime.date(2022,12,24)

thisXMasDay = thisXMas.weekday()

thisXMasDayAsString = weekDays[thisXMasDay]

print("This year's Christmas is on a {}".format(thisXMasDayAsString))

 # Find out what day of the week next new year is

nextNewYear     = datetime.date(2023,1,1)

nextNewYearDay  = nextNewYear.weekday()

nextNewYearDayAsString = weekDays[nextNewYearDay]

print("Next new year is on a {}".format(nextNewYearDayAsString))

 