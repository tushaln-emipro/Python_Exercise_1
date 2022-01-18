"""
    Program 4
    Write a Python program to get the volume of a sphere with radius 15.
     a. Formula - 4/3 πr3
"""

# Way 1

pi = 3.14
radius = 15
V = 4.0 / 3.0 * pi * radius ** 3
print('The volume of the sphere is :', V)

# Way 2


def myfun(r):
    print('The volume of the sphere is :', 4.0 / 3.0 * pi * r ** 3)


myfun(15)
