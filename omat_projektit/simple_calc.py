#! /usr/bin/python3

def multiplicator(x:int,y:int):
    multiplication = x * y
    return multiplication

def summer(x:int,y:int):
    sum = x + y
    return sum

def substractor(x:int,y:int):
    substraction = x - y
    return substraction

def to_the_power_off(x: int, y: int):
    power = x**y
    return power


while True:
    x, y=input("Give two values: ").split()
    
    try:
        x = int(x)
        y = int(y)
    except Exception:
        x*x
        print("false value type(s)")
        break
        
    what_to_do = input("Do you want to add, substract or multiply these values? Type anything else to quit.")
    if what_to_do == "multiply":
        result=multiplicator(x,y)
        print(result)
    elif what_to_do == "substract":
        result=substractor(x,y)
        print(result)
    elif what_to_do == "add":
        result=summer(x,y)
        print(result)
    else:
        print("lol")
        power = to_the_power_off(x,y)
        print("Unlimited power:" , power)
        break

    