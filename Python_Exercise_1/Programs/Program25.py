"""
    Program 25
    Write a Python program to count the number of strings in a list where the string length is 2 or more and the first
    and last character are the same from a given list of strings.
"""
_list = ["aba", "bca", "12341", "555"]
# Way 1


def gettotal(lt):
    tot = 0
    for i in lt:
        if len(i) >= 2 and i[0] == i[-1]:
            tot = tot + 1
    print(tot)


print(gettotal(_list))
