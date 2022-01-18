"""
    Program 6
    Write a Python program to calculate the sum of three given numbers,
    if the values are equal then return three times of their sum.
"""


# Way 1


def _sumfun(a, b, c):
    if a == b == c:
        print('Sum :', (a + b + c) * 3)
    else:
        print('Sum :', a + b + c)


print('One Time')
_sumfun(1, 1, 2)
print('n * 3')
_sumfun(1, 1, 1)

# Way 2

x = (lambda a, b, c: (a + b + c) * 3 if a == b == c else a + b + c)
print('One Time :', x(1, 1, 2))
print('n*3 :', x(1, 1, 1))
