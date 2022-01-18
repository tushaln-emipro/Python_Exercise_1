"""
    Program 34
    Write a Python program to create a dictionary of keys x, y, and z where each key has as value
    a list from 11-20, 21-30, and 31-40 respectively. Don’t use static value for 11-20, 21-30, 31-40.
    Access the fifth value of each key from the dictionary.
        a. Expected Output
            i. First
                1. x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
                2. y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
                3. z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
            ii. Second
                1. 15
                2. 25
                3. 35
"""

x = []
y = []
z = []
# Way 1

def disoutput(t1, t2, t3):
    for a in range(t1[-1]):
        if a >= t1[0]:
            x.append(a)
    for b in range(t2[-1]):
        if b >= t2[0]:
            y.append(b)
    for c in range(t3[-1]):
        if c >= t3[0]:
            z.append(c)
    print('i. First', '\n', '1. x has value', x, '\n','2. y has value', y, '\n','3. z has value', z)
    print('ii. Second','\n', (x[4] if len(x) > 4 else 0), '\n', (y[4] if len(y) > 4 else 0), '\n', (z[4] if len(z) > 4 else 0))

disoutput((11,20),(21,30),(31,40))

# Way 2
x1 = []
y1 = []
z1 = []

def final_disoutput(t1,t2,t3):
    x1.append([a for a in range(t1[0],t1[1])])
    y1.append([b for b in range(t2[0], t2[1])])
    z1.append([c for c in range(t3[0], t3[1])])
    print('i. First', '\n', '1. x has value', x1[0], '\n', '2. y has value', y1[0], '\n', '3. z has value', z1[0])
    print('ii. Second', '\n', (x1[0][4] if len(x1[0]) > 4 else 0), '\n', (y1[0][4] if len(y1[0]) > 4 else 0), '\n',
          (z1[0][4] if len(z1[0]) > 4 else 0))


final_disoutput((11, 20), (21, 30), (31, 40))
