"""
    Program 30
    Define a global dictionary. Iterate through it and print the key and value of it separately in the following format.
        a. Key is <key> and Value is <value>.
    The loop statement should be enough to extract key and value, so don't use the "get" method or [] to extract the
    value from the dictionary.
"""
list1 = {'a': 10, 'b': 50}
for key, value in list1.items():
    print('WritKey', key, 'Value', value)
