#! /usr/bin/python3
from animal import Animal

def main():
    a1 = Animal("Dog", "Roy", 7)
    a2 = Animal("Cat", "Lucifer", 9)
    a3 = Animal("Tiger", "Tony", 4)
    a4 = Animal("Lion", "Leo", 11)
    a5 = Animal("Bear", "Grizz", 6)
    a6 = Animal("Crocodile", "Dundee", 24)
    a7 = Animal("Rabbit", "Roger", 1)
    a8 = Animal("Dragon", "Saphira", 56)
    a9 = Animal("Shark", "Steve", 18)
    a10 = Animal("Deer", "David", 2)

    print(a8.animal_sound("ROAAAARRR"))
    a8.set_weight(1000000)
    print(a8.weight)
    a2.set_color("Black")
    a9.set_gender("Don't want to say.")
    print(a2.color, a9.gender)
    a5.set_speed("Speed of light!")
    print(a5.speed)


    
if __name__ == "__main__":
    main()