"""
    Program 27
    Define a global dictionary. Define a function which takes 2 values 1st as key and 2nd as value.
    The function should add those key values to the global dictionary.
"""
data = {}


def myfun(k, v):
    data[k] = v


myfun('a', 1)
myfun('b', 2)
myfun('c', 3)
print(data)
