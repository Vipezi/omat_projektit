#! /usr/bin/python3

class MySecondClass:
    x = 2

object1 = MySecondClass()
object2 = MySecondClass()

print(object1.x)

object1.x = 3

print(object2.x)
print(object1.x)