"""
    Program 12
    Define a global dictionary with key & values.
    Iterate through it and print the key and value of it separately in the following format.
        a. WritKey is <key> and Value is <value>
"""

# Way 1

list1 = {'a': 10, 'b': 50}
for key in list1:
    print('WritKey', key, 'Value', list1[key])

# Way 2

for key, value in list1.items():
    print('WritKey', key, 'Value', value)
