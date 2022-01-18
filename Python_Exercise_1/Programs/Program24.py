"""
    Program 24
    Write a Python program to multiply all the items in a list.
"""
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
total = reduce((lambda x, y: x * y), li)
print('Total :', total)
