"""
    Program 14
    Given variables x=30 and y=20, write a Python program to print "30+20=50".
"""

# Way 1


def sumprint(x, y):
    print(x, "+", y, "=", (x + y))


sumprint(30, 20)

# Way 2


def sumprint1(x, y):
    print(str(x), "+", str(x), "=", str(x+y))


sumprint1(30, 20)
