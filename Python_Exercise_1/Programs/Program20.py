"""
    Program 20
    Write a Python program to concatenate all elements in a list into a string and return it.
"""
lt1 = [1, 2, 3, 4]

# Way 1


def concatenatefun(data):
    txt = ''
    for e in data:
        txt += str(e)
    return txt


print(concatenatefun(lt1))

# Way 2


lst_str = ''.join(map(str, lt1))
print(lst_str)
