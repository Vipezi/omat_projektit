#! /usr/bin/python3
def multiplier(numbers):
    i = 0
    length_of_list = len(numbers)
    while i < length_of_list:
        if numbers[i] < 100:
            numbers[i] = numbers[i] * 2
        else:
            i+=1
    return numbers

                
        
    

print(multiplier([16, 50, 0.6, 2, 99, 12]))