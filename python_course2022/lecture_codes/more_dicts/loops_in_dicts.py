#! /usr/bin/python3

# key must be unique
some_dict = {1: "value1", 2: "value2", 3: "value3"}
#print(some_dict)

# for with .items() Type is tuple
for item in some_dict.items():
    print(item)
    #print(type(item))
# item here is just a name for a variable


for key, value in some_dict.items():
    print(f"key: {key}, value: {type(value)}")

print(some_dict.items())
print(type(some_dict.items()))

for key in some_dict.keys():
    print(f"keys: {key}")


# Take the keys only
keys = some_dict.keys()
print(keys)

keys_list=list(keys)
print(keys_list[0])

# Take the items = keys and values
items = some_dict.items()
items_list = list(items)
print(items_list[0])

for value in some_dict.values():
    print(f"value : {value} type is: {type(value)}")

values =some_dict.values()
values_list = list(values)

print(type(values_list))
print(values_list[0])

# check if something is stored in something, returns True or False
print("value1" in values)
# key is int this time, not string therefore it returns False
print("1" in keys)
print(1 in keys)
