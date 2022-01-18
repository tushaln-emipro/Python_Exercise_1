"""
    Program 5
    Write a Python program to get the difference between a given number and 17,
    if the number is greater than 17 return double the absolute difference.
"""

# Way 1


def myfun(n):
    if n > 17:
        return 17 - n
    else:
        return (17 - n) * 2


print(myfun(10), myfun(18))

# Way 2

x = (lambda a: 17 - a if a > 17 else (17 - a) * 2)
print(x(10), x(18))

# Way 3

x = (lambda a, b: b-a if a > b else (b-a) * 2)
print(x(10, 17), x(18, 17))
