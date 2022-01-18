"""
    Program 7
    Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""

# Way 1


def myfun(s, n):
    txt = ""
    for i in range(n):
        txt = txt + s
    return txt


print(myfun('xyz', 2))

# Way 2

print("abc" * 2)

# Way 3


def repfun(s, n):
    print(s * n)


repfun('123', 2)
