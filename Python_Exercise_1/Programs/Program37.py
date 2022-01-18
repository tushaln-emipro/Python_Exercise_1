"""
    Program 37
    Write a Python program to check if all values are the same in a dictionary.
        a. Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
        b. Check all are 23 in the dictionary.
            i. True
        c. Check all are 10 in the dictionary.
            i. False
        d. Check if any one value in the dictionary is 25
            i. False
"""
OrgDict = {'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 25}


def myfun(n):
    print(all(True if any(i == n for i in OrgDict.values()) else  value == n for value in OrgDict.values()))


myfun(23)
myfun(10)
myfun(25)
