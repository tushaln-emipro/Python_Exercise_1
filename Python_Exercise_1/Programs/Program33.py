"""
    Program 33
    Write a Python program to match key values in two dictionaries.
        a. Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
        b. Expected output: key1: 1 is present in both x and y
"""
d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}


def myfunc(lt1, lt2):
    for k in lt1:
        if(k in lt2 and lt1[k] == lt2[k]):
            print(k+':', lt1[k], 'is present in both x and y')


myfunc(d1, d2)
