#! /usr/bin/python3

import random

def leaky_relu(relu):
    if relu > 0:
        return relu
    else:
        return 0.01 * relu

uni=round(random.uniform(0.01, 0.99),4)

result=leaky_relu(uni)
print(result)


    


