from random_number import *
#print(number_list)

def test_random_from_list():
    random.seed(0)
    assert random_from_list([1,6,7,8,10]) == random.choice([1,6,7,8,10])
    '''random.seed(100)
    print(random_from_list[5,6,8,12,4])
    assert random_from_list([1,6,7,8,9]) == random.choice([1,6,7,8,9])'''