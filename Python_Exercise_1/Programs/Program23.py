"""
    Program 23
    Write a Python program to sum all the items in a list.
"""

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
_sum = reduce((lambda x, y: x + y), li)
print('Sum :', _sum)
