"""
    Program 11
    Take 3 global dictionaries as follows. Define a function, which takes those 3 dictionaries and concatenate them.
        a. dic1={1:10, 2:20}
        b. dic2={3:30, 4:40}
        c. dic3={5:50, 6:60}
        d. Output should be - {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""


def _merge(dict1, dict2, dict3):
    res = {**dict1, **dict2, **dict3}
    return res


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dict4 = _merge(dic1, dic2, dic3)
print(dict4)
