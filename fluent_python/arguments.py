#! /usr/bin/python3

import numpy as np

def first_way(*numbers):
    result = 1
    for i in numbers:
        result*=i
    print(result)

def second_way(*numbers):
    result = 1
    for i in numbers:
        for l in i:
            result *= l

    print(result)

def third_way(*numbers):
    for i in numbers:
        last_list.extend(i)
    last_list = np.prod(numbers)
    print(last_list)


def main():
    list1 = [1,2,3]
    list2 = [4,5,6]
    list3 = [7,8,9]
    first_way(*list1, *list2, *list3)
    second_way(*list1, *list2, *list3)
    third_way(*list1, *list2, *list3)
    


if __name__ == "__main__":
    main()


"""
Ways to multiply lists with eachother
list1.extend(list2)
list1.extend(list3)
product1 = np.prod(list1, list2, list3)
#product2 = np.prod(list2)
#product3 = np.prod(list3)
#last_product = product1 * product2 * product3
print(product1)"""