#! /usr/bin/python3

# Challenge 1
# Get Pentagonal number
# The logic is that the dots increase 5 + the lastly added amount of dots
def pentagonal(num):
    if num == 1: 
        dots =  1
    elif num == 2: 
        dots = 6
    else:
        dots = 6
        for n in range(2, num):
            print(dots)
            dots += 5 * n 
            
#pentagonal(8)

# Challenge 2
# Get dns from ip-address
import socket

def get_domain(address):
    dns = socket.gethostbxaddr(address)
    return dns

#print(get_domain("8.8.8.8"))

# Challenge 3
# Karaca's Encryption Algorithm

def karaca(word):
    word = word[::-1]
    word = word.replace("a", "0").replace("e", "1").replace("i", "2").replace("o", "2").replace("u","3")
    word += "aca"
    return word

#print(karaca("Vihtis"))

# Challenge 4
# Symbol combiner

def sxmbols(characters):
    return characters

"""print(sxmbols([
  ["#", "!"],
  ["!!", "X"]
]))"""

# Challenge 5
# Censored

def uncensor(sentence, vowels):
    counter = 0
    new_sentence = ""
    for s in sentence:
        if s == "*":
            new_sentence += vowels[counter]
            counter += 1
        else:
            new_sentence += s
            
    return new_sentence

#print(uncensor("*PP*RC*S*", "UEAE"))

# Challenge 6
# Pluralize

def pluralize(a_list):
    new_list = []
    for word in a_list:
        if word not in new_list and word + "s" not in new_list:
            new_list.append(word)
        elif word in new_list:
            index = new_list.index(word)
            new_list[index] = word + "s"
    return new_list

#print(pluralize(["chair", "pencil", "arm"]))

# Challenge 7
# Amount of digits

def digits(number):
    count = 0
    
    while number != 0:
        number //= 10
        count += 1
    return count

#print(digits(1289396387328))

# StageArray
# Transpose and array: transposed_array = list(map(list, zip(*array)))

# Challenge 8
