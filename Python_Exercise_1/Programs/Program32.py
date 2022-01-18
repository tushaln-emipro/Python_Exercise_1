"""
    Program 32
    students = {'Aex':{'class':'V', 'roll_id':2}, 'Puja':{'class':'V',’roll_id':3}}
        a. Using the above dictionary, print the following output.
            i. Aex
            ii. class : V
            iii. roll_id : 2
            iv. Puja
            v. class : V
            vi. roll_id : 3
"""
nums = ('i', 'ii', 'iii', 'iv', 'v', 'vi')
students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}
# Way 1

def result():
    p = 0
    for i in students:
        p = 0 if (p == 0) else p + 1
        print(nums[p]+'.', i)
        for j in students[i]:
            p = p + 1
            print(nums[p]+'.', j, ':', students[i][j])


result()

# Way 2


def finalresult():
    for i,j in students.items():
        print(i)
        for i1, j1 in j.items():
            print(i1, ':', j1)

print('Final result')
finalresult()
