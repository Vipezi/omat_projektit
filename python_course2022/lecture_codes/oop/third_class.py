#! /usr/bin/python3

# self is just a naming convention for the object itself
class MyThirdClass:

    def __init__(self,x):
        self.x = x

object3 = MyThirdClass(10)
object4 = MyThirdClass(10)
print(object3.x)

object3.x = 3

#object5 = MyThirdClass() type error, need one positional argument.
#print(object5.x)

