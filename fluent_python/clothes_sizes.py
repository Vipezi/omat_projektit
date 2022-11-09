#! /usr/bin/python3

def cloth_switcher(length):
    if length > 165 and length < 170:
        print("XXS")
    elif length > 170 and length < 175:
        print("XS")
    elif length > 175 and length < 180:
        print("S")
    elif length > 180 and length < 185:
        print("M")
    elif length > 185 and length < 190:
        print("L")
    elif length > 190 and length < 195:
        print("XL")
    elif length > 195 and length < 200:
        print("XXL")
    elif length > 200 and length < 210:
        print("XXXL")
    else:
        print("Your size is either to big.")
        print("Too small.")
        print("Please consider changing departments.")


def size_dict(length):
    sizes = {
        "XXS" : [x for x in range(165, 171)],
        "XXS" : [x for x in range(176, 181)],
        "S" : [x for x in range(181, 186)],
        "M" : [x for x in range(186, 191)],
        "L" : [x for x in range(191, 196)],
        "XL" : [x for x in range(196, 201)],
        "XXL" : [x for x in range(201, 211)]

    }
   
    for key, value in sizes.items():
        if length in value:
            return key
        elif length not in value:
            return "too small or too big."
            
length = int(input("Please tell me your length I will tell your size? (If you are a male and fit the description) "))

size = size_dict(length)

print(f"Your size is {size}")
