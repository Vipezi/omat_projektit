#! /usr/bin/python3

water_temperature = []
user_input = int(input("What is the temperature of the water?"))
water_temperature.append(user_input)
while True:
    if sum(water_temperature) < 100:
        print("The water isn't hot enough")
        water_temperature.append(20)
    else:
        print("The water is boiling")
        break