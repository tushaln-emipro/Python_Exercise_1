"""
    Program 22
    Create a function which takes a value. Define a global dictionary.
    The function should be able to display a statement whether the passed value is in the dictionary or not.
"""
data = {'a': 2, 'x': 8, 'z': 1}
# Way 1


def isavailable(n):
    if n in data:
        print("Exists")
    else:
        print("Not Exists")


isavailable('a')

# Way 2

x = (lambda a: 'Exists' if a in data else 'Not Exists')
print(x('b'))
