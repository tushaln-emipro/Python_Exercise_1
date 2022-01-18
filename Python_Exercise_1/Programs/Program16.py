"""
    Program 16
    Write a Python program to display your details like name, age, address in three different lines.
        a. Expected Output
        i. Name : Joseph Mascot
        ii. Age : 39
        iii. Address : Bohemian Street, Lane 3, Greg County
"""

data = {"Name": "Joseph Mascot", "Age": 39, "Address": "Bohemian Street, Lane 3, Greg County"}
nums = ('i', 'ii', 'iii', 'v', 'iv')


def displaylist():
    for p, i in enumerate(data):
        print(nums[p] + '.', i, ':', data[i])


displaylist()
