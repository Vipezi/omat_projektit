#! /usr/bin/python3

def my_function(m_list):
    print(f"Id of the original list{id(m_list)}")
    new_list = m_list.copy()
    new_list[0] = 3
    return new_list

my_value = [1,2,3,4]
print(my_value)
thelist = my_function(my_value)
print(f"The original list {my_value} and its id {id(my_value)}")
print(f"The changed list {thelist} and its id {id(thelist)}")

a = 1
b = a
b = 3

print(id(a), id(b))