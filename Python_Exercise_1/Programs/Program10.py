"""
    Program 10
    Write a Python program to check whether a specified value is contained in a group of values.
        a. Test Data :
        b. 3 -> [1, 5, 8, 3] : True
        c. -1 -> [1, 5, 8, 3] : False
"""

# Way 1

data = [1, 5, 8, 3]
print(1 in data)
print(-1 in data)

# Way 2


def isavailable(n):
    _list = [1, 5, 8, 3]
    r = n in _list
    print(r)


isavailable(1)
isavailable(-1)
