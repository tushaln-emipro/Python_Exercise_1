"""
    Program 29
    Define a global empty dictionary. Iterate from 1 till 10 and fill the dictionary with the key as the number
    and value as the square of that number.
"""

# Way 1
empdict = {}
for i in range(10):
    empdict[i] = i**2
print(empdict)

# Way 2

empdict1 = {}
for x in range(1, 10): empdict1[x] = x * x
print(empdict1)
