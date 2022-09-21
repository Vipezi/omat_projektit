#! /usr/bin/python3

import math

print("Calculate hypotenuse or leg from right triangle")
def legs():
    answer = input("Do you want to calculate hypotenuse or leg?")
    if answer == "hypotenuse":
        leg1 = int(input("give first leg"))
        leg2 = int(input("give second leg"))
        hypotenuse = math.sqrt(leg1**2 + leg2**2)
        print("lenght of hypotenuse is = ", hypotenuse)
        print("Then give me the hypotenuze this time.")
    elif answer == "leg":
        hypotenuse=int(input("Give hypotenuze"))
        leg = int(input("Give leg"))
        legs = math.sqrt(hypotenuse**2 - leg**2)
        print("lenght of legs is =", legs)  
    else:
         
legs()

    