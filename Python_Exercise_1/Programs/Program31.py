"""
    Program 31
    Define a dictionary, which is having keys as subject name such as maths, sci etc. and marks as values.
    Sum all the marks. and print the total.
"""
result = {"maths": 70, "sci": 75, "hindi": 85}
# Way 1


def gettotal():
    tot = 0
    for i in result.values():
        tot = tot + i
    print('Total', tot)


gettotal()

# Way 2

from functools import reduce
_sum = reduce((lambda x, y: x + y), result.values())
print('Total', _sum)
