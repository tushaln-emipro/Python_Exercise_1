"""
    Program 17
    Write a Python program that will accept the base and height of a triangle and compute the area.
"""

# Way 1


def displayarea(b, h):
    print('Area is', (b*h/2))


displayarea(10, 20)

# Way 2

x = (lambda b, h: (b*h/2))
print('Area is', x(10, 20))
