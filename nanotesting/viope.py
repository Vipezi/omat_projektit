#! /usr/bin/python3
import random

female_names=["sari","miia","anna","tiia","kaija","katiriina","laura","varpu","merja","eeva","tiina"]
male_names=["eki","kalle","niilo","matias","juho","eero","tuomas","tero","hannu","sakari","anssi","ville"]

namelist=male_names+female_names
"""print(namelist)
print(random.choice(namelist))"""

"""def names():
    namelist=male_names+female_names
    print(namelist)
    print(random.choice(namelist))

names()"""

def names2():
   random.shuffle(namelist)
   print(namelist)
   
names2()

"""def names3():
    
    print(namelist)
     

names3()"""