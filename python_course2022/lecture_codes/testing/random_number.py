#! /usr/bin/python3

import random

number_list = [1,6,7,8,10]

def random_from_list(i_list):
    value_to_return = random.choice(i_list)
    return value_to_return


if __name__ == "__main__":
    random.seed(100)
    print(random_from_list(number_list))

#print(random_number(number_list))