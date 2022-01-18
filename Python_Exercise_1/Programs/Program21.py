"""
    Program 21
    Define a global dictionary. Iterate through that dictionary and print the output in the following format.
        a. Sample Output
            i. a -- 2
            ii. x -- 8
            iii. z -- 1
"""
nums = ('i', 'ii', 'iii', 'v', 'iv')
data = {'a': 2, 'x': 8, 'z': 1}


def displaylist():
    for p, i in enumerate(data):
        print(nums[p] + '.', i, '--', data[i])


displaylist()
