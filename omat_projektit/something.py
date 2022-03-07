#! /usr/bin/python3

"""

def add_prefix_un(word):
    i = "un"
    word = [i + sub for sub in word]
    return word

def make_words_group(prefix,vocab_words):
    pre_vocab_words = [prefix + sub for sub in vocab_words]
    return pre_vocab_words


prefix = input("What prefix do you want to use: ")
vocab_words = [item for item in input("Enter the list items : ").split()]
word=[item for item in input("Give me a word: ").split()]

result = make_words_group(prefix,vocab_words)
answer=add_prefix_un(word)
counter = 0
for word in result:
    print(f"{vocab_words[counter]} :: {result[counter]}")
    counter += 1

print(answer)



def remove_suffix_ness(ness):
    if ness[-1] == "y":
        new_string=ness.replace(ness[-1], "i")
        #ness = ness[:-1]
        return new_string + "ness"
    else:
        return ness + "ness"

suffix = input("Give a word: ")

result = remove_suffix_ness(suffix)
print(result)



def noun_to_verb(sentence, index):
    verbify = sentence[index - 1]
    return verbify + "en"


sentence = input("Give me a sentence: ").split()
index = int(input("Which word should I verbify? 1 is the first word of the sentence etc. "))

result=noun_to_verb(sentence,index)
print(result)

"""

def create_inventory(item):
    for item in item:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory

def add_items(inventory,input):
    from collections import Counter
    inventory=Counter([inventory])

def decrement_items(inventory,removed_item_list):
    inventory.pop(removed_item_list,None)
    return inventory

inventory = {}
item = input("Give items to inventory: ").split()
create_inventory(item)
while True:
    print(inventory)
    more_items = input("Add item to inventory: (When you want to end type 'quit')")
    if "quit" in more_items:
        print(inventory)
        break
    else:
        add_items(inventory,more_items)
    
"""
list_input = [item for item in input("Give me a list: ").split()]

removed_item_list = [item for item in input("What to remove from list? ").split()]

dictionary=add_items(list_input)
inventory=create_inventory(dictionary)
decrement_items(inventory,removed_item_list)

print(inventory)

"""