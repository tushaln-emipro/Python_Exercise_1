"""
    Program 15
    Write a Python program to count the number occurrences of a specific character in a string.
"""

# Way 1

_str = "Hello World"
print(_str.count('l'))

# Way 2


def countchar(a, b):
    print(a.count(b.lower()))


countchar(_str, 'L')

# Way 3

l1 = ["TUSHAL", "NIMAVAT", "RAJKOT"]
print(sum(map(lambda a: 1 if 'a' in a.lower() else 0, l1)))

# Way 4


def countchar1(s):
    print(sum(map(lambda a: 1 if s.lower() in a.lower() else 0, l1)))
    print('final output', ''.join(l1).lower().count(s.lower()))

countchar1('a')
