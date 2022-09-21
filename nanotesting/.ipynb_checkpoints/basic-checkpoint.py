#! /usr/bin/python3

"""brothers=["Juhani" , "Aapo" , "Tuomas" , "Simeoni" , "Timo" , "Lauri" , "Eero"]
holidays=["Vappu" , "Juhannus" , "Joulu"]
lisst=["Going", "trough","the","items", "in", "our", "list"]

user=input("Give an item")
for answer in (user):
    if user in lisst:
        print("JEEEE! found")
        break
    if user not in lisst:
        print("not found")
        break"""
        

"""answer=input("Say Uusivuosi!")
question=int(input("Where would you like to put it?"))
index=question-1
holidays.insert(index, answer)
pori=28100
rauma=26100
postal=pori*rauma
result=postal
print(result)
print(brothers[6])
print(holidays)"""

import random


def is_random_number_bigger_than_median(lower_limit, upper_limit):

    random_number_to_return = random.randrange(lower_limit, upper_limit)

    if random_number_to_return > (upper_limit + lower_limit) /2:

        number_is_bigger_than_median = True 

    else:

        number_is_bigger_than_median = False



    list_to_return = [random_number_to_return, number_is_bigger_than_median]

    return list_to_return

for x in range(10):
    print(is_random_number_bigger_than_median(2, 8))

def two_random_numbers_list():
    random_number1=random.randrange(1000)
    random_number2=random.randrange(1000)
    if random_number1 < random_number2:
        random_number_list_to_return = [random_number1,random_number2]
    else:
        random_number_list_to_return = [random_number2,random_number1]
    return random_number_list_to_return

two_random_numbers_list()

for x in range(10):
    random_number_list=two_random_numbers_as_list()
    number_and_answer=is_random_number_bigger_than_median(random_number_list[0],random_number_list[1])
    print("number",number_and_answer[0],"is bigger than media",number_and_answer[1],"Range was from",random_number_list[0], "to",random_number_list[1])











