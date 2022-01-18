"""
    Program 35
    Write a Python program to drop empty(None) Items from a given Dictionary.
        a. Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
        b. New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}
"""
OrgDict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
NewDict = {k: v for k, v in OrgDict.items() if v is not None}
print('a. Original Dictionary -', OrgDict)
print('b. New Dictionary after dropping empty items:', NewDict)
